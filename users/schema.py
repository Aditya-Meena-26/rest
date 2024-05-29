import graphene
from graphene_django.types import DjangoObjectType
from graphql import GraphQLError
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import UserSerializer
from .utils import generate_otp, send_email

class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser

class CreateUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, email, password):
        
        if CustomUser.objects.filter(email=email).exists():
            raise GraphQLError('User with this email already exists.')
        
        
        serializer = UserSerializer(data={'email': email, 'password': password})
        if serializer.is_valid():
            user = serializer.save()
            return CreateUser(user=user)
        raise GraphQLError(serializer.errors)

class LoginWithOTPMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)

    message = graphene.String()

    @staticmethod
    def mutate(root, info, email):
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise GraphQLError('User with this email does not exist.')

        otp = generate_otp()
        user.otp = otp
        user.save()

        send_email(email, otp)

        return LoginWithOTPMutation(message='OTP has been sent to your email.')

class ValidateOTPMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        otp = graphene.String(required=True)

    token = graphene.String()

    @staticmethod
    def mutate(root, info, email, otp):
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise GraphQLError('User with this email does not exist.')

        if user.otp == otp:
            user.otp = None
            user.save()
            token, _ = Token.objects.get_or_create(user=user)
            return ValidateOTPMutation(token=token.key)
        else:
            raise GraphQLError('Invalid OTP.')

class LogoutUser(graphene.Mutation):
    message = graphene.String()

    @staticmethod
    def mutate(root, info):
        if not info.context.user.is_authenticated:
            raise GraphQLError('User is not authenticated.')

        try:
            info.context.user.auth_token.delete()
            return LogoutUser(message='Successfully logged out.')
        except Exception as e:
            raise GraphQLError(str(e))

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    login_with_otp = LoginWithOTPMutation.Field()
    validate_otp = ValidateOTPMutation.Field()
    logout_user = LogoutUser.Field()

class Query(graphene.ObjectType):
    dummy_field = graphene.String()

schema = graphene.Schema(query=Query, mutation=Mutation)
