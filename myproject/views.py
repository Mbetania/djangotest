from .models import User
from django.http import HttpResponseRedirect

def add_user(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    user = User(name=name)
    user.save()
    return HttpResponseRedirect('/')

  retur render(request, 'addUser.html')