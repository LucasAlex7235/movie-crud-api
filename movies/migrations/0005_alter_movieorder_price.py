# Generated by Django 4.1.6 on 2023-02-17 01:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0004_movie_user_alter_movie_added_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movieorder",
            name="price",
            field=models.DecimalField(decimal_places=4, max_digits=8),
        ),
    ]
