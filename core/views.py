from django.contrib import messages
from django.shortcuts import render

from .forms import ContactForm


def index(request):
    return render(request, 'index.html')


def contact(request):
    form = ContactForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, 'Enviado com sucesso')
            form = ContactForm()
        else:
            messages.error(request, 'Erro ao enviar formulário')

    context = {
        'form': form
    }

    return render(request, 'contact.html', context)


def product(request):
    return render(request, 'product.html')
