from django.db import models

NATINALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
    ('LEBANON', 'Líbano'),
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATINALITY_CHOICES,
        blank=True,
        null=True,
    )


    def __str__(self):
        return self.name
    