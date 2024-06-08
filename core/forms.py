from django import forms

from core.models import PlayerModel, GameModel


class PlayerModelForm(forms.ModelForm):
    class Meta:
        model = PlayerModel
        fields = "__all__"


class GameModelForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = "__all__"
