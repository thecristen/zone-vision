"""Functions to fetch data and generate models to the database"""
import json
import requests
from django.contrib.gis.geos import GEOSGeometry
from .models import Zone

def get_zones():
    """Creates zones by fetching them via the Zoning.io API"""
    zones = []
    zoning_request = requests.get('https://zoning.io/en/api/1.0/jurisdictions.json')
    jurisdictions = zoning_request.json()
    for result in jurisdictions['data']:
        shape_url = result['attributes']['zone_shapes']['geojson']
        shape_request = requests.get(shape_url)
        shape_geojson = shape_request.json() # GeoJSON FeatureCollection

        for feature in shape_geojson['features']:
            if feature['geometry']:
                if feature['geometry']['type'] == 'Polygon':
                    feature['geometry']['type'] = 'MultiPolygon'
                geo_string = json.dumps(feature['geometry'])
                zones.append(Zone(
                    name=feature['properties']['name'],
                    code=feature['properties']['code'],
                    keywords=feature['properties']['keywords'],
                    description=feature['properties']['description'],
                    geometry=GEOSGeometry(geo_string, srid=4326)
                ))

    Zone.objects.bulk_create(zones)
