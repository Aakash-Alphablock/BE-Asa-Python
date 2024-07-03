from django.urls import path, include
from bot import views
from bot.api.v1.bot_v1 import BotAPIV1

# v1_urls = [
#     path('bot/', BotAPIV1.as_view(), name='bot'),
#     # Add more URL patterns here
# ]

# urlpatterns = [
#     path('v1/', include(v1_urls)),
# ]
