from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate


@api_view(['POST'])
def auth_check(request):
    data = request.data
    user = authenticate(username=data['username'], password=data['password'])
    if user is not None:
        return Response({"message": "Successfully Logged in!"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Failed Logged in!"}, status=status.HTTP_403_FORBIDDEN)
