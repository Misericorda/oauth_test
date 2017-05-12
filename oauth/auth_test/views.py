from django.shortcuts import render, redirect
from django.contrib.auth import logout

from . import services


def main_page(request):
    # using the same view for logout
    if request.GET.get('log_out') == 'True':
        logout(request)
        return redirect('/')
    else:
        # if user's already authenticated
        # make api call and send the data to the template
        if request.user.is_authenticated():
            #using services.py for helper functions
            friends = services.get_friends(request.user.username)
            return render(request, 'base.html', {'friends': friends})
        # user's not authenticated, show main page
        return render(request, 'base.html')
