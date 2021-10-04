from core.models import Contato
from rest_framework import serializers

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ['nome','email','telefone','aniversario','id']
