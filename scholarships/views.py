from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import *

def index(request):
    scholarship_list = Scholarship.objects.all()
    paginator = Paginator(scholarship_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        scholarships = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        scholarships = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        scholarships = paginator.page(paginator.num_pages)
    return render(request, 'scholarships/index.html', {'scholarships': scholarships})

def collection(request):
    scholarship_list = Scholarship.objects.all()
    paginator = Paginator(scholarship_list, 25)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        scholarships = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        scholarships = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        scholarships = paginator.page(paginator.num_pages)
    return render(request, 'scholarships/collection.html', {'scholarships': scholarships})

def detail(scholarship_id):
    return 'TODO: Page info for scholarship with ID: %s' % scholarship_id