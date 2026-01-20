from django.shortcuts import render, redirect
from .forms import FileForm
from .models import FileUpload

def home(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("fileupload:home")

    form = FileForm()
    files = FileUpload.objects.all()
    return render(request,"fileupload/base.html",{'form':form, "files":files})

# Create your views here.
