from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm


def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MessageForm()

    messages = Message.objects.order_by('-created_at')
    return render(request, 'hello/index.html', {
        'form': form,
        'messages': messages,
    })
