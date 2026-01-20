from django import forms
from .models import FileUpload

class FileForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = '__all__'
        labels = {"file":""}
