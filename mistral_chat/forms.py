from django import forms


class UploadPDFForm(forms.Form):
    file = forms.FileField()
    prompt = forms.CharField(max_length=16000)