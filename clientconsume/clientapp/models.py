from django.db import models


class Message(models.Model):
    content = models.BinaryField(max_length=255)

# Create your models here.
