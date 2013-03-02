from django.http import HttpResponse

def index(request, query):
    return HttpResponse(query)