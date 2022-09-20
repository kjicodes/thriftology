from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('listings/', views.listings_index, name="listings_index"),
    path('listings/<int:listing_id>/', views.listings_detail,name='listings_detail'),  # Kateleen - added 'details' path
    path('listings/create/', views.ListingCreate.as_view(), name='create'),
    path('mythrifts/', views.mythrifts_home, name="mythrifts_index"),
    path('mythrifts/listings/', views.mythrifts_listings, name='mythrifts_listings'),
    path('mythrifts/sold/', views.mythrifts_sold, name='mythrifts_sold'),
    path('mythrifts/bought/', views.mythrifts_bought, name='mythrifts_bought'),
    path('listings/<int:listing_id>/add_photo/', views.add_photo, name='add_photo'),
    path('mythrifts/listings/<int:pk>/delete', views.ListingDelete.as_view(), name='listing_delete'),
    path('mythrifts/listings/<int:pk>/update/', views.ListingUpdate.as_view(), name='listing_update'),
    path('listing/<int:listing_id>/buy', views.buy_listing, name='buy_listing') # BUY listing 
]
