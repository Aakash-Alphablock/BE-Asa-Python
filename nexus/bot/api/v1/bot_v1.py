
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from common.authentications import ClerkJWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from common.decorators import validate_request_data
from bot.api.v1 import serializers
from bot.private import BotService
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import permission_classes, authentication_classes

from common.resource import BaseAPIResource

class BotAPIV1(BaseAPIResource):
    authentication_classes = [ClerkJWTAuthentication]
    permission_classes = [IsAuthenticated] #This is to apply authentication to all the methods in the class

    @action(detail=False, methods=['post'], url_path='create-new-bot')
    @validate_request_data(serializer=serializers.CreateNewBotSerializer)
    def create_new_bot(self, request, *args, **kwargs):
        data = kwargs.get('validated_data')
        bot_sevrice = BotService()
        bot_details = bot_sevrice.create_new_bot(**data)
        return self.create_success_response(data=bot_details)

    @action(detail=False, methods=['get'], url_path='get-all-bots')
    @validate_request_data(serializer=serializers.CreateNewBotSerializer)
    def get_all_bots(self, request, *args, **kwargs):
        data = kwargs.get('validated_data')
        bot_sevrice = BotService()
        bot_details = bot_sevrice.get_all_bots(data)
        return self.create_success_response(data=bot_details)

    # @permission_classes([IsAuthenticated])
    # @authentication_classes([ClerkJWTAuthentication])
    @action(detail=False, methods=['get'], url_path='bot-details')
    @validate_request_data(serializer=serializers.GetBotDetailsSerializer)
    def get_bot_details(self, request, *args, **kwargs):
        data = kwargs.get('validated_data')
        bot_sevrice = BotService()
        bot_details = bot_sevrice.get_bot_details(data['bot_id'])
        if not bot_details:
            return self.create_error_response(message='Bot not found')
        return self.create_success_response(data=bot_details)

    @action(detail=False, methods=['get'], url_path='delete-all-bots')
    @validate_request_data(serializer=serializers.CreateNewBotSerializer)
    def delete_all_bots(self, request):
        pass

    @action(detail=False, methods=['get'], url_path='insert-new-url')
    @validate_request_data(serializer=serializers.CreateNewBotSerializer)
    def insert_new_urls(self, request):
        pass