from django.http import JsonResponse

class RaspberryPiAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow all IPs (getting issues with my IP /Port)
        return self.get_response(request)
