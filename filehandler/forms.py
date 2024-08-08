from django import forms
from filehandler.models import *

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file']