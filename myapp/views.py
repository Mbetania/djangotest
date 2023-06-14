from django.shortcuts import render
from .models import User
from django.http import HttpResponseRedirect
# Create your views here.
def add_user(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    user = User(name=name)
    user.save()
    return HttpResponseRedirect('/')

  retur render(request, 'addUser.html')