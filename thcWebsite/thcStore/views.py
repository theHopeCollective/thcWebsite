from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from  cart.forms import CartAddProductForm
from django.views.generic import CreateView
from .forms import ProductCreateForm
from django.urls import reverse_lazy

def product_list(request, category_slug=None):
# Catalog View
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request,
                  'thcStore/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,},)

def product_detail(request, id, slug):
#product View
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'thcStore/product/detail.html',
              {'product': product,
               'cart_product_form': cart_product_form})

class product_create(CreateView):
        # form_class = forms.ProductCreateForm
        form_class = ProductCreateForm
        success_url = reverse_lazy("login")
        template_name = "thcStore/product/create.html"
