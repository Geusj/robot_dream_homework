# Create your views here.
from django.http import JsonResponse

from books.models import Books


def books_view(request):
    books = Books.objects.all()
    data = list(books.values())
    return JsonResponse(data, safe=False)
