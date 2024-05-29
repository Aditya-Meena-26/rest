from django.urls import path
from . import views

urlpatterns = [
    path('compose/', views.send_message, name='compose_message'),
    path('inbox/', views.inbox, name='inbox'),
    path('message/<int:message_id>/', views.message_detail, name='message_detail'),
]
