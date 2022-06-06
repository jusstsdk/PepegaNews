from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from users.forms import UserCreationForm
from news.models import Author

import logging

logger = logging.getLogger('main')


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        logger.info('Checked registration')
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            Author.objects.create(user=user)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        logger.info('User registered')
        return render(request, self.template_name, context)
