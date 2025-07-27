# accounts/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import UserData
from django.views.decorators.csrf import csrf_exempt
from .serializers import LoginDataSerializer
from django.shortcuts import HttpResponse

@api_view(['POST'])
def login_view(request):
    serializer = LoginDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Login data saved!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def app_view(request):
    return HttpResponse("App is running!")

@csrf_exempt
def get_user_data(request):
    if request.method == 'GET':
        users = UserData.objects.all().values()  # convert to dictionary
        return JsonResponse(list(users), safe=False)