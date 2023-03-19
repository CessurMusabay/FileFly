from django import forms
from .models import Transfer
from django.contrib.auth.hashers import make_password



class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.password = make_password(instance.password)
            instance.save()
        return instance