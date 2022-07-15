import json

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from kafka import KafkaProducer
from rest_framework import status
from rest_framework.response import Response

from autorize import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def send_message(instance, **kwargs):
    while True:
        email = instance.email

        payload = {
            'email': instance.email,
            'username': instance.username,
            'password': instance.password
        }
        print("Init.")
        print(payload)
        producer = KafkaProducer(bootstrap_servers='localhost:9092', api_version=(3, 20))
        serialized_data = json.dumps(payload).encode('utf-8')
        producer.send('Ptopic', serialized_data)
        producer.flush()
        return Response(status.HTTP_200_OK)
