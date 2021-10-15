from rest_framework import viewsets, exceptions

from books.models import Book
from books.serializers import BookSerializer, DetailBookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
    detail_serializer_class = DetailBookSerializer

    filter_fields = ['id', 'title']

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return self.detail_serializer_class
    #     else:
    #         return self.serializer_class

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = self.detail_serializer_class
        return super().retrieve(request, *args, **kwargs)

