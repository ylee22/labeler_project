from django.shortcuts import render, redirect

from polls.forms import DocumentForm
from polls.models import Image

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