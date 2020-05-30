from django import forms

from .models import Contribution

class ContributionCreationForm(forms.ModelForm):
    
    class Meta:
        model = Contribution
        fields = ['quantity']