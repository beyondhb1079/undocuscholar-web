from rest_framework import serializers
from scholarships.models import Scholarship

class ScholarshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scholarship
        fields = ('name', 'deadline', 'amount', 'description', 'website')