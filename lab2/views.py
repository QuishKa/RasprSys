from django.shortcuts import render
import math

def index(request):
    if request.method == 'POST':
        amount = math.floor(float(request.POST['amount']))
        rate = float(request.POST['rate'])
        res = amount * rate
        return render(request, 'html/lab2.html', {'res': res})
    return render(request, 'html/lab2.html')