from rest_framework.serializers import (ModelSerializer,
                                         CharField,
                                         HyperlinkedIdentityField,
                                         SerializerMethodField,
                                         ValidationError)

from User.models import UserExtended

from Device.serializers import DeviceSerializer

from Device.models import Device

from rest_framework.response import Response

from django.contrib.auth import get_user_model
User = get_user_model() 

from django.contrib.auth import (authenticate,
                                 login)

class UserCreateSerializer(ModelSerializer):
    username = CharField
    class Meta:
        model = User
        fields=[
            'username',
            'password'
        ]
        extra_kwargs = {"password":
                                {
                                    "write_only":True
                                }
        }

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user_obj = User.objects.create_user(
            username=username,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

class UserLoginSerializer(ModelSerializer):
    username = CharField
    class Meta:
        model = User
        fields=[
            'username',
            'password'
        ]
        extra_kwargs = {"password":{"write_only":True}}

    # def validate(self, validated_data):
    #     username = validated_data['username']
    #     password = validated_data['password']
    #     user = authenticate(username=username, password=password)
    #     if user is None:
    #         raise ValidationError(
    #             'A user with this username and password is not found.'
    #         )

                    
    #     data =  {
    #         "user": user,
    #         "username": user.username,
    #         "pk": user.id 
    #     }   
    #     print(data)
    #     return data         
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # user = authenticate(username=username, password=password)

        # if user is not None:
        #     if user.is_active:
        #         login(request, user)
        #         return Response({'username':user.username, 'pk':user.id})
        #     return Response(status=HTTP_404_NOT_FOUND)                
        # return Response(status=HTTP_400_BAD_REQUEST)   

class UserExtendedCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = UserExtended
        fields = [
            'email',
            'first_name',
            'last_name',
            'mobile',   
            'user_image'
        ]



class UserExtendedListSerializer(ModelSerializer):
    detail_url = HyperlinkedIdentityField(view_name='user:detail', lookup_field='pk')
    class Meta:
        model = UserExtended
        fields = [
            'pk',
            'user',
            'email',            
            'first_name',
            'last_name',
            'mobile',
            'detail_url'
        ]


class UserExtendedDetailSerializer(ModelSerializer):
    edit_url = HyperlinkedIdentityField(view_name='user:update', lookup_field='pk')
    delete_url = HyperlinkedIdentityField(view_name='user:delete', lookup_field='pk')
    username = SerializerMethodField()
    user_image = SerializerMethodField()
    devices = SerializerMethodField() 
    class Meta:
        model = UserExtended
        fields = [
            'pk',
            'first_name',
            'last_name',
            'email',
            'mobile',            
            'is_active',
            'user_image',
            'edit_url',
            'delete_url',
            'user',
            'username',
            'devices'
        ]        

    def get_username(self, obj):
        return str(obj.user.username)        

    def get_user_image(self, obj):
        return obj.user_image.url

    def get_devices(self, obj):
        d_qs = Device.objects.filter(owner = obj.user)
        devices = DeviceSerializer(d_qs, many = True).data
        return devices 