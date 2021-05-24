from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import *


class CurrencySerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        obj = Currency.objects.create(**validated_data)
        return obj

    class Meta:
        model = Currency

        fields = (
            'name',
            'code',
            'symbol',
            'rate',
            'created_at',
            'updated_at',
            'deleted_at',
        )


class CategorySerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        obj = Category.objects.create(**validated_data)
        return obj

    class Meta:
        model = Category

        fields = (
            'title',
            'user',
            'code',
            'created_at',
            'updated_at',
            'deleted_at',
        )


class AccountSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        obj = Account.objects.create(**validated_data)
        return obj

    class Meta:
        model = Account

        fields = (
            'title',
            'code',
            'currency',
            'balance',
            'created_at',
            'updated_at',
            'deleted_at',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=Account.objects.all(),
                fields=['code']
            )
        ]


class TransactionSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        obj = Transaction.objects.create(**validated_data)
        return obj

    class Meta:
        model = Transaction

        fields = (
            'title',
            'description',
            'currency',
            'category',
            'total',
            'created_at',
            'updated_at',
            'deleted_at',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=Transaction.objects.all(),
                fields=['code']
            )
        ]


class ProfileSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        obj = Profile.objects.create(**validated_data)
        return obj

    class Meta:
        model = Profile

        fields = (
            'user',
            'accounts',
            'created_at',
            'updated_at',
            'deleted_at',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=Profile.objects.all(),
                fields=['code']
            )
        ]
