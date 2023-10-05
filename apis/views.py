from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, BasePermission, SAFE_METHODS
from products.models import Product
from .custom_permission import IsAuthorOrReadOnly
from .serializers import ProductSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404


# Create your views here.
class PostUserWritePermission(BasePermission):
    """This class is responsible for checking the author to avoid from others users to perform some methods"""
    message = "Editing posts is restricted to the author only."

    def has_object_permission(self, request, view, obj):
        # Check if the request method is in SAFE_METHODS
        if request.method in SAFE_METHODS:
            return True

        else:
            # We will be matching the object author to the request user
            return obj.author == request.user


class ProductApiListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(status='published')
        return queryset


class ProductApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = ProductSerializer

    def get_object(self):
        queryset = Product.objects.filter(status='published')
        object = get_object_or_404(queryset, id=self.kwargs.get("pk"))
        return object
