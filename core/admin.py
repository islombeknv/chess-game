from django.contrib import admin

from core.models import PlayerModel, GameModel


@admin.register(PlayerModel)
class PlayerModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "elo_rating",
        "country",
        "games_played",
        "wins",
        "losses",
        "draws",
    )
    search_fields = ("name", "country")
    list_filter = ("country",)

    fieldsets = (
        (None, {"fields": ("name", "country")}),
        (
            "Statistics",
            {"fields": ("elo_rating", "games_played", "wins", "losses", "draws")},
        ),
    )


@admin.register(GameModel)
class GameModelAdmin(admin.ModelAdmin):
    list_display = (
        "white_player",
        "black_player",
        "result",
        "opening",
        "number_of_moves",
        "date_played",
    )
    search_fields = ("white_player__name", "black_player__name", "opening")
    list_filter = ("result", "opening", "date_played")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "white_player",
                    "black_player",
                    "result",
                    "opening",
                    "number_of_moves",
                    "date_played",
                )
            },
        ),
    )
