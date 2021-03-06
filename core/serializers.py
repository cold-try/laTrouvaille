from rest_framework import serializers
from core.models import Article, Categorie, Commentaire


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = "__all__"


class ArticlerSerializer(serializers.ModelSerializer):
    categorie = CategorieSerializer()
    class Meta:
        model = Article
        fields = "__all__"


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = "__all__"


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = "__all__"