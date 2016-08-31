"""
Basic Utility function
"""
import math
import json
import decimal
import datetime
from restaurants.models import Restaurant
from django.forms.models import model_to_dict
from django.core import serializers

def distance_in_kms(lat1, long1, lat2, long2):
    degrees_to_radians = math.pi/180.0
    phi1 = (90.0-lat1)*degrees_to_radians
    phi2 = (90.0-lat2)*degrees_to_radians
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1-theta2)+math.cos(phi1)*math.cos(phi2))
    arc = math.acos(cos)
    return arc * 6371

def getKey(item):
    return item['fields']['distance']

def nearby_restaurants(latitude, longitude):
    restaurants = Restaurant.objects.all()
    restaurants = serializers.serialize('python', restaurants)
    for restaurant in restaurants:
        restaurant['fields']['distance'] = distance_in_kms(float(latitude), float(longitude), float(restaurant['fields']['lat']), float(restaurant['fields']['lag']))
        print latitude, longitude, restaurant['fields']['lat'], restaurant['fields']['lag']
    temp = sorted(restaurants, key=getKey)
    return temp

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return "%.2f" % obj
        if isinstance(obj, datetime.datetime):
            return str(obj)
        return json.JSONEncoder.default(self, obj)
