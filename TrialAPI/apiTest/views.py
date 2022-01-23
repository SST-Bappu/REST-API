import json
from django.http import response
from django.shortcuts import render
import requests
# Create your views here.

def home_token(request): #Token authentication
    endpoint = 'http://localhost:8000/app/cars/'
    head = {"Authorization": "Token 33dc54ac1f551cefa0b9d2539e9c9c1e9a88eaa5"}
    res = requests.get(endpoint,headers=head)
    data = res
    print(res)
    print(data)
    return response.HttpResponse(data)

def delete_car(request):
    endpoint = 'http://localhost:8000/app/cars/100'
    head = {"Authorization": "Token 33dc54ac1f551cefa0b9d2539e9c9c1e9a88eaa5"}
    res = requests.delete(endpoint,headers=head)
    print(res)
    # print(res.content)
    return response.HttpResponse("1 item deleted successfully")


def update_car(request):
    endpoint = 'http://localhost:8000/app/cars/45/'
    head = {"Authorization": "Token 33dc54ac1f551cefa0b9d2539e9c9c1e9a88eaa5"}
    res = requests.put(endpoint,data={'model':'newModel'})
    print(res)
    print(res.content)
    return response.HttpResponse("1 item updated successfully")













def home(request): #Sending and handling url with parameters in allow-any permission
    res = requests.get("http://localhost:8000/app/home/?id=101&key=200")
    data = res.json()
    print(res)
    print(data)
    return response.HttpResponse("<h1>We get accesss of that particular API</h1>")

def home_s(request): #Token authentication
    endpoint = 'http://localhost:8000/racing/driver'
    head = {"Authorization": "Token 33dc54ac1f551cefa0b9d2539e9c9c1e9a88eaa5"}
    res = requests.get(endpoint,headers=head)
    data = res.json()
    print(data)
    print(res)
    return response.HttpResponse(data)

def home_jwt(request): #JWT Authentication
    endpoint = 'http://localhost:8000/api/token/'
    data = {
        'username': 'SST',
        'password': 'p@ssw@rd123'
    }
    res = requests.post(endpoint,data = data)
    print(res)
    data = res.content
    data = data.decode('utf8').replace("'",'"')
    data = json.loads(data)
    refresh = data['refresh']
    access = data['access']
    try:
        endpoint = 'http://localhost:8000/racing/driver'
        head = {"Authorization": f"Bearer {access}"}
        res = requests.get(endpoint,headers=head)
        data = res.json()
        print(data)
        print(res)
        return response.HttpResponse("<h1>We get accesss of that particular API</h1>")
    except:
       return response.HttpResponse("<h1>API error</h1>")
        