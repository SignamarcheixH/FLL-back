from rest_framework import serializers
from api.models import Word

class WordSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Word
		fields = ('name',)