
from django.urls import path, include
from bot import views
from bot.api.v1.bot_v1 import BotAPIV1
from rest_framework.routers import DefaultRouter
from bot.api.v1.bot_v1 import BotAPIV1

router = DefaultRouter()
router.register(r'', BotAPIV1, basename='bot')


urlpatterns = [
    path('', include(router.urls), name='bot')
]
