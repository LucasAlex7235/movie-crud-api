from django.db import models
from accounts.models import Account


class Rating(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True)
    rating = models.CharField(max_length=127, choices=Rating.choices, default=Rating.G)
    synopsis = models.TextField(null=True)
    orders = models.ManyToManyField(
        Account, through="MovieOrder", related_name="movies_ordered"
    )
    user = models.ForeignKey(
        "accounts.account", on_delete=models.CASCADE, related_name="movies_added"
    )
    added_by = models.CharField(max_length=127)

    def __repr__(self) -> str:
        return f"<Account [{self.id}] - {self.title}>"


class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
