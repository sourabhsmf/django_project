from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def index(request):
    context = {'products' : Product.objects.all()}
    return render(request, 'product/index.html' , context)

def add(request):
    errorMessage = {}
    try:
        newProduct = Product(productName = request.POST['product-name'] , productPrice = request.POST['product-price'], productURL = request.POST['product-url']).save()
    except:
        print("Exception occurred")
    return render(request, 'product/add.html', context={'error_message':errorMessage})

def delete(request, productId):
    return render(request, 'product/delete.html' , {'product': get_object_or_404(klass=Product, id=productId)})

def view(request, productId):
    return render(request, 'product/view.html', {'product': get_object_or_404(klass=Product, id=productId)})
