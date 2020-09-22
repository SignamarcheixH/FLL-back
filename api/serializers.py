from rest_framework import serializers
from api.models import Word, Meaning, Language, Exemple

class WordSerializer(serializers.ModelSerializer):
	class Meta:
		model = Word
		fields = ('id', 'name',)


class LanguageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Language
		fields = ('id', 'name',)


class ExempleSerializer(serializers.ModelSerializer):
	
	language_obj = LanguageSerializer(source="language")

	class Meta:
		model = Exemple
		fields = ('id', 'sentence', 'language_obj')


class MeaningSerializer(serializers.ModelSerializer):
	
	grammatical_type_verbose = serializers.CharField(source='get_grammatical_type_display') 
	exemple_obj = ExempleSerializer(source="exemple", many=True)
	word_obj = WordSerializer(source="word")

	class Meta:
		model = Meaning
		fields = ['id', 'grammatical_type', 'grammatical_type_verbose', 'meaning', 'families', 'exemple_obj', 'word_obj']
