from rest_framework.serializers import ModelSerializer
from . models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'user_name', 'first_name', 'password']
        extra_kwargs = {
            # Setting the password to read-only and hide it from request, we can see it in action when using postman
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        """
        set_password() method is responsible for hashing password.
        """
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
