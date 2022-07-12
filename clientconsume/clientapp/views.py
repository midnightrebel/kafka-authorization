from rest_framework import generics
from kafka import KafkaConsumer, TopicPartition
from .serializers import MessageSerializer
from rest_framework import status
import pickle
from rest_framework.response import Response


class ConsumerView(generics.GenericAPIView):
    serializer_class = MessageSerializer

    def get(self, request):
        payload = ''
        consumer = KafkaConsumer('Ptopic',
                                 bootstrap_servers=['localhost:9092'],
                                 api_version=(3, 20)
                                 )
        print(consumer.subscription())
        consumer.poll()
        if consumer.bootstrap_connected():
            print ("Yes")
            for message in consumer:
                print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                     message.offset, message.key,message.value))
        else:
            print('No')
        return Response(payload, status.HTTP_200_OK)


