# from rest_framework import serializers
# from . import models


# class QuerySerializer(serializers.ModelSerializer):
#   creator = serializers.ReadOnlyField(source='creator.username')
#   answers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

#   class Meta:
#     model = models.Query
#     fields = ['id', 'department', 'query', 'creator','answers']

  
# class AnswerSerializer(serializers.ModelSerializer):
#   creator = serializers.ReadOnlyField(source='owner.username')

#   class Meta:
#     model = models.Answer
#     fields = ['id', 'query', 'creator','answer']