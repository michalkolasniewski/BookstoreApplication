from django.http import HttpResponse
from django.views.generic import ListView
from rest_framework import viewsets


from books.models import Book
from books.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer

    filter_fields = ['title', 'published_date']
    search_fields = ['title', 'published_date']

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse('Unauthorized', status=401)

        return super().destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse('Unauthorized', status=401)
        return super().create(request, *args, **kwargs)


class BookListView(ListView):
    model = Book
    template_name = 'home.html'
    paginate_by = 30
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('id')
        return queryset
