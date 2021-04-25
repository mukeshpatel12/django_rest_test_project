import json
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import load_backend
from django.contrib.auth import login as auth_login
from django.conf import settings

base_url = settings.BASE_URL

def signup(request):
    """To call signup api."""
    if request.method == 'POST':
        url = '/'.join([base_url, 'rest/user/'])
        response = requests.post(url, data=request.POST)
        if response.ok:
            return HttpResponseRedirect(reverse('user:login'))
        return render(request, 'signup.html', response.json())
    return render(request, 'signup.html')


def login(request):
    """To call login api."""
    if request.method == 'POST':
        url = '/'.join([base_url, 'api/token/'])
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            if not hasattr(user, 'backend'):
                for backend in settings.AUTHENTICATION_BACKENDS:
                    if user == load_backend(backend).get_user(user.pk):
                        user.backend = backend
                        break
            if hasattr(user, 'backend'):
                auth_login(request, user)
            data = {
                'username': request.POST.get('username'),
                'password': request.POST.get('password'),
            }
            token_response = requests.post(url, data=data)
            data = token_response.content
            token_response_dict = json.loads(data.decode("UTF-8"))

            # Set access and refresh token in session
            request.session['access'] = token_response_dict.get("access")
            request.session['refresh'] = token_response_dict.get("refresh")
            return HttpResponseRedirect(reverse('post:blog-list'))
        return render(request, 'login.html', {'error_msg': "Incorrect username or password!"})
    return render(request, 'login.html')

        






