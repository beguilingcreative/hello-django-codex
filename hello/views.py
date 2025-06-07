from dataclasses import dataclass
from datetime import datetime
from django.shortcuts import render, redirect
from .forms import MessageForm

# In-memory list to store messages during runtime
messages = []

@dataclass
class Message:
    title: str
    content: str
    created_at: datetime

def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = Message(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                created_at=datetime.now(),
            )
            messages.insert(0, msg)
            return redirect('index')
    else:
        form = MessageForm()

    return render(request, 'hello/index.html', {
        'form': form,
        'messages': messages,
    })
