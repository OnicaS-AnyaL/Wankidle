# Generated by Django 4.2.13 on 2024-05-19 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_database_feat_or_not_database_game_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='database',
            name='game_or_not',
            field=models.BooleanField(default=True),
        ),
    ]
