from rest_framework import serializers
from .models import Super

class SupersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id','name','alter_ego','primary_ability','secondary_ability','catchphrase', 'super_type']
        depth = 1