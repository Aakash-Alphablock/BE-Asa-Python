from common.models import BaseModel
from django.db import models

class Bot(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    token = models.CharField(max_length=255)
    user_id = models.PositiveBigIntegerField()
    is_demo_bot = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'token': self.token,
            'user_id': self.user_id,
            'is_demo_bot': self.is_demo_bot,
            'is_deleted': self.is_deleted
        }
