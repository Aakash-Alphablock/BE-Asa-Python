from rest_framework.viewsets import ViewSet
from common.responses import BaseResponseMixin

class BaseAPIResource(ViewSet, BaseResponseMixin):
    pass