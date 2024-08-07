from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

class HelloView(ViewSet):
    def list(self, requet):
        return Response({"message": "hello"}, status=status.HTTP_200_OK)
    
#Users
class UsersView(ViewSet):
    def list(self, request):
        # TMP Data
        users = [
            {"id": 1, "username": "awesome_user", "tags": ["Пицца", "Барбершоп", "Животные"]},
            {"id": 2, "username": "super_user", "tags": ["Вино", "Грузинская кухня", "Музей", "Театр"]},
        ]
        return Response(users, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        users = {
            1: {"id": 1, "username": "awesome_user", "tags": ["Пицца", "Барбершоп", "Животные"]},
            2: {"id": 2, "username": "super_user", "tags": ["Вино", "Грузинская кухня", "Музей", "Театр"]},
        }
        user = users.get(int(pk))
        if user:
            return Response(user, status=status.HTTP_200_OK)

        return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

