from django.db import models
from django.contrib.auth import get_user_model
import uuid


class HouseModel(models.Model):
    STATUS_CHOICE = (
        ("FREE", "FREE"),
        (
            "BAUGHT",
            "BAUGHT",
        ),
    )
    unique_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    area = models.IntegerField()
    floor = models.IntegerField()
    city = models.CharField(max_length=50, db_index=True)
    price = models.FloatField()
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICE, default="FREE", db_index=True
    )
    seller = models.ForeignKey(
        get_user_model(),
        on_delete=models.DO_NOTHING,
        null=False,
        related_name="seller",
    )
    buyer = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name="buyer",
    )

    def __str__(self):
        return f"House {self.unique_id} in {self.city}"
