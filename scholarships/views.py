from django.http import HttpResponse
from django.template import loader

from .models import *


# Create your views here.
def index(request):
    template = loader.get_template('scholarships/index.html')
    context = {
        'scholarships': Scholarship.objects.all(),
    }
    return HttpResponse(template.render(context, request))

def detail(request, scholarship_id):
    return HttpResponse("You're looking at scholarship %s." % scholarship_id)
