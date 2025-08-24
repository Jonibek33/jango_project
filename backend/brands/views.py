from django.shortcuts import render

# Create your views here.

def brands(request):
    context = {
        'title': 'Brands',
        'message': 'A list of available brands for the system.',
    }
    return render(request, 'brands.html', context)