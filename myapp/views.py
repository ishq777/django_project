from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

# Create your views here.
def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")


    form = ImageForm()
    images = Image.objects.all()
    return render(request, "myapp/home.html",{'images':images, "form":form})
