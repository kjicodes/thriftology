from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Listing, Photo
import uuid
import boto3
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# View Functions:

# Home
def home(request):
    return render(request, 'home.html')

# About


def about(request):
    return render(request, 'about.html')

# add following to bottom of CreateListing class
# def form_valid(self, form):
#     form.instance.user = self.request.user
#     return super().form_valid(form)
# don't forget to use LoginRequiredMixin in class-based views and @login_required in def


class CreateListing(LoginRequiredMixin, CreateView):
  model = Listing
  fields = ['title', 'description', 'price', 'size', 'condition', 'gender']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


@login_required
def listings_index(request):
    listings = Listing.objects.all()
    return render(request, 'listings/index.html', {'listings': listings})


@login_required
def mythrifts_index(request):
    user = request.user
    return render(request, 'mythrifts/index.html', {'user': user})
