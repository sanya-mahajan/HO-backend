#create serializer that accept user input string and uses web scraping to get the data from the url
from rest_framework import serializers
from .scrapeMedInfo import get_med_info

class SearchMedInfoSerializer(serializers.Serializer):
    search=serializers.CharField(max_length=100)
    
    def validate_search(self, value):
        print("value",value)
        if get_med_info(value):
            return value
        else:
            raise serializers.ValidationError("invalid search terms")