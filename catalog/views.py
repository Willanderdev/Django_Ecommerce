from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Product, Category
from watson import search as watson


class Product_listView(ListView):
    model = Product
    context_object_name = 'produtos'
    template_name = 'catalog/product_list.html'
    paginate_by = 3
    ordering = 'id'
   
    def get_queryset(self):
        queryset = Product.objects.all()
        pesquisa = self.request.GET.get('pesquisa', '')
        if pesquisa:
            queryset = watson.filter(queryset, pesquisa) 
        return queryset
    


class CategoryListView(ListView):
    context_object_name = 'product_list'
    template_name = 'catalog/category.html'
    paginate_by = 3
    ordering = 'id'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])
    
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

# def category(request, slug):
#     category = Category.objects.get(slug=slug)
#     context = {
#         'current_category': category,
#         'product_list': Product.objects.filter(category=category)
#     }
#     return render(request, 'catalog/category.html', context)


def product(request, slug):
    product = Product.objects.get(slug=slug)
    prod = Product.objects.all()
    context = {
        'product': product,
        
    }
    return render(request, 'catalog/product.html', context)
