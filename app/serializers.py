from app.models import Profile,Email,Text
from rest_framework import serializers
from generic_relations.relations import GenericRelatedField

from backend.app.models import Contact

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = (
            'content',
        )

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = (
            'content',
        )


class ContactSerializer(serializers.ModelSerializer):
     item =  GenericRelatedField({
        Email: EmailSerializer(),
        Text:TextSerializer()
     })
     class Meta:
          model = Contact
          absolute = True
          fields = (
              'item'
          )



class ProfileSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True,read_only=True)
    class Meta:
        model = Profile
        fields = (
            'name',
            'email',
            'about',
            'resume',
            'contacts'
        )