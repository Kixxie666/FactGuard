from django.http import JsonResponse

class RaspberryPiAccessMiddleware:
    ALLOWED_IPS = ['xxx.x.x.xxx']  #RasPi IP

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/vote/") and request.META['REMOTE_ADDR'] not in self.ALLOWED_IPS:
            return JsonResponse({"error": "Access restricted to Raspberry Pi users"}, status=403)
        return self.get_response(request)
