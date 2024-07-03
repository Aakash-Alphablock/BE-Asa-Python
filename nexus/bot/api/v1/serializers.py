from rest_framework import serializers

class CreateNewBotSerializer(serializers.Serializer):
    # Define the fields required for creating a new bot
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=255)
    token = serializers.CharField(max_length=35) # token length later to be changed
    user_id = serializers.IntegerField()
    is_demo_bot = serializers.BooleanField()

    def validate(self, data):
        # Validate the data
        # validate method validates the object level post validation checks
        if len(data['name']) < 3:
            raise serializers.ValidationError('Name must be at least 3 characters long')
        return data
    
    def validate_name(self, value):
        # Validate the name
        # validate_field_name validates the feild level post validation checks
        if value == 'admin':
            raise serializers.ValidationError('Name cannot be admin')
        return value

class GetBotDetailsSerializer(serializers.Serializer):
    # Define the fields for getting bot details
    bot_id = serializers.IntegerField()

class InsertNewUrlSerializer(serializers.Serializer):
    # Define the fields for inserting a new URL
    bot_id = serializers.IntegerField()
    url = serializers.URLField()