import json

from kafka import KafkaProducer
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import User
from .serializers import RegistrationSerializer, UserSerializer


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CurrentUserView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [OAuth2Authentication, JWTAuthentication, ]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class ProducerView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [OAuth2Authentication, JWTAuthentication ]

    def get(self, request):
        email = request.user.email
        user = User.objects.filter(email=email).first()
        payload = {
            'email': user.email,
            'username': user.username
        }
        producer = KafkaProducer(bootstrap_servers='localhost:9092', api_version=(3, 20),
                                 )

        serialized_data = json.dumps(payload).encode('utf-8')
        producer.send('Ptopic',  serialized_data)
        return Response(serialized_data,status.HTTP_200_OK)