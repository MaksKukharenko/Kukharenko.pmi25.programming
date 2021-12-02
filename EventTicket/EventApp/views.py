from rest_framework.generics import ListCreateAPIView
from EventApp.models import EVENT
from EventApp.serializers import EventSerializer
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView

class EventReadMethods(ListCreateAPIView):
    queryset = EVENT.objects.all()
    serializer_class = EventSerializer

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["id", "Data", "Start", "End", "Price", "Code", "Location"]
# request, pk
class event_detail(APIView):

    def get(self, request, pk):
        try:
            event = EVENT.objects.get(pk=pk)
        except EVENT.DoesNotExist:
            return Response({'message': 'The event does not exist'}, status=status.HTTP_404_NOT_FOUND)
        event_serializer = EventSerializer(event)
        return Response(event_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            event = EVENT.objects.get(pk=pk)
        except EVENT.DoesNotExist:
            return Response({'message': 'The event does not exist'}, status=status.HTTP_404_NOT_FOUND)
        event_data = JSONParser().parse(request)
        event_serializer = EventSerializer(event, data=event_data)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response({"event":event_serializer.data}, status=status.HTTP_200_OK)
        return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            event = EVENT.objects.get(pk=pk)
        except EVENT.DoesNotExist:
            return Response({'message': 'The event does not exist'}, status=status.HTTP_404_NOT_FOUND)
        event.delete()
        return Response({'message': 'event was deleted successfully!'}, status=status.HTTP_200_OK)