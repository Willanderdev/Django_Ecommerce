from django.shortcuts import render

from .forms import ContatoForm
from django.contrib import messages
from checkout.models import CartItem



def index(request):
    cart = CartItem.objects.count()
    context = {
        'cart':cart
    }
    return render(request, 'index.html', context=context)


def contact(request):
    # se o form estiver preenchido, envie o email, se o form for igual a None(vazio), ñao vai  estar válido e não vai enviar..
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        messages.success(
            request, 'E-mail enviado com sucesso, logo entrarei em contato com vc :)')

        form = ContatoForm()
    else:
        print(form.errors.as_data())
        
    form = ContatoForm()
    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)


def product(request):
    return render(request, 'product.html')
