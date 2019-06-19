from django.urls import path
from property.views import (
    CreateAndListPropertyView, PropertyDetailView, BuyerPropertyListView)


urlpatterns = [
    path('', CreateAndListPropertyView.as_view(),
         name='create_and_list_property'),
    path('get/<slug:slug>/', PropertyDetailView.as_view(),
         name='single_property'),
    path('buyer-list/', BuyerPropertyListView.as_view(),
         name='get_buyer_list'),
    path('buyer-list/<slug:slug>/', BuyerPropertyListView.as_view(),
         name='modify_buyer_list'),
]