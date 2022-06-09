from wsgiref.util import request_uri
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

class ApiRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'dummy_opennotes': reverse('dummy-opennotes-list', request=request, format=format),
            'authenticated_endpoint': reverse('lockedEndpoint', request=request, format=format),
            'token': '-----------',
            'token_obtain_pair': reverse('tokens:obtain_pair', request=request, format=format),
            'token_refresh': reverse('tokens:refresh', request=request, format=format),
            'token_verify': reverse('tokens:verify', request=request, format=format),
            'user': '-----------',
            'user_register': reverse('user:register', request=request, format=format),
            'user_reset': reverse('user:reset', request=request, format=format),
            'user_verify': reverse('user:verify', request=request, format=format),
        })
