from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.


class Profile(models.Model):
      name = models.CharField(max_length=255)
      email = models.EmailField(unique=True)
      about = models.TextField()
      resume = models.FileField(upload_to="profile/resume")
     

class Contact(models.Model):
      profile = models.ForeignKey(Profile,related_name='contacts',on_delete=models.CASCADE)
      content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE,
                                     limit_choices_to={'model__in':(
                                     'text',
                                     'email')})
      object_id = models.PositiveIntegerField()
      item = GenericForeignKey('content_type', 'object_id')
      
      def __str__(self):
          return self.profile.name
     



class ItemBase(models.Model):
      name = models.CharField(max_length=50)
      logo = models.ImageField(upload_to="profile/contact/logo")

      def __str__(self):
          return self.name
      class Meta:
          abstract = True


class Email(ItemBase):
      content = models.EmailField(unique=True)
class Text(ItemBase):
      content = models.CharField(max_length=100,unique=True)


      

