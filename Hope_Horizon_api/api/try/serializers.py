from rest_framework import serializers
from api.models import *
from api.submodels.models_try import *


class TrySerializers(serializers.ModelSerializer):
    # emailz = serializers.CharField(required=False)
    class Meta:
        model = Try 
        fields = '__all__'

    
    def add(self, request):
        try:
            name = self.validated_data['name']
            email = self.validated_data['email']
            message = self.validated_data['message']
            image = self.validated_data['image']

            return Try.objects.create(
                name = name,
                email = email,
                message = message,
                image = image
            )
        except Exception as error:
            print("TrySerializer_add_error: ", error)
            return None


    