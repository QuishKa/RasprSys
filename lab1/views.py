from django.shortcuts import render
from .forms import NameForm

def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            context = {
                'name':request.POST['name'],
                'last_name':request.POST['last_name'],
                'email':request.POST['email']
            }
            return render(request, 'html/lab1info.html', context)
        else:
            form = NameForm()
            return render(request, 'html/lab1.html', {"form": form})
    else:
        form = NameForm()
    return render(request, 'html/lab1.html', {"form": form})
