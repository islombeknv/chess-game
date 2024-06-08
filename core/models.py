from django.db import models


class PlayerModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    elo_rating = models.IntegerField(verbose_name="elo rating")
    country = models.CharField(max_length=50, verbose_name="country")
    games_played = models.IntegerField(default=0, verbose_name="games played")
    wins = models.IntegerField(default=0, verbose_name="wins")
    losses = models.IntegerField(default=0, verbose_name="losses")
    draws = models.IntegerField(default=0, verbose_name="draws")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "player"
        verbose_name_plural = "players"


class GameModel(models.Model):
    RESULT_CHOICES = [
        ("win", "Win"),
        ("loss", "Loss"),
        ("draw", "Draw"),
    ]
    OPENING_CHOICES = [
        ("Sicilian Defense", "Sicilian Defense"),
        ("Ruy Lopez", "Ruy Lopez"),
    ]

    white_player = models.ForeignKey(
        PlayerModel,
        related_name="white_games",
        on_delete=models.CASCADE,
        verbose_name="white player",
    )
    black_player = models.ForeignKey(
        PlayerModel,
        related_name="black_games",
        on_delete=models.CASCADE,
        verbose_name="black player",
    )
    result = models.CharField(
        max_length=4, choices=RESULT_CHOICES, verbose_name="result"
    )
    opening = models.CharField(
        max_length=50, choices=OPENING_CHOICES, verbose_name="opening"
    )
    number_of_moves = models.IntegerField(verbose_name="number of moves")
    date_played = models.DateField(verbose_name="date played")

    def __str__(self):
        return f"{self.white_player}, {self.black_player}"

    class Meta:
        verbose_name = "game"
        verbose_name_plural = "games"
