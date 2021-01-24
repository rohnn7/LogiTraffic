from django.db.models import Q
from django.shortcuts import render

from User.models import UserExtended

from django.contrib.auth import (authenticate,
                                 login)

from rest_framework.response import Response

from rest_framework.filters import (SearchFilter,
                                     OrderingFilter)

from rest_framework.status import (HTTP_200_OK, 
                                   HTTP_201_CREATED, 
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_404_NOT_FOUND,
                                   HTTP_204_NO_CONTENT)

from rest_framework.views import APIView

from rest_framework.generics import (CreateAPIView ,
                                     ListAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateAPIView,
                                     DestroyAPIView)

from User.serializers import (UserExtendedListSerializer,
                              UserExtendedDetailSerializer,
                              UserExtendedCreateUpdateSerializer,
                              UserCreateSerializer,
                              UserLoginSerializer)

from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        IsAuthenticatedOrReadOnly,
                                        IsAdminUser)

from User.permissions import IsOwner

from django.contrib.auth import get_user_model

User = get_user_model()                               
# Create your views here.

class UserExtendedListAPIView(ListAPIView):
    #queryset = UserExtended.objects.filter(is_active=True)
    serializer_class = UserExtendedListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [ 'UserExtended__user']

    def get_queryset(self, *args, **kwargs):
        queryset_list = UserExtended.objects.filter(is_active=True)
        query = self.request.GET.get('q')
        print(query)
        if query:
            queryset_list = queryset_list.filter(
                Q(first_name__icontains = query)|
                Q(mobile__icontains = query)|
                Q(email__icontains = query)|
                Q(user__icontains = query)
            ).distinct()
        return queryset_list            


class UserExtendedRetrieveAPIView(RetrieveAPIView):
    queryset = UserExtended.objects.all()
    serializer_class = UserExtendedDetailSerializer
    # permission_classes = [IsAuthenticated]        

class UserExtendedUpdateAPIView(RetrieveUpdateAPIView):
    queryset = UserExtended.objects.all()
    serializer_class = UserExtendedCreateUpdateSerializer
    # permission_classes = [IsOwner]

class UserExtendedCreateAPIView(CreateAPIView):
    queryset = UserExtended.objects.all()
    serializer_class = UserExtendedCreateUpdateSerializer    
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class UserExtendedDeleteAPIView(DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = UserExtended.objects.all()
    serializer_class = UserExtendedDetailSerializer

    def perform_destroy(self, instance):
        instance.user.delete()
        instance.delete()


class UserCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    # serializer_class = UserCreateSerializer  

    
    def post(self, request, format=None):
        serializer = UserCreateSerializer (data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({'headers':{'Access-Control-Allow-Headers':'http://localhost:8080',
                }, 'data':serializer.data,} ,status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, format=None): 
        print(request.data)        
        print(request.data['username'])       
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return Response({'username':user.username, 'pk':user.id, 'user': user.user.id})
            return Response(status=HTTP_404_NOT_FOUND)                
        return Response(status=HTTP_400_BAD_REQUEST)  
       

       

    

    
           

