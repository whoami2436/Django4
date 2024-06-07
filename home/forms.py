from django import forms
from .models import Portfolio


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'description', 'age', 'date_of_birth', 'location', 'education', 'skills', 'experience', 'project', 'contact']