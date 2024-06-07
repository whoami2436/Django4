from django.urls import path
from . import views
from .forms import PortfolioForm

urlpatterns = [
    # Digər URL-lər
   path('portfolio/', views.portfolio_form, name='portfolio_form'), 
    path('portfolio/form/', views.portfolio_form, name='portfolio_form'),
]
