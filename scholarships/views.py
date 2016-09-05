from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("You're looking at the list of scholarships")

def detail(request, scholarship_id):
    return HttpResponse("You're looking at scholarship %s." % scholarship_id)
