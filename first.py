def first_kakao(auth_code):
    import requests

    url = 'https://kauth.kakao.com/oauth/token'
    rest_api_key = '내 API KEY'
    redirect_uri = 'https://example.com/oauth'
    authorize_code = auth_code

    data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

    response = requests.post(url, data=data)
    tokens = response.json()
    print(tokens)

# json 저장
    import json
    with open("kakao_code.json","w") as fp:
        json.dump(tokens, fp)
