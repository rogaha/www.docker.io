from django import forms
from models import Image
from django_filepicker.widgets import FPFileWidget


class NewsSubscribeForm(forms.Form):

    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'email address'}))

class FilePickerForm(forms.Form):

    fpfile = forms.CharField(widget=FPFileWidget)
