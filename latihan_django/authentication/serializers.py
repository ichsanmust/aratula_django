from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import Users
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #     required=True,
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    # )

    # username = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Users.objects.all())]
    )
    fullname = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    retypePassword = serializers.CharField(write_only=True, required=True)

    class Meta:
        # model = User
        model = Users
        # fields = ('username', 'password', 'retypePassword', 'email', 'first_name', 'last_name')
        fields = ('username', 'password', 'retypePassword', 'fullname')

    def validate(self, attrs):
        if attrs['password'] != attrs['retypePassword']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        del validated_data['retypePassword']
        # user = User.objects.create(**validated_data)
        user = Users.objects.create(**validated_data)

        # user.set_password(validated_data['password'])
        user.password = make_password(validated_data['password'])
        user.save()

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            # user = authenticate(username=username, password=password)
            user = Users.objects.get(username=username)
            if user is None:
                raise serializers.ValidationError("Tidak ada User yang active.")
            
            if check_password(password, user.password):
                  data['user'] = user
            else :
                raise serializers.ValidationError("Paassword Salah.")
        else:
            raise serializers.ValidationError("Username dan password harus diisi.")

        data['user'] = user
        return data