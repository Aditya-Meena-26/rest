from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message

@login_required
def send_message(request):
    if request.method == 'POST':
        # Handle form submission to send a message
        # Add your logic here to handle sending a message
        pass
    else:
        # Render the form to compose a message
        return render(request, 'compose_message.html')

@login_required
def inbox(request):
    received_messages = Message.objects.filter(receiver=request.user)
    return render(request, 'inbox.html', {'received_messages': received_messages})

@login_required
def message_detail(request, message_id):
    message = Message.objects.get(id=message_id)
    if message.receiver == request.user:
        message.is_read = True
        message.save()
    return render(request, 'message_detail.html', {'message': message})
