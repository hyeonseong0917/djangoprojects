from django.shortcuts import render
from django.http import HttpResponse
import datetime
import requests
import pprint
import json

def display(request):
    url = "https://developer-lostark.game.onstove.com/characters/%EB%AA%85%EC%98%88%ED%9B%88%EC%9E%A5/siblings"
    headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyIsImtpZCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyJ9.eyJpc3MiOiJodHRwczovL2x1ZHkuZ2FtZS5vbnN0b3ZlLmNvbSIsImF1ZCI6Imh0dHBzOi8vbHVkeS5nYW1lLm9uc3RvdmUuY29tL3Jlc291cmNlcyIsImNsaWVudF9pZCI6IjEwMDAwMDAwMDAwMzIxOTYifQ.hQb5_aBfT0m6ALxg59y4qH0hCLaElEQp6v_JkPAlrrESKHdIqswoltrWbJwVMbO5N6YV7yB1G5nhhHtJ4mY2BuJnbNkZSrAWz6G1wGEq6y41Pcrulz91dxR-VzOUQFhNx-lYy0b5oOP6ThDp1uSgNaZWG4UQv_0-wyP8O77Na4fYoB3Wn3fusJl5nTfGIheOWkZjL138m7WMW8uzFo3cyW8VgO_HtPNjp5ZRHa254w1w-2W5P3BXxLq31iT5bQba9DhafsjlxTgEns6zV04ILPwD_YySbymX-NidYoI_l7Gm5ArkcjoneZSxUp58z1EpI2-ptKIW7Z9FS_iAjvQ6Kw'}
    
    response = requests.get(url,headers=headers)
    jsr=response.json()
    jsrs=sorted(jsr, key=lambda x : x["ItemMaxLevel"])
    # print(type(js))
    print(jsrs[0])
    return HttpResponse(jsrs)
    # print(response.text)
    # return response
    # contents = response.text
    # # return HttpResponse("<h1>My First Django App!</h1>")
    # return contents

def displayDateTime(request):    
    dt=datetime.datetime.now()
    s="<b>Current Date and Time: </b>" +str(dt)
    return HttpResponse(s)
    
