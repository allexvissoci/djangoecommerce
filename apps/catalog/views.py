from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views import generic


class ProductsListView(generic.ListView):

    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'product_list'


class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        context['current_category'] = get_object_or_404(Category, slug=slug)
        return context


class ProductListView(generic.ListView):

    template_name = 'catalog/product.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.get(slug=self.kwargs['slug'])


product_list = ProductsListView.as_view()
category = CategoryListView.as_view()
product = ProductListView.as_view()
