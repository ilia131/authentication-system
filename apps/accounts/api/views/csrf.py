from django.middleware.csrf import get_token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


@method_decorator(ensure_csrf_cookie, name="dispatch")
class CSRFTokenAPIView(APIView):

    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            "success": True,
            "csrfToken": get_token(request),
        })