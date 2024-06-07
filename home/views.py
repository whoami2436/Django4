from django.shortcuts import render, redirect
from .forms import PortfolioForm
from django.http import HttpResponse

# Create your views here.
def home__page(request):
    return render(request, "index.html")

def about__page(request):
    return HttpResponse("About")


def portfolio_form(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Uğurlu post etdikdə yönləndiriləcək URL
    else:
        form = PortfolioForm()
    return render(request, 'portfolio_form.html', {'form': form})