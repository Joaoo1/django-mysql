from django.contrib import messages
from django.shortcuts import redirect, render, redirect

from .forms import ContactForm, ProductModelForm
from .models import Product


def index(request):
    context = {
        'products': Product.objects.all()
    }

    return render(request, 'index.html', context)


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
    print(request.user)
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProductModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto salvo com sucesso')
                form = ProductModelForm()
            else:
                messages.error(request, 'Erro ao salvar produto.')
        else:
            form = ProductModelForm()

        context = {'form': form}
        return render(request, 'product.html', context)
    else:
        return redirect('index')
