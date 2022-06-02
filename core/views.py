from unicodedata import category
from django.shortcuts import render

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, permission_classes, parser_classes, throttle_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from core.serializers import ArticlerSerializer, CategorieSerializer
from core.models import Article, Categorie
from core.paginations import CustomPagination


def pagination(query_set, request, serializer):
    paginator = CustomPagination()
    paginator.page_size = 3
    result_page = paginator.paginate_queryset(query_set, request)
    queryset_serializer = serializer(result_page, many=True)
    paginate = paginator.get_paginated_response(queryset_serializer.data)
    return paginate


@api_view(['GET'])
@permission_classes([AllowAny])
def last_entries(request):
    last_entries = Article.objects.all()
    paginated = pagination(last_entries, request, ArticlerSerializer)
    return Response({'articles': paginated.data, 'fromCategory': False})


@api_view(['GET'])
@permission_classes([AllowAny])
def per_categories(request, id):
    selected_category = Categorie.objects.get(id=id)
    last_entries = Article.objects.filter(categorie=selected_category)
    paginated = pagination(last_entries, request, ArticlerSerializer)
    return Response({'articles': paginated.data, 'fromCategory': selected_category.nom,
    'categoryId':id})


@api_view(['GET'])
@permission_classes([AllowAny])
def article_details(request, pk=None):
    article_details = Article.objects.get(id=pk)
    article_details_serializer = ArticlerSerializer(article_details)
    return Response({'articleDetails': article_details_serializer.data})


@api_view(['GET'])
def get_categories(request):
    categories = Categorie.objects.all()
    categories_serializer = CategorieSerializer(categories, many=True)
    return Response({'getCategories': categories_serializer.data})