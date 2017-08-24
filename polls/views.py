from django.shortcuts import render, redirect
from rest_framework import generics

from polls.forms import DocumentForm
from polls.models import Image

from . import serializers

""" Takes """

def home(request):
    documents = Image.objects.all()
    print(documents.count())
    return render(request, 'home.html', { 'documents': documents })


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

class ListImages(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = serializers.ImageSerializer
