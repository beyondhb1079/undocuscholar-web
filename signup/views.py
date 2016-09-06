from django.shortcuts import render

# Create your views here.
from django.contrib import auth
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

# TODO: Clean this up, add a forgot password to login, password reset, email
# confirmation. Also after the Beyond HB 1079 team is all added, make sure
# is_staff isn't set to true for other strange people
def index(request):
    # TODO: validate_password(request.POST['password'])
    if request.user.is_authenticated():
        return HttpResponseRedirect("/admin/")
    
    if request.method == 'GET':
        return render(request, 'signup/register.html')
    else:
        if request.POST['password'] != request.POST['confirm_password']:
            return render(request, 'signup/register.html', {
                'form': {
                    'non_field_errors': ['Passwords don\'t match'],
                    'username': request.POST['username'],
                    'email': request.POST['email']
                }
            })
        
        try: 
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], email=request.POST['email'])
            user.is_staff = True
            user.groups.add(Group.objects.filter(name='Moderator')[0])
            user.save()
            return HttpResponseRedirect("/admin/")
        except (IntegrityError):
            return render(request, 'signup/register.html', {
                'form': {
                    'non_field_errors': ['That username is already taken.'],
                    'username': request.POST['username'],
                    'email': request.POST['email']
                },
            })
        except Exception as e:
            return render(request, 'signup/register.html', {
                'form': {
                    'non_field_errors': [e.message],
                    'username': request.POST['username'],
                    'email': request.POST['email']
                }
            })