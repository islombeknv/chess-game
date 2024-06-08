from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient
from core.models import PlayerModel, GameModel
from core.api.serializers import PlayerModelSerializer, GameModelSerializer


class PlayerModelListAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.player1 = PlayerModel.objects.create(
            name="Ali", elo_rating=1500, country="USA"
        )
        self.player2 = PlayerModel.objects.create(
            name="Odil", elo_rating=1600, country="Uzbekistan"
        )
        self.player3 = PlayerModel.objects.create(
            name="Jack", elo_rating=1700, country="Russia"
        )
        self.players = PlayerModel.objects.order_by("-pk")

    def test_list_players(self):
        url = reverse("core:player-list")
        response = self.client.get(url)
        serializer = PlayerModelSerializer(self.players, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_players_by_name(self):
        url = reverse("core:player-list")
        response = self.client.get(url, {"name": "Ali"})
        players = self.players.filter(name__icontains="Ali")
        serializer = PlayerModelSerializer(players, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_players_by_elo_rating(self):
        url = reverse("core:player-list")
        response = self.client.get(url, {"elo_rating_min": 1600})
        players = self.players.filter(elo_rating__gte=1600)
        serializer = PlayerModelSerializer(players, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_players_by_country(self):
        url = reverse("core:player-list")
        response = self.client.get(url, {"country": "Uzbekistan"})
        players = self.players.filter(country__icontains="Uzbekistan")
        serializer = PlayerModelSerializer(players, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class GameModelListAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.player1 = PlayerModel.objects.create(
            name="Ali", elo_rating=1500, country="USA"
        )
        self.player2 = PlayerModel.objects.create(
            name="Odil", elo_rating=1600, country="Uzbekistan"
        )
        self.game1 = GameModel.objects.create(
            white_player=self.player1,
            black_player=self.player2,
            result="win",
            opening="Sicilian Defense",
            number_of_moves=30,
            date_played=timezone.localtime(),
        )
        self.game2 = GameModel.objects.create(
            white_player=self.player2,
            black_player=self.player1,
            result="loss",
            opening="Ruy Lopez",
            number_of_moves=25,
            date_played=timezone.localtime(),
        )
        self.games = GameModel.objects.order_by("-date_played")

    def test_list_games(self):
        url = reverse("core:game-list")
        response = self.client.get(url)
        games = GameModel.objects.order_by("-date_played")
        serializer = GameModelSerializer(games, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_games_by_result(self):
        url = reverse("core:game-list")
        response = self.client.get(url, {"result": "win"})
        games = self.games.filter(result="win")
        serializer = GameModelSerializer(games, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_games_by_date(self):
        url = reverse("core:game-list")
        response = self.client.get(
            url, {"date_played_start": "2024-01-01", "date_played_end": "2024-12-31"}
        )
        games = self.games.filter(
            date_played__gte="2024-01-01", date_played__lte="2024-12-31"
        )
        serializer = GameModelSerializer(games, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_games_by_opening(self):
        url = reverse("core:game-list")
        response = self.client.get(url, {"opening": "Sicilian Defense"})
        games = self.games.filter(opening__icontains="Sicilian Defense")
        serializer = GameModelSerializer(games, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_games_by_players(self):
        url = reverse("core:game-list")
        response = self.client.get(
            url, {"white_player_name": "Odil", "black_player_name": "Jack"}
        )
        games = self.games.filter(
            white_player__name__icontains="Odil",
            black_player__name__icontains="Jack",
        )
        serializer = GameModelSerializer(games, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
