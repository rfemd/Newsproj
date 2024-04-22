from rest_framework import viewsets
from . import models
from . import serializers


class NewsViewset(viewsets.ModelViewSet):
	queryset = models.News.objects.all()
	serializer_class = serializers.NewsSerializer


#list() retrieve() create() update() destroy()