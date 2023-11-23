from django.db import models
import uuid

# Create your models here.


class HouseModel(models.Model):
    STATUS_CHOICE = (
        ("FREE", "FREE"),
        (
            "BAUGHT",
            "BAUGHT",
        ),
    )
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    area = models.IntegerField()
    floor = models.IntegerField()
    city = models.CharField(max_length=150)
    price = models.FloatField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICE)
