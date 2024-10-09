from django.shortcuts import render

def index(request):
    return render(request, 'led/html/index.html')

def led(request):
    return render(request, 'led/html/led.html')

def ssid(request):
    return render(request, 'led/html/ConfIP_SSID_JS.html')