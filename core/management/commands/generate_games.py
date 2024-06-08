import random
from datetime import timedelta
from tqdm import tqdm
from django.core.management.base import BaseCommand
from django.utils import timezone

from core.models import PlayerModel, GameModel


class Command(BaseCommand):
    help = "Generate realistic chess game records"

    def add_arguments(self, parser):
        parser.add_argument(
            "num_records", type=int, help="The number of game records to generate"
        )

    def handle(self, *args, **kwargs):
        num_records = kwargs["num_records"]

        self.generate_players()
        self.generate_games(num_records)
        self.stdout.write(
            self.style.SUCCESS(f"Successfully generated {num_records} game records")
        )

    @staticmethod
    def generate_players():
        names = ["Alisher", "Bobur", "Jack", "Ruslan", "Odil"]
        countries = ["Uzbekistan", "USA", "China", "Russia"]

        for _ in tqdm(range(10), desc="Generating players"):
            elo_rating = random.randint(2500, 2800)
            name = random.choice(names)
            country = random.choice(countries)
            if not PlayerModel.objects.filter(name=name).exists():
                PlayerModel.objects.create(
                    name=name, elo_rating=elo_rating, country=country
                )

    @staticmethod
    def generate_games(num_records):
        players = list(PlayerModel.objects.all())
        result_choices = ["win", "loss", "draw"]
        opening_choices = ["Sicilian Defense", "Ruy Lopez"]

        for _ in tqdm(range(num_records), desc="Generating games"):
            white_player = random.choice(players)
            black_player = random.choice(players)
            while black_player == white_player:
                black_player = random.choice(players)

            result = random.choice(result_choices)
            opening = random.choice(opening_choices)
            number_of_moves = random.randint(20, 60)
            date_played = timezone.localtime() - timedelta(days=random.randint(0, 365))

            GameModel.objects.create(
                white_player=white_player,
                black_player=black_player,
                result=result,
                opening=opening,
                number_of_moves=number_of_moves,
                date_played=date_played,
            )

            white_player.games_played += 1
            black_player.games_played += 1

            if result == "win":
                white_player.wins += 1
                black_player.losses += 1
            elif result == "loss":
                white_player.losses += 1
                black_player.wins += 1
            elif result == "draw":
                white_player.draws += 1
                black_player.draws += 1

            white_player.save()
            black_player.save()
