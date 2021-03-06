# Generated by Django 4.0.4 on 2022-04-19 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('category', models.CharField(choices=[('action', 'Action'), ('adventure', 'Adventure'), ('puzzle', 'Puzzle'), ('strategy', 'Strategy'), ('sports', 'Sports'), ('board_card_game', 'Board/Card Game'), ('other', 'Other')], max_length=15)),
                ('rating', models.FloatField()),
                ('max_level', models.FloatField(blank=True, null=True)),
                ('game_image_url', models.URLField()),
                ('summary', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('profile_picture_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
