from django.shortcuts import render

def index(request):
    return render(request, '../templates/main_pages/index.html')
