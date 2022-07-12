from .models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from views import ProducerView

@receiver(post_save, sender=User)
def send_message(sender, instance, created,  **kwargs):
    pass