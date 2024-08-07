from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

class HelloView(ViewSet):
    def list(self, requet):
        return Response({"message": "hello"}, status=status.HTTP_200_OK)

