# Generated by Django 4.2.6 on 2023-11-28 02:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0002_emotionvector"),
    ]

    operations = [
        migrations.CreateModel(
            name="TrackVibe",
            fields=[
                (
                    "track_id",
                    models.CharField(max_length=250, primary_key=True, serialize=False),
                ),
                ("track_lyrics_vibe", models.CharField(max_length=250, null=True)),
                ("track_audio_vibe", models.CharField(max_length=250, null=True)),
                ("upvote_count", models.IntegerField(default=0)),
                ("downvote_count", models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name="Track",
        ),
    ]
