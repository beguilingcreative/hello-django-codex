from dataclasses import dataclass
from datetime import datetime
import math
import random
from django.shortcuts import render, redirect
from .forms import MessageForm, FactorialForm

# In-memory list to store messages during runtime
messages = []

QUOTES = [
    "Talk is cheap. Show me the code.",
    "Simple is better than complex.",
    "Errors should never pass silently.",
    "Now is better than never.",
]

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


def utilities(request):
    result = None
    if request.method == 'POST':
        form = FactorialForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            result = math.factorial(number)
    else:
        form = FactorialForm()

    quote = random.choice(QUOTES)
    return render(request, 'hello/utilities.html', {
        'form': form,
        'result': result,
        'quote': quote,
    })
