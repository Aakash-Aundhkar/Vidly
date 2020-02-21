from django.db import models
from tastypie.resources import ModelResource
from movies.models import movie
# Create your models here.


class movieresource(ModelResource):
    class Meta:
        queryset = movie.objects.all()
        resource_name = "movies"
