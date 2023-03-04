from django.http import JsonResponse
from .models import temptdata
from .serializer import temptdataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET", "POST"])
def temptdata_list(request):

    if request.method == "GET":
        temptdata = temptdata.objects.all()
        serializer = temptdataSerializer(temptdata, many=True)
        return JsonResponse(serializer.data)

    if request.method == "POST":
        serializer = temptdataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
