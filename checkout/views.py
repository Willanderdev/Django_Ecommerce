# coding=utf-8

from django.shortcuts import get_object_or_404, redirect
from paypal.standard.forms import PayPalPaymentsForm
from django.views.generic import RedirectView, TemplateView, ListView, DetailView
from django.forms import modelformset_factory
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.conf import settings
from catalog.models import Product

from .models import CartItem, Order


class CreateCartItemView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        if self.request.session.session_key is None:
            self.request.session.save()
        cart_item, created = CartItem.objects.add_item(
            self.request.session.session_key, product
        )
        # if created:
        #     messages.success(self.request, 'Produto adicionado')
        # else:
        #     messages.success(self.request, 'Produto atualizado')
        return reverse('cart')


class CartItemView(TemplateView, CreateCartItemView):

    template_name = 'checkout/cart.html'

    def get_formset(self, clear=False):
        CartItemFormSet = modelformset_factory(
            CartItem, fields=('quantity',), can_delete=True, extra=0
        )
        session_key = self.request.session.session_key
        if session_key:
            if clear:
                formset = CartItemFormSet(
                    queryset=CartItem.objects.filter(cart_key=session_key)
                )
            else:
                formset = CartItemFormSet(
                    queryset=CartItem.objects.filter(cart_key=session_key),
                    data=self.request.POST or None
                )
        else:
            formset = CartItemFormSet(queryset=CartItem.objects.none())
        return formset

    def get_context_data(self, **kwargs):
        context = super(CartItemView, self).get_context_data(**kwargs)
        context['formset'] = self.get_formset()
        return context

    def post(self, request, *args, **kwargs):
        formset = self.get_formset()
        context = self.get_context_data(**kwargs)
        if formset.is_valid():
            formset.save()
            # messages.success(request, 'Carrinho atualizado',
            #                  fail_silently=True)
            context['formset'] = self.get_formset(clear=True)
        return self.render_to_response(context)


class CheckoutView(LoginRequiredMixin, TemplateView):

    template_name = 'checkout/checkout.html'

    def get(self, request, *args, **kwargs):
        session_key = request.session.session_key
        if session_key and CartItem.objects.filter(cart_key=session_key).exists():
            cart_items = CartItem.objects.filter(cart_key=session_key)
            order = Order.objects.create_order(
                user=request.user, cart_items=cart_items
            )
            cart_items.delete()
        else:
            messages.info(request, 'Não há itens no carrinho de compras')
            return redirect('cart')
        response = super(CheckoutView, self).get(request, *args, **kwargs)
        response.context_data['order'] = order
        return response
    
# view que mostra todos os pedidos do user logado    
class OrderListView(LoginRequiredMixin, ListView):
    
    template_name = 'checkout/order_list.html'
    paginate_by = 20
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
#view que mostra o pedido com detalhes    
class OrderDetailView(LoginRequiredMixin, DetailView):
    
    template_name = 'checkout/order_detail.html'
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class PaypalView(LoginRequiredMixin, TemplateView):

    template_name = 'checkout/paypal.html'

    def get_context_data(self, **kwargs):
        context = super(PaypalView, self).get_context_data(**kwargs)
        order_pk = self.kwargs.get('pk')
        order = get_object_or_404(
            Order.objects.filter(user=self.request.user), pk=order_pk
        )
        paypal_dict = order.paypal()
        paypal_dict['return_url'] = self.request.build_absolute_uri(
            reverse('order_list')
        )
        paypal_dict['cancel_return'] = self.request.build_absolute_uri(
            reverse('order_list')
        )
        paypal_dict['notify_url'] = self.request.build_absolute_uri(
            reverse('paypal-ipn')
        )
        context['form'] = PayPalPaymentsForm(initial=paypal_dict)
        return context


def paypal_notification(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED and \
            ipn_obj.receiver_email == settings.PAYPAL_EMAIL:
        try:
            order = Order.objects.get(pk=ipn_obj.invoice)
            order.complete()
        except Order.DoesNotExist:
            pass


valid_ipn_received.connect(paypal_notification)
