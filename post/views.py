from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
import requests
from django.conf import settings

base_url = settings.BASE_URL

def blog_list(request):
    """To list api and show blog list."""

    # Get access and refresh token from session
    access = request.session.get('access')
    url = '/'.join([base_url, 'rest/post/'])
    response = requests.get(url, headers={'Authorization': 'Bearer {}'.format(access)})
    if response.ok:
        return render(request, 'blog_list.html', {'blog_list': response.json()})
    return render(request, 'blog_list.html', {'blog_list': []})

def create_blog(request):
    """To create blog."""

    access = request.session.get('access')
    url = '/'.join([base_url, 'rest/post/'])
    if request.method == 'POST':
        response = requests.post(url, data=request.POST, headers={'Authorization': 'Bearer {}'.format(access)})
        if response.ok:
            return HttpResponseRedirect(reverse('post:blog-list'))
    return render(request, 'create_blog.html')


def like_unlike_blog(request):
    """To manage like unlike."""

    access = request.session.get('access')
    url = '/'.join([base_url, 'rest/post/likes'])

    if request.method == 'POST':
        response = requests.post(
            url, headers={'Authorization': 'Bearer {}'.format(access)}, data={'user_id':request.POST.get('user_id'),'like_status':request.POST.get('submit'), 'blog_id': request.POST.get('blog_id')})
        return HttpResponseRedirect(reverse('post:blog-list'))
