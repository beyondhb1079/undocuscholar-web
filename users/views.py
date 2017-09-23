from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.shortcuts import render, redirect


from django import forms

class SwitchInput(forms.CheckboxInput):
    template_name = 'switch.html'
    def __init__(self, on="On", off="Off", attrs=None, check_test=None):
        super(SwitchInput, self).__init__(attrs, check_test)
        self.on = on
        self.off = off

    def get_context(self, name, value, attrs):
        context = super(SwitchInput, self).get_context(name, value, attrs)
        context['widget']['on'] = self.on
        context['widget']['off'] = self.off
        return context

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100, empty_value='guac')
    your_choice = forms.BooleanField(widget=SwitchInput("Parent", "Student"), initial=True, label="Are you a parent or student?")
    your_date = forms.DateField(label='Your Date')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = NameForm()
    return render(request, 'users/register.html', {'form': form})


def update(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserChangeForm()
    return render(request, 'users/change.html', {'form': form})

def login(request):
    return render("TODO")