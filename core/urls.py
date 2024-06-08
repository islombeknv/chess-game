from django.urls import path

from core.api.views import ListCreateAPIView, GameModelListCreateAPIView
from core.views import (
    PlayerModelCreateView,
    PlayerModelListView,
    PlayerModelUpdateView,
    PlayerModelDeleteView,
    GameModelListView,
    GameModelCreateView,
    GameModelUpdateView,
    GameModelDeleteView,
)

app_name = "core"

urlpatterns = [
    path("api/v1/players/", ListCreateAPIView.as_view(), name="player-list"),
    path("api/v1/games/", GameModelListCreateAPIView.as_view(), name="game-list"),
    path("api/v1/player/create/", ListCreateAPIView.as_view(), name="player-create"),
    path(
        "api/v1/game/create/", GameModelListCreateAPIView.as_view(), name="game-create"
    ),
]


urlpatterns += [
    path("", PlayerModelListView.as_view(), name="dash-player-list"),
    path(
        "dashboard/player/create/",
        PlayerModelCreateView.as_view(),
        name="dash-player-create",
    ),
    path(
        "dashboard/player/update/<int:pk>/",
        PlayerModelUpdateView.as_view(),
        name="dash-player-update",
    ),
    path(
        "dashboard/player/delete/<int:pk>/",
        PlayerModelDeleteView.as_view(),
        name="dash-player-delete",
    ),  # games starts
    path("dashboard/games/", GameModelListView.as_view(), name="dash-game-list"),
    path(
        "dashboard/game/create/",
        GameModelCreateView.as_view(),
        name="dash-game-create",
    ),
    path(
        "dashboard/game/update/<int:pk>/",
        GameModelUpdateView.as_view(),
        name="dash-game-update",
    ),
    path(
        "dashboard/game/delete/<int:pk>/",
        GameModelDeleteView.as_view(),
        name="dash-game-delete",
    ),
]
