from django.shortcuts import render

# Create your views here.

def cars(request):
    context = {
        'title': 'Cars',
        'message': 'A list of available cars for the system.',
    }
    return render(request, 'cars.html', context)