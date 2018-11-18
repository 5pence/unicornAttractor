from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('ticket_list'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
    