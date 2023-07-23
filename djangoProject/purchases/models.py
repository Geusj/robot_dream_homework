from django.db import models
from users.models import User


class Purchases(models.Model):
    price = models.IntegerField(null=False)
    date_of_purchase = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'purchases'
        ordering = ['-date_of_purchase']  # порядок сортування на сортування за датою у порядку спадання.

    def __str__(self):
        return f"Purchase of {self.price} by {self.user} on {self.date_of_purchase}"
