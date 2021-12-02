from rest_framework import serializers
from EventApp.models import EVENT


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EVENT
        fields = '__all__'
        read_only_fields = ('id',)

    def validate(self, values):
        if values["Start"] > values["End"]:
            raise serializers.ValidationError("Start can`t be later than End")
        else:
            return values
