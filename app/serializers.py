from .models import DcHero
from rest_framework import serializers


class DcHeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DcHero
        fields = ['pageId', 'name', 'urlslug', 'identity', 'align','eye','hair','sex','gsm','alive','appearances','firstAppearance','year']
