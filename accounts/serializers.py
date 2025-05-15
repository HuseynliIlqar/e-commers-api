from django_filters.conf import settings
from jwt.utils import force_bytes
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from baskets.models import Basket
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import BadHeaderError
from smtplib import SMTPException


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    password_2 = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password_2']:
            raise serializers.ValidationError({
                'password_2': 'Parollar eyni olmalıdır.'
            })
        return attrs

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Bu istifadəçi adı artıq mövcuddur.")
        return value

    def create(self, validated_data):

        validated_data.pop('password_2')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.is_active = False
        user.save()

        Basket.objects.create(user=user)

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        activation_link = f"http://127.0.0.1:8000/accounts/activate/{uid}/{token}/"

        try:
            send_mail(
                subject="Hesab aktivləşdirmə linki",
                message=f"Aktivləşdirmə üçün bu linkə daxil olun: {activation_link}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,  # mail göndərilməsə Exception atsın
            )
        except (BadHeaderError, SMTPException, Exception) as e:
            user.delete()  # mail göndərilmədisə istifadəçini sil
            raise serializers.ValidationError("Email göndərilə bilmədi. Zəhmət olmasa düzgün email yazın.")

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("İstifadəçi adı və ya parol yanlışdır.")

        if not user.is_active:
            raise serializers.ValidationError("Hesab aktiv deyil. Zəhmət olmasa emailinizi təsdiqləyin.")

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError("İstifadəçi adı və ya parol yanlışdır.")

        refresh = RefreshToken.for_user(user)
        attrs['user'] = user
        attrs['token'] = str(refresh.access_token)
        attrs['refresh_token'] = str(refresh)
        return attrs

class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, attrs):
        refresh_token = attrs.get('refresh_token')

        if not refresh_token:
            raise serializers.ValidationError("Refresh token is required.")

        return attrs

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    new_password_confirm = serializers.CharField(write_only=True)

    def validate(self, data):
        user = self.context.get('request').user
        old_password = data.get('old_password')

        if not user.check_password(old_password):
            raise serializers.ValidationError({"old_password": "Köhnə parol düzgün deyil."})

        new_password = data.get('new_password')
        new_password_confirm = data.get('new_password_confirm')
        if new_password != new_password_confirm:
            raise serializers.ValidationError({"new_password_confirm": "Yeni parol və təkrar eyni olmalıdır."})

        if len(new_password) < 8:
            raise serializers.ValidationError({"new_password": "Yeni parol ən azı 8 simvoldan ibarət olmalıdır."})

        return data