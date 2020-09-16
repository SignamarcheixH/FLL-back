from django.contrib import admin
from api.models import Word, Family, Exemple, Language, Meaning

# Register your models here.

admin.site.register(Word)
admin.site.register(Family)
admin.site.register(Language)
admin.site.register(Exemple)
admin.site.register(Meaning)

# @admin.register(Meaning)
# class MeaningAdmin(admin.ModelAdmin):
#     fields = ('word', 'grammatical_type', 'exemple', 'families', 'meaning',)
