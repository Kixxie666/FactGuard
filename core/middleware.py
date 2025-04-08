from django.http import JsonResponse

class RaspberryPiAccessMiddleware:
    ALLOWED_IPS = ['31.205.137.39']

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR', '')

        if request.path.startswith("/vote/") and ip not in self.ALLOWED_IPS:
            return JsonResponse({"error": "Access restricted to Raspberry Pi users"}, status=403)

        return self.get_response(request)
