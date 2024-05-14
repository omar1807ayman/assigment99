from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import ProductForm


def index(request):
    return render(request, 'index.html')
def add(request):
    return render(request, 'add.html')


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success_url/')  # Redirect after POST
    else:
        form = ProductForm()

    return render(request, 'product.html', {'form': form})
