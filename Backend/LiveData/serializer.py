from rest_framework.serializers import (ModelSerializer,
                                         CharField,
                                         HyperlinkedIdentityField,
                                         SerializerMethodField,
                                         ValidationError)

from User.models import UserExtended

from LiveData.models import LiveData

from django.contrib.auth import get_user_model


class LiveDataUpdateSerializer(ModelSerializer):
    class Meta:
        model = LiveData
        fields = [
            'speed',
            'longitude',
            'latitude',
            'live_image'
        ]


class LiveDataDetailSerializer(ModelSerializer):
    delete_url = HyperlinkedIdentityField(view_name='livedata:delete', lookup_field = 'pk')
    edit_url = HyperlinkedIdentityField(view_name='livedata:update', lookup_field = 'pk')
    username_owner = SerializerMethodField()
    class Meta:
        model = LiveData
        fields = [
            'pk',
            'device',
            'speed',
            'logitude',
            'latitude',
            'live_image',
            'delete_url',
            'edit_url',
            'username_owner'  
        ]        

    def get_username_owner(self, obj):
        return str(obj.device.owner.username)    

class LiveDataListSerializer(ModelSerializer):
    detail_url = HyperlinkedIdentityField(view_name='livedata:detail', lookup_field = 'pk')
    class Meta:
        model = LiveData
        fields = [
            'pk',
            'device',
            'detail_url'
        ]


class LiveDataSerializer(ModelSerializer):
    class Meta:
        model = LiveData
        fields = [
            'pk',
            'device',
            'speed',
            'logitude',
            'latitude',
            'live_image',  
        ]        
