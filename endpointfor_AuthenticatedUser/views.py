from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class lockedEndpointView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        return Response({
            'error': False,
            'message': 'You are authenticated?!, Hi!',
        })
