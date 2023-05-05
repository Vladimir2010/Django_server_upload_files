from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import os 


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'templates/upload.html', context)


def download(request):
    return render(request, '/')





# Create your views here.
