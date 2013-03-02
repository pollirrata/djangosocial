from django.http import HttpResponse

def index(request):
    return HttpResponse("Index")

def query(request, query):
    return HttpResponse(query)