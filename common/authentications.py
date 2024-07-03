import jwt


from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from user import public as user_public
from django.conf import settings

class ClerkJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')
        if not token or not token.startswith('Bearer '):
            return None

        token = token.split(' ')[1]

        try:
            # Decode the JWT token
            secret_key = settings.CLERT_JWT_SECRET_KEY
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            clerk_user_id = payload.get('sub')  # Assuming 'sub' contains the Clerk user ID
            # You can extract other information like email, roles, etc., from the JWT payload if needed
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT token has expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid JWT token')
        else:
            return (self.get_user(clerk_user_id), None)
        
    def get_user(self, clerk_user_id):
        return user_public.get_user_by_clerk_user_id(clerk_user_id)