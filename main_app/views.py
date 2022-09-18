from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# View Functions:

# Home
def home(request):
    return render(request, 'home.html')

# add following to bottom of CreateListing class
# def form_valid(self, form):
#     form.instance.user = self.request.user 
#     return super().form_valid(form)
# don't forget to use LoginRequiredMixin in class-based views and @login_required in def


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

# for ks later
# @login_required
# def listings_index(request):
#   listings = Listing.objects.filter(user=request.user)
#   # You could also retrieve the logged in user's cats like this
#   # cats = request.user.cat_set.all()
#   return render(request, 'listings/index.html', { 'listings': listings })