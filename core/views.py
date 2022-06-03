from unicodedata import category
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


from rest_framework.parsers import FormParser
from rest_framework.decorators import api_view, permission_classes, parser_classes, throttle_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from core.serializers import ArticlerSerializer, CategorieSerializer, CommentarySerializer
from core.models import Article, Categorie, Commentaire
from core.paginations import CustomPagination


def pagination(query_set, request, serializer):
    paginator = CustomPagination()
    paginator.page_size = 10
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

    related_articles = Article.objects.filter(categorie=article_details.categorie).exclude(id=pk).order_by('-id')[:5]
    related_articles_serializer = ArticlerSerializer(related_articles, many=True)

    comments = Commentaire.objects.filter(article=article_details)
    comments_serializer = CommentarySerializer(comments, many=True)
    return Response({'articleDetails': article_details_serializer.data, 'relatedArticles': related_articles_serializer.data,
    'comments': comments_serializer.data})


@api_view(['POST'])
@throttle_classes([UserRateThrottle])
@permission_classes([AllowAny])
def send_commentary(request):
    targeted_article = Article.objects.get(id=request.data['id'])
    Commentaire(
        article=targeted_article, 
        commentary=request.data['commentContent'], 
        email=request.data['commentEmail'], 
        author=request.data['commentAuthor'], 
        website=request.data['commentWebsite']
    ).save()
    comments = Commentaire.objects.filter(article=targeted_article)
    comments_serializer = CommentarySerializer(comments, many=True)
    return Response({'comments': comments_serializer.data})
    

@api_view(['GET'])
@permission_classes([AllowAny])
def get_categories(request):
    categories = Categorie.objects.all()
    categories_serializer = CategorieSerializer(categories, many=True)
    return Response({'getCategories': categories_serializer.data})


@api_view(['GET'])
@permission_classes([AllowAny])
def get_bestof(request):
    bestof_article = Article.objects.filter(best_of_year=True)
    paginated = pagination(bestof_article, request, ArticlerSerializer)
    return Response({'articles': paginated.data, 'fromCategory': 'Meilleur de 2022'})


@api_view(['GET'])
@permission_classes([AllowAny])
def get_selection(request):
    bestof_article = Article.objects.filter(our_selection_panel=True)
    paginated = pagination(bestof_article, request, ArticlerSerializer)
    return Response({'articles': paginated.data, 'fromCategory': 'Notre sélection'})