from django.http import HttpResponse

def home(request):
    return HttpResponse("Hi there. This is a sample boilerplate view.")