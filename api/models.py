from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Feedback(models.Model):
    rating = models.IntegerField(
        default = 1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    message = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.message