from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('listings/', views.listings_index, name="listings_index"),
    path('listings/<int:listing_id>/', views.listings_detail, name='listings_detail'), #Kateleen - added 'details' path  
    path('mythrifts/', views.mythrifts_home, name="mythrifts_index"),
    path('mythrifts/listings', views.mythrifts_listings, name='mythrifts_listings'),
    path('mythrifts/sold', views.mythrifts_sold, name='mythrifts_sold'),
    path('mythrifts/bought', views.mythrifts_bought,name='mythrifts_bought'),
    path('listings/<int:listing_id>/add_photo/', views.add_photo, name='add_photo'),
    # path('listing/<int:listing_id>/buy'),
    path('listings/create/', views.CreateListing.as_view(), name='create_listing')
]
