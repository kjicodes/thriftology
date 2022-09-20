from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Listing, Photo
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3

S3_BASE_URL = 'https://s3.ca-central-1.amazonaws.com/'
BUCKET = 'thriftologysei'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/listings/')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def listings_index(request):
    listings = Listing.objects.all().filter(buyer=None)
    return render(request, 'listings/index.html', {'listings': listings})

# Kateleen - added 'listings_detail' function
def listings_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, 'listings/detail.html', {'listing': listing})


@login_required
def buy_listing(request, listing_id):
    user = request.user
    buyer_id = user.id
    listings = Listing.objects.get(id=listing_id).buyer
    Listing.objects.get(id=listing_id).buyer.save()
    return redirect(request, 'mythrifts/index.html', {'user': user })


@login_required
def mythrifts_home(request):
    user = request.user
    return render(request, 'mythrifts/index.html', {'user': user})


@login_required
def mythrifts_listings(request):
    user = request.user
    user_id = user.id
    unsold = Listing.objects.all().filter(seller=user_id).filter(buyer=None)
    # print(f"user={user}, user id={user_id} listings = {unsold}")
    return render(request, 'mythrifts/index.html', {'user': user, 'listings': unsold})


@login_required
def mythrifts_sold(request):
    user = request.user
    user_id = user.id
    sold = Listing.objects.all().filter(seller=user_id).exclude(buyer=None)
    # print(f"user={user}, user id={user_id} listings = {sold}")
    return render(request, 'mythrifts/index.html', {'user': user, 'listings': sold})


@login_required
def mythrifts_bought(request):
    user = request.user
    user_id = user.id
    bought = Listing.objects.all().filter(buyer=user_id)
    # print(f"user={user}, user id={user_id} listings = {bought}")
    return render(request, 'mythrifts/index.html', {'user': user, 'listings': bought})


@login_required
def add_photo(request, listing_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, listing_id=listing_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', listing_id=listing_id)


class ListingCreate(LoginRequiredMixin, CreateView):
    model = Listing
    fields = ['title', 'description', 'price', 'size', 'condition', 'gender', 'isRental', 'date_listed']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ListingDelete(DeleteView, LoginRequiredMixin):
    model = Listing
    fields = ['title', 'description', 'price', 'size', 'condition', 'gender']
    success_url = '/mythrifts/listings/'  # commit test


class ListingUpdate(UpdateView, LoginRequiredMixin):
    model = Listing
    fields = ['title', 'description', 'price', 'size', 'condition', 'gender']
    success_url = '/mythrifts/listings/'  # commit test
