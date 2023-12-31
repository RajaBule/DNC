from django import forms
from .models import Samples

class newsample(forms.ModelForm):
    class Meta:
        model = Samples
        fields = ('id', 'name', 'location', 'stype','sampleweight',
                  'sampleweightunit', 'expweight', 'expweightunit',
                  'customer', 'project', 'notes', 'country', 'farm',
                  'tracknum', 'importer', 'exporter', 'wetmill', 'drymill',
                  'cooperative', 'assosiation', 'othertrac', 'moisture',
                  'wa', 'proccessing', 'density', 'screensize',
                  'varieties', 'cropyear', 'classification',
                  'grade', 'generalcomments', 'sensorial', 'sensorialdescriptors')