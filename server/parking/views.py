from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
import parking.serializers as ser
import parking.models as mod
import json
# Create your views here.


class ParkingViewSet(viewsets.ModelViewSet):
    serializer_class = ser.ParkingSerializer
    queryset = mod.Parking.objects.all()

class ParkingPlaceViewSet(viewsets.ModelViewSet):
    serializer_class = ser.ParkingPlaceSerializer
    queryset = mod.ParkingPlace.objects.all()

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ser.ClientSerializer
    queryset = mod.Client.objects.all()

    @action(methods=["GET"], detail=False)
    def login(self, request, login, password):
        try:
           us =  mod.Client.objects.get(login=login)
        except:
            return Response("Нет пользователя с таким логином", 
                            status=status.HTTP_404_NOT_FOUND)
        if us.password != password:
            return Response("Неверный пароль",  status=status.HTTP_400_BAD_REQUEST)
        res = ser.ClientSerializer(us)
        return Response(res.data, status=status.HTTP_200_OK)
    
    @action(methods=["POST"], detail=False)
    def register(self, request, login, password):
        try:
           user = ser.ClientSerializer(data=request.body)
        except:
            return Response("Некорректный body запроса", 
                            status=status.HTTP_400_BAD_REQUEST)
        if mod.Client.objects.contains(login = login):
            return Response("Пользователь с таким логином существует", 
                            status=status.HTTP_400_BAD_REQUEST)
        mod.Client(name = user.name, 
                     login=login, password=password).save()
        return Response(status=status.HTTP_201_CREATED)

class TariffViewSet(viewsets.ModelViewSet):
    serializer_class = ser.TarifSefializer
    queryset = mod.Tariff.objects.all()

class AutoViewSet(viewsets.ModelViewSet):
    serializer_class = ser.AutoSerializer
    queryset = mod.Auto.objects.all()

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = ser.EmployeeSerializer
    queryset = mod.Employee.objects.all()

    @action(methods=["GET"], detail=False)
    def login(self, request, login, password):
        try:
           us =  mod.Employee.objects.get(login=login)
        except:
            return Response("Нет пользователя с таким логином", 
                            status=status.HTTP_404_NOT_FOUND)
        if us.password != password:
            return Response("Неверный пароль",  status=status.HTTP_400_BAD_REQUEST)
        res = ser.EmployeeSerializer(us)
        return Response(res.data, status=status.HTTP_200_OK)
    
    @action(methods=["POST"], detail=False)
    def register(self, request, login, password):
        try:
           user = ser.EmployeeSerializer(data=request.body)
        except:
            return Response("Некорректный body запроса", 
                            status=status.HTTP_400_BAD_REQUEST)
        if mod.Employee.objects.contains(login = login):
            return Response("Пользователь с таким логином существует", 
                            status=status.HTTP_400_BAD_REQUEST)
        mod.Employee(name = user.name, parking = user.parking, 
                     login=login, password=password).save()
        return Response(status=status.HTTP_201_CREATED)