from django.urls import path
from . views import (
    ProductApiListView,
    ProductApiDetailView
)

urlpatterns = [
    path('', ProductApiListView.as_view(), name='Product_List'),
    path('/<int:pk>', ProductApiDetailView.as_view(), name='Product_Detail' )
]