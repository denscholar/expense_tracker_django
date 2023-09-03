from rest_framework import serializers


class UsernameValidationSerializer(serializers.Serializer):
    username = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "").strip()
        print(username)
        if not username:  # Check if the username is empty after stripping whitespace
            raise serializers.ValidationError("Username cannot be empty")
        return data
