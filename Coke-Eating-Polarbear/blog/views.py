from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def service_details(request):
    return render(request, 'service-details.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def traffic(request):
    return render(request, 'traffic_recognize.html')