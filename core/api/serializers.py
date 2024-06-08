from rest_framework import serializers
from core.models import PlayerModel, GameModel


class PlayerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerModel
        fields = "__all__"


class GameModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameModel
        fields = "__all__"
