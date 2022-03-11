import os
from django.shortcuts import render
from django.http import HttpResponse
from thirdpartyapp.settings import (
    CLIENT_ID,
    CLIENT_SECRET,
    CLIENT_REDIRECT_URL,
    CLIENT_AUTHORIZE_URL,
    CLIENT_BASE_URL,
    CLIENT_TOKEN_URL
)

import requests
from requests.auth import HTTPBasicAuth

def index(request):
    url = "http://localhost:8000/authorize?client_id=pythirdparty&redirect_uri=http%3A%2F%2F127.0.0.1%3A8002%2Fappauth%2Fcode&response_type=code&scope=all"
    return HttpResponse(url)


def authorize(request):
    full_path = request.get_full_path()
    # full_path: http://127.0.0.1:8002/appauth/code?code=v9opHZTdRdGURQ65MwJU0Q&email=fherbert%40dune.com&first_name=Frank&language=en&last_name=Herbert&role_id=2&state=&tenant_id=1&user_id=1&user_uuid=d62401ca-570a-4d0a-a74c-688dd8d8aa88

    url_params = full_path.split("?code=")[1]
    # url_params: v9opHZTdRdGURQ65MwJU0Q&email=fherbert%40dune.com&first_name=Frank&language=en&last_name=Herbert&role_id=2&state=&tenant_id=1&user_id=1&user_uuid=d62401ca-570a-4d0a-a74c-688dd8d8aa88

    url_param = url_params.split("&")
    """
    url_param:
    [
        'v9opHZTdRdGURQ65MwJU0Q',
        'email=fherbert%40dune.com',
        'first_name=Frank',
        'language=en',
        'last_name=Herbert',
        'role_id=2',
        'state=',
        'tenant_id=1',
        'user_id=1',
        'user_uuid=d62401ca-570a-4d0a-a74c-688dd8d8aa88'
    ]
    """

    code = url_param[0]
    # code: v9opHZTdRdGURQ65MwJU0Q

    # For debugging purposes.
    print("-=>",full_path)
    print("-=>",url_params)
    print("-=>",url_param)

    payload = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "state": "xyz",
        "redirect_uri": CLIENT_REDIRECT_URL,
        "code": code,
    }
    r = requests.post(CLIENT_TOKEN_URL, params=payload, data={}, auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))

    return HttpResponse(r.text)
