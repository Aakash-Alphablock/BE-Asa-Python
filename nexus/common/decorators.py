from functools import wraps
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

def validate_request_data(serializer: serializers.Serializer):
  """
  Decorator to validate request data against a DRF serializer.
  """
  
  @wraps(serializer)
  def decorator(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
      # Get data based on request content type
      if request.content_type:
        if request.content_type.startswith('application/json'):
          data = request.data
        elif request.method in ('POST', 'PUT', 'PATCH'):
          # Handle form data or custom content types (modify as needed)
          data = request.POST.dict()
        else:
          data = request.GET.dict()
      else:
        data = {}
      
      # Validate data using serializer
      val_serializer = serializer(data=data)
      if not val_serializer.is_valid():
        return Response(val_serializer.errors, status=HTTP_400_BAD_REQUEST)
      
      validated_data = val_serializer.validated_data
      
      # Call view function with validated data
      response = func(self, request, *args, validated_data=validated_data, **kwargs)
      return response
    
    return wrapper
  
  return decorator