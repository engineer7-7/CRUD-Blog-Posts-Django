from django.shortcuts import render


# Create your views here.

# view to display the main HTML page
def display_page(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def display_projects(request):
    return render(request, 'pages/projects.html')


def index(request):
    return render(request, 'pages/index.html')
