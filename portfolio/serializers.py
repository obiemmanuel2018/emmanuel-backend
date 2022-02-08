from portfolio.models import Category,Project,Image
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
      project = serializers.SlugRelatedField(queryset=Project.objects.all(),slug_field='name')
      class Meta:
          model = Image
          fields = (
              'project',
              'file',
            
          )


class CategorySerializer(serializers.ModelSerializer):
      
      class Meta:
          model = Category
          fields = (
              'name',
               'description'
          )


class ProjectSerializer(serializers.ModelSerializer):
      images = ImageSerializer(many=True,read_only=True)
      category = serializers.SlugRelatedField(queryset=Category.objects.all(),slug_field='name')
      class Meta:
          model = Project
          fields = (
              'pk',
              'category',
              'name',
              'cover_img',
              'description',
              'images',
              'created_at',
              'updated_at'
          )