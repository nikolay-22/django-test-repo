from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Profile(models.Model):
    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(  # SHOULD BE AT LEAST 12
        validators=(
            MinValueValidator(12),
        ),
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    profile_picture_url = models.URLField(
        null=True,
        blank=True,
    )


class Game(models.Model):
    TYPE_CHOICE_ACTION = 'action'
    TYPE_CHOICE_ADVENTURE = 'adventure'
    TYPE_CHOICE_PUZZLE = 'puzzle'
    TYPE_CHOICE_STRATEGY = 'strategy'
    TYPE_CHOICE_SPORTS = 'sports'
    TYPE_CHOICE_BOARD_CARD_GAME = 'board_card_game'
    TYPE_CHOICE_OTHER = 'other'
    TYPE_CHOICES = (
        (TYPE_CHOICE_ACTION, 'Action'),
        (TYPE_CHOICE_ADVENTURE, 'Adventure'),
        (TYPE_CHOICE_PUZZLE, 'Puzzle'),
        (TYPE_CHOICE_STRATEGY, 'Strategy'),
        (TYPE_CHOICE_SPORTS, 'Sports'),
        (TYPE_CHOICE_BOARD_CARD_GAME, 'Board/Card Game'),
        (TYPE_CHOICE_OTHER, 'Other'),
    )

    title = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=15,
        choices=TYPE_CHOICES,
        null=False,
        blank=False,
    )

    # MUST BE BETWEEN 0.1 AND 5.0
    rating = models.FloatField(
        validators=(
            MinValueValidator(0.1),
            MaxValueValidator(5),
        ),
        null=False,
        blank=False,
    )

    # MUST BE AT LEAST 1
    max_level = models.FloatField(
        validators=(
            MinValueValidator(1),
        ),
        null=True,
        blank=True,
    )

    game_image_url = models.URLField(
        null=False,
        blank=False,
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )
