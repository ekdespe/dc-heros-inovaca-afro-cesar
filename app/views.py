from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from django.core.paginator import Paginator
from django.http import HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from .serializers import DcHeroSerializer
from config import settings as st

from app.models import DcHero


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def dc_hero_list_by_50(request):
    """
    Parameters
         ----------
            ❚ Required: none
    Return
    The  list of 50 heros from dc universe

    """
    st.log("Listing all hero")
    try:    
        heros = DcHero.objects.all()
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(heros, request)
        serializer = DcHeroSerializer(result_page, many=True)
    except:
        st.error(f"Error at listing all hero:{heros.errors}")
        return JsonResponse(heros.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def dc_hero_details(request,hero):
    """
     Parameters
         ----------
            ❚ Required: pageID
    Return
    The  hero by pageID if exists

    """
    st.log("Showing details hero")

    try:
        hero = DcHero.objects.get(pageId=hero)
    except DcHero.DoesNotExist:
        return JsonResponse({'message': 'Nao existe heroi com esse id'}, status=status.HTTP_404_NOT_FOUND)
    hero_serialized = DcHeroSerializer(hero,many=False)

    return Response(hero_serialized.data)

@api_view(['POST' ])
@renderer_classes([JSONRenderer])
def dc_hero_create(request):
    """

     Parameters
         ----------
            ❚ Required: none
    Return
    Created hero info

        """
    st.log("Creating hero")

    hero_data = JSONParser().parse(request)
    hero_serializer = DcHeroSerializer(data=hero_data)
    if hero_serializer.is_valid():
        hero_serializer.save()
        return JsonResponse(hero_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(hero_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@renderer_classes([JSONRenderer])
def dc_hero_full_update(request,hero):

    """
     Parameters
         ----------
            ❚ Required: pageID
    Return
    The  hero by pageID if exists and updated


    """
    st.log("Updating details hero")

    hero = DcHero.objects.get(pageId=hero)
    hero_ = JSONParser().parse(request)
    hero_serializer = DcHeroSerializer(hero, data=hero_)
    if hero_serializer.is_valid():
        hero_serializer.save()
        return JsonResponse(hero_serializer.data)
    return JsonResponse(hero_serializer.errors, status=status.HTTP_400_BAD_REQUEST)       

@api_view(['PATCH'])
@renderer_classes([JSONRenderer])
def dc_hero_partial_update(request,hero):
    """
    Parameters
         ----------
            ❚ Required: pageID
    Return
    The  hero by pageID if exists and updated
    """  
    st.log("Updating details hero")

    hero = DcHero.objects.get(pageId=hero)
    hero_ = JSONParser().parse(request)
    hero_serializer = DcHeroSerializer(hero, data=hero_)
    if hero_serializer.is_valid():
        hero_serializer.save()
        return JsonResponse(hero_serializer.data)
    return JsonResponse(hero_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
def dc_hero_delete(request,hero):
    """
    Parameters
         ----------
            ❚ Required: pageID
    Return
    The deleted hero by pageID if exists and updated
    """
    st.log("Deleting hero")

    try:
        hero = DcHero.objects.get(pageId=hero)
    except DcHero.DoesNotExist:
        return JsonResponse({'message': 'Nao existe heroi com esse id'}, status=status.HTTP_404_NOT_FOUND)

    hero.delete()
    return JsonResponse({'message': 'Heroi deletado com sucesso.'})

