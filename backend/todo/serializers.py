from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """
    we specified the model to work with and the fields we want to be converted to JSON
    """
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')
