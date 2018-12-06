from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from newsAPI import util


@csrf_exempt
def news_api(request):
    return JsonResponse(util.get_news())