from django.http import HttpResponse

def home(request):
    return HttpResponse("This is the landing page")

def test(request):
    return HttpResponse("This is self made testing page")

def show(request):
    return HttpResponse("This is show page where data of all the other persons would be shown and also with their details")