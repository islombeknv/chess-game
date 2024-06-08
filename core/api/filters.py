import django_filters
from core.models import PlayerModel, GameModel


class PlayerModelFilter(django_filters.FilterSet):
    elo_rating_min = django_filters.NumberFilter(
        field_name="elo_rating", lookup_expr="gte"
    )
    elo_rating_max = django_filters.NumberFilter(
        field_name="elo_rating", lookup_expr="lte"
    )
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    country = django_filters.CharFilter(field_name="country", lookup_expr="icontains")

    class Meta:
        model = PlayerModel
        fields = ["name", "elo_rating_min", "elo_rating_max", "country"]


class GameModelFilter(django_filters.FilterSet):
    date_played_start = django_filters.DateFilter(
        field_name="date_played", lookup_expr="gte"
    )
    date_played_end = django_filters.DateFilter(
        field_name="date_played", lookup_expr="lte"
    )
    result = django_filters.CharFilter(field_name="result")
    opening = django_filters.CharFilter(field_name="opening", lookup_expr="icontains")
    white_player_name = django_filters.CharFilter(
        field_name="white_player__name", lookup_expr="icontains"
    )
    black_player_name = django_filters.CharFilter(
        field_name="black_player__name", lookup_expr="icontains"
    )

    class Meta:
        model = GameModel
        fields = [
            "result",
            "opening",
            "date_played_start",
            "date_played_end",
            "white_player_name",
            "black_player_name",
        ]
