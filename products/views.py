from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Product
from .forms import ProductForm


# FUNCTION BASED VIEWS

# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'products/product_list.html', {'products': products})
#
#
# def product_detail(request, id):
#     obj = get_object_or_404(Product, id=id)
#     return render(request, 'products/product_detail.html', {'object': obj})
#
#
# def product_create(request):
#     form = ProductForm()
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             Product.objects.create(**form.cleaned_data)
#             return redirect('products:product_list')
#     return render(request, 'products/product_confirm_delete.html', {'form': form})
#
#
# def product_update(request, id):
#     obj = get_object_or_404(Product, id=id)
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             for k, v in form.cleaned_data.items():
#                 setattr(obj, k, v)
#             obj.save()
#             return redirect('products:product_detail', id=obj.id)
#     initial = {'title': obj.title, 'description': obj.description, 'price': obj.price, 'summary': obj.summary,
#                'featured': obj.featured}
#     form = ProductForm(initial=initial)
#     return render(request, 'products/product_update.html', {'form': form})
#
#
# def product_delete(request, id):
#     obj = get_object_or_404(Product, id=id)
#     if request.method == 'POST':
#         obj.delete()
#         return redirect('products:product_list')
#     return render(request, 'products/product_create.html', {'object': obj})


# CLASS BASED VIEWS


class ProductListView(ListView):
    queryset = Product.objects.all()


class ProductDetailView(DetailView):
    queryset = Product.objects.all()


class ProductCreateView(CreateView):
    template_name = 'products/product_create.html'
    form_class = ProductForm
    queryset = Product.objects.all()


class ProductUpdateView(UpdateView):
    template_name = 'products/product_update.html'
    form_class = ProductForm
    queryset = Product.objects.all()


class ProductDeleteView(DeleteView):
    template_name = 'products/product_confirm_delete.html'
    queryset = Product.objects.all()

    def get_success_url(self):
        return reverse('products:product_list')
