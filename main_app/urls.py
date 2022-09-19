from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  
    path('accounts/signup/', views.signup, name='signup'),
    path('listings/', views.listings_index, name = "listings_index"),  # Kyle
    # path('listing/<int:listing_id>/',),  # Kateleen
    # path('listing/<int:listing_id>/buy'),
    # path('listing/create/'),  # Venessa
    # path('listing/<int:listing_id>/add_photo/'),  # Venessa
    # path('users/<int:user_id>/listings'),  # Randolph
    # # still to be figured out
    # path('users/<int:user_id>/listings/<int:listing_id>/update'),  # Randolph
]
