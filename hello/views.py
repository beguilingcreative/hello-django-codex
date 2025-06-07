from dataclasses import dataclass
from datetime import datetime
import math
import random
import os
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import MessageForm, FactorialForm
from azure.data.tables import TableServiceClient

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


def panic_records(request):
    """Display entries from Azure Table Storage with PartitionKey 'PanicTracker'."""
    conn_str = os.environ.get('AzureWebJobsCosmosDBConnectionString')
    if not conn_str:
        return render(request, 'hello/panic_records.html', {
            'page_obj': None,
            'error': 'Connection string not configured.'
        })

    table_name = os.environ.get('COSMOS_TABLE_NAME', 'PanicTracker')
    service = TableServiceClient.from_connection_string(conn_str)
    table = service.get_table_client(table_name)

    # Retrieve all entities with the specified partition key
    entities = table.query_entities("PartitionKey eq 'PanicTracker'")
    items = list(entities)

    paginator = Paginator(items, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'hello/panic_records.html', {
        'page_obj': page_obj,
        'error': None,
    })
