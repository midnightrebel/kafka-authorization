import json

from django.db.models.signals import post_save
from django.dispatch import receiver
from kafka import KafkaProducer
from rest_framework import status
from rest_framework.response import Response

from .models import User


def send_message(sender, instance, created, **kwargs):
    if created:
        email = instance.user.email
        print(email)
        user = User.objects.filter(email=email).first()
        payload = {
            'email': user.email,
            'username': user.username
        }
        producer = KafkaProducer(bootstrap_servers='localhost:9092', api_version=(3, 20),
                                 )

        serialized_data = json.dumps(payload).encode('utf-8')
        producer.send('Ptopic', serialized_data)
        return Response(serialized_data, status.HTTP_200_OK)


post_save.connect(send_message, sender=User)
