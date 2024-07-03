from user import models

def get_user_by_email(email):
    try:
        user = models.UserProfile.objects.get(email=email)
        return user
    except models.UserProfile.DoesNotExist:
        return None
    

def get_user_by_id(user_id):
    try:
        user = models.UserProfile.objects.get(id=user_id)
        return user
    except models.UserProfile.DoesNotExist:
        return None
    
def get_user_by_clerk_user_id(clerk_user_id):
    try:
        user = models.UserProfile.objects.get(clerk_user_id=clerk_user_id)
        return user
    except models.UserProfile.DoesNotExist:
        return None