from rest_framework import serializers
from dummy_opennotes.models import DummyOpenNotes

class DummyOpenNotesSerializer(serializers.ModelSerializer):
  class Meta:
    model = DummyOpenNotes
    fields =  ['id', 'title', 'note', 'created']
