from django.shortcuts import render

# Create your views here.
from .models import User
from django.http import HttpResponseRedirect

def add_user(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    user = User(name=name)
    user.save()
    return HttpResponseRedirect('/')

  return render(request, 'addUser.html')