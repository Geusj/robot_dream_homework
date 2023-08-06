from django.http import HttpResponse, JsonResponse
from users.models import User


def users_view(request):
    users = User.objects.all()
    data = list(users.values())
    return JsonResponse(data, safe=False)
