from rest_framework import serializers
from .models import temptdata

class temptdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = temptdata
        fields = ["rollnum_1", "rollnum_2", "name_1", "name_2", "in_time"]
     
     
     
