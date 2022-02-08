
from distutils.command.upload import upload
from django.db import models

# Create your models here.


class Category(models.Model):
     
      name = models.CharField(max_length=200,unique=True)
      description = models.TextField()

      def __str__(self):
          return self.name
      


class Project(models.Model):
      category = models.ForeignKey(Category,related_name='projects',on_delete=models.CASCADE)
      name = models.CharField(max_length=200)
      cover_img = models.ImageField(upload_to='projects/cover/%y/%m/%d')
      description = models.TextField()
      views = models.BigIntegerField(default=0)
      created_at = models.DateField(auto_now=True)
      updated_at = models.DateField(auto_now_add=True)
      

      def __str__(self):
          return self.name


class Image(models.Model):
      project = models.ForeignKey(Project,related_name='images',on_delete=models.CASCADE)
      file = models.ImageField(upload_to='projects/images/%y/%m/%d')
      
      def __str__(self):
          return "Image for {}".format(self.project.name)
