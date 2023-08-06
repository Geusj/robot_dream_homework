# Create your views here.
from django.http import JsonResponse

from purchases.models import Purchases


def purchases_view(request):
    purchases = Purchases.objects.all()
    data = list(purchases.values())
    return JsonResponse(data, safe=False)
