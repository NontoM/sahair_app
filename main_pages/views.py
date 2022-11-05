from django.shortcuts import render

def index(request):
    return render(request, '../templates/main_pages/index.html')

def customerDashboard(request): 
    return render(request, '../templates/main_pages/customer_dashboard.html', {})
