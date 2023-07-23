from django.db import models
from users.models import User


class Books(models.Model):
    title = models.CharField(max_length=100, default="Default Title")
    author = models.CharField(max_length=100, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['title', 'author']  # В Book title та author разом мають бути унікальними.
        db_table = 'books'

    def __str__(self):
        return f"{self.title} - {self.author}"
