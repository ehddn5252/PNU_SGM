from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .serializers import userSerializer,strategySerializer,resultSerializer

from .models import User, Strategy, Result

from .rebalancing import test_backtesting
from .rebalancing.test_backtesting_class_collection import Init_data,User_input_data,Stock_trading_indicator,Result

# ================= user crud ======================= 
# ===================================================

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		# user api 예시
		'User List':'/user-list/',
		'User Detail':'/user-detail/<str:pk>/',
		'User Create':'/user-create/',
		'User Update':'/user-update/<str:pk>/',
		'User Delete':'/user-delete/<str:pk>/',
		# strategy api 예시
		'Strategy List':'/strat-list/',
		'Strategy Detail':'/strat-detail/<str:pk>/',
		'Strategy Create':'/strat-create/',
		'Strategy Update':'/strat-update/<str:pk>/',
		'Strategy Delete':'/strat-delete/<str:pk>/',
		# Result api 예시
		'Result List':'/result-list/',
		'Result Detail':'/result-detail/<str:pk>/',
		'(Do not use)Result Create':'/result-create/',
		'(Do not use)Result Update':'/result-update/<str:pk>/',
		'(Do not use)Result Delete':'/result-delete/<str:pk>/',
		}
	test_backtesting.testfunc()
	initData = Init_data()
	userInputData = User_input_data()
	stockTradingIndicator = Stock_trading_indicator()
	result = Result("dongwoo")

	test_backtesting.backtesting(initData,userInputData,stockTradingIndicator,result)
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

@api_view(['GET'])
def strategyList(request):
	strategys = Strategy.objects.all().order_by('-id')
	serializer = strategySerializer(strategys, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def strategyDetail(request, pk):
	strategys = Strategy.objects.get(id=pk)
	serializer = strategySerializer(strategys, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def strategyCreate(request):
	serializer = strategySerializer(data=request.data)
	
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def strategyUpdate(request, pk):
	strategys = Strategy.objects.get(id=pk)
	serializer = strategySerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def strategyDelete(request, pk):
	strategys = Strategy.objects.get(id=pk)
	strategys.delete()

	return Response('strategy succsesfully delete!')
	
# ================= result crud ===================
# =================================================== 

@api_view(['GET'])
def resultList(request):
	results = Result.objects.all().order_by('-id')
	serializer = resultSerializer(results, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def resultDetail(request, pk):
	results = Result.objects.get(id=pk)
	serializer = resultSerializer(results, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def resultCreate(request):
	serializer = resultSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def resultUpdate(request, pk):
	results = Result.objects.get(id=pk)
	serializer = resultSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def resultDelete(request, pk):
	results = Result.objects.get(id=pk)
	results.delete()

	return Response('result succsesfully delete!')