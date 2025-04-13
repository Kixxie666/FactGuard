from django.http import JsonResponse

class RaspberryPiAccessMiddleware:
    ALLOWED_IPS = ['31.205.137.39', '127.0.0.1']

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR', '')

        if request.path.startswith("/vote") and ip not in self.ALLOWED_IPS:
            return JsonResponse({"error": f"Access restricted: your IP {ip} is not allowed"}, status=403)

        return self.get_response(request)
