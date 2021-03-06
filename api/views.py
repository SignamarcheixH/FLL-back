import csv, io, random
from django.shortcuts import render
from django.contrib import messages
from rest_framework import viewsets, response
from rest_framework.decorators import action
from api.serializers import WordSerializer, MeaningSerializer
from api.models import Word, Language, Exemple, Meaning

class WordViewset(viewsets.ModelViewSet):
	queryset = Word.objects.all().order_by('name')
	serializer_class = WordSerializer

	@action(
		methods=['get'], detail=False,
		url_path="random", url_name="random"
	)
	def random(self, request):
		total = Word.objects.all().count()
		random_index = random.randint(1, total - 1)
		queryset = Word.objects.all()[random_index]
		serializer = self.serializer_class(queryset)
		return response.Response(serializer.data)

class MeaningViewset(viewsets.ModelViewSet):


	serializer_class = MeaningSerializer

	def get_queryset(self):
		queryset = Meaning.objects.all().order_by('word__name')
		filter_letter = self.request.query_params.get('letter', None)
		if(filter_letter):
			queryset = queryset.filter(word__name__startswith=filter_letter).order_by('word__name')
		return queryset
		

	@action(
		methods=['get'], detail=False,
		url_path="random", url_name="random"
	)
	def random(self, request):
		total = Meaning.objects.all().count()
		random_index = random.randint(1, total - 1)
		queryset = Meaning.objects.all()[random_index]
		serializer = self.serializer_class(queryset)
		return response.Response(serializer.data)


# Create your views here.

def csv_upload(request):
	template = "csv_upload.html"
	data = Word.objects.all()
	prompt = {
		'order': 'Order of the CSV should be name, email, address, phone, profile',
		'words': data
	}
	if request.method == "GET":
		return render(request, template, prompt)
	csv_file = request.FILES['file']
	if not csv_file.name.endswith('.csv'):
		messages.error(request, 'THIS IS NOT A CSV FILE')
	data_set = csv_file.read().decode('UTF-8')

	io_string = io.StringIO(data_set)
	next(io_string)
	for column in csv.reader(io_string, delimiter=','):
		word = column[0]
		meaning = column[1]
		exemple = column[2]
		gramma_types = {
			'V' : 0,
			'A' : 1,
			'N' : 2
		}
		gramma_type = gramma_types[column[3]]

		english = Language.objects.get(name="English")
		newWord, created = Word.objects.update_or_create(
			name = word
		)
		newExemple, created = Exemple.objects.update_or_create(
			sentence = exemple,
			language = english
		)
		newMeaning, created = Meaning.objects.get_or_create(meaning = meaning, word=Word.objects.get(id=newWord.id), grammatical_type=gramma_type)
		newMeaning.exemple.add(Exemple.objects.get(id=newExemple.id))
		
	context = {}
	return render(request, template, context)
