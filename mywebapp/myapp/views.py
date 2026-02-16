from django.http import HttpResponse

def home(request):
    return HttpResponse("This is the landing page")

def test(request):
    return HttpResponse("This is self made testing page")