from django.shortcuts import render
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render

from User.models import UserExtended

from django.contrib.auth import (authenticate,
                                 login)

from rest_framework.response import Response

from rest_framework.filters import (SearchFilter,
                                     OrderingFilter)

from rest_framework.status import (HTTP_200_OK, 
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_404_NOT_FOUND,
                                   HTTP_204_NO_CONTENT)

from rest_framework.views import APIView

from rest_framework.generics import (CreateAPIView ,
                                     ListAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateAPIView,
                                     DestroyAPIView)

from LiveData.serializer import (LiveDataUpdateSerializer,
                                 LiveDataListSerializer,
                                 LiveDataDetailSerializer)

from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        IsAuthenticatedOrReadOnly,
                                        IsAdminUser)

from LiveData.permissions import IsOwner

from Device.models import Device

from django.contrib.auth import get_user_model

from LiveData.models import LiveData

from rest_framework.exceptions import APIException

User = get_user_model()         
# Create your views here.

class LiveDataListAPIView(ListAPIView):
    queryset = LiveData.objects.all()
    serializer_class = LiveDataListSerializer

class LiveDataDetailAPIView(RetrieveAPIView):
    queryset = LiveData.objects.all()
    serializer_class = LiveDataDetailSerializer
    permission_classes = [IsAuthenticated]

class LiveDataUpdateAPIView(RetrieveUpdateAPIView):
    queryset = LiveData.objects.all()
    serializer_class = LiveDataDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]

class LiveDataDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = LiveData.objects.all()
    serializer_class = LiveDataDetailSerializer

    def perform_destroy(self, instance):
        instance.device.delete()
        instance.delete()
