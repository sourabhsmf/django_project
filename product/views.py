from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import addProductForm
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    context = {'products' : Product.objects.all()}
    return render(request, 'product/index.html' , context)

def add(request):
    if request.method == "POST":
        form = addProductForm(request.POST)
        
        if form.is_valid() :
            newProduct = Product(productName = form.cleaned_data['product_name'] , productPrice = form.cleaned_data['product_price'] , productURL = form.cleaned_data['product_url'])
            newProduct.save()
            print(newProduct.id)
            return HttpResponseRedirect(redirect_to='view/' + str(newProduct.id))
        else:
            return render(request, 'product/add.html', context={'form':form})
    else:
        return render(request, 'product/add.html')
        

def delete(request, productId):
    return render(request, 'product/delete.html' , {'product': get_object_or_404(klass=Product, id=productId)})

def view(request, productId):
    return render(request, 'product/view.html', {'product': get_object_or_404(klass=Product, id=productId)})
