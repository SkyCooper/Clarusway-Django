from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Category, Blog
from .serializers import CategorySerializer, BlogSerializer
from .permissions import IsAdminOrReadOnly


class CategoryView(ModelViewSet):  # crud
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ['name']


class BlogView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # filterset_fields = ['category__name'] # CATEGORY NAME İNE GÖRE FİLTRELEME YAPMAK İÇİN
    filterset_fields = ['category']
    search_fields = ['title', 'content']
