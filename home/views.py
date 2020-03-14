from django.shortcuts import render
import requests
import json

URL = "https://code.junookyo.xyz/api/ncov-moh/data.json"
r = requests.get(url=URL)


#####################################

# Create your views here.
def home_view(request, *args, **kwargs):
    json_dict = json.loads(r.text)
    data = json_dict['data']

    context = {
        'data': data
    }
    return render(request, "home.html", context)


def product_view(request, *args, **kwargs):
    return render(request, "product.html")
