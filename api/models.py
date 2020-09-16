from django.db import models

# Create your models here.


class Word(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name

class Family(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name

class Language(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name

class Exemple(models.Model):
	sentence = models.CharField(max_length=400)
	language = models.ForeignKey('Language', on_delete=models.CASCADE)

	def __str__(self):
		return self.sentence

class Meaning(models.Model):
	VERB = 0
	ADJECTIVE = 1
	NOUN = 2
	ADVERB = 3
	GRAMMATICAL_TYPE_CHOICES = [
		(VERB, 'Verbe'),
		(ADJECTIVE, 'Adjectif'),
		(NOUN, 'Nom'),
		(ADVERB, 'Adverbe'),
	]
	grammatical_type = models.PositiveSmallIntegerField(choices=GRAMMATICAL_TYPE_CHOICES, default=NOUN)
	meaning = models.CharField(max_length=400)
	families = models.ManyToManyField(Family, blank=True)
	exemple = models.ManyToManyField(Exemple, blank=True)
	word = models.ForeignKey('Word', on_delete=models.CASCADE, blank=True, default=None, null=True)

	def __str__(self):
		return self.meaning
