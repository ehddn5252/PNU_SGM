from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .serializers import userSerializer

from .models import User

# ================= user crud ======================= 
# ===================================================
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		# api 예시
		'      User apis     ':'',
		'User List':'/user-list/',
		'User Detail':'/user-detail/<str:pk>/',
		'User Create':'/user-create/',
		'User Update':'/user-update/<str:pk>/',
		'User Delete':'/user-delete/<str:pk>/',
		}
	return Response(api_urls)


@api_view(['GET'])
def userList(request):
	users = User.objects.all().order_by('-id')
	serializer = userSerializer(users, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def userDetail(request, pk):
	user = User.objects.get(id=pk)
	serializer = userSerializer(user, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def userCreate(request):
	serializer = userSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def userUpdate(request, pk):
	user = User.objects.get(id=pk)
	serializer = userSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def userDelete(request, pk):
	user = User.objects.get(id=pk)
	user.delete()

	return Response('user succsesfully delete!')


# ================= stretagy crud ===================
# =================================================== 