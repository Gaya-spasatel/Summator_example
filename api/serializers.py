from rest_framework import serializers


class SummatorSerializer(serializers.Serializer):
    first_operand = serializers.IntegerField()
    second_operand = serializers.IntegerField()
    result = serializers.IntegerField()
    operation = serializers.CharField(max_length=1)
