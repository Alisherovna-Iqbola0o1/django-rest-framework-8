from rest_framework import serializers
from .models import Salom1, Salom2, Salom3, Salom4, Salom5

class Salom1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Salom1
        fields = '__all__'

class Salom2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Salom2
        fields = '__all__'

class Salom3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Salom3
        fields = '__all__'

class Salom4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Salom4
        fields = '__all__'

class Salom5Serializer(serializers.ModelSerializer):
    class Meta:
        model = Salom5
        fields = '__all__'