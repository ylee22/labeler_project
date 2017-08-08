from django import forms

from polls.models import Image


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('caption', 'file', )