# Tutorial

1. Start `ngrok` service.

```
./ngrok http 8000
```

2. And we will use option: `https://8d4a-108-168-97-30.ngrok.io -> http://localhost:8000`.

3. Register a new user with the following request:

```shell
curl -X POST -H "Content-Type: application/json" \
     -d '{"username":"jsmith","agree_tos":true,"country":"Canada","country_tel_code":"1","email":"jsmith@dune.com","first_name":"John","last_name":"Smith","password":"pleasechangeme","password_repeat":"pleasechangeme","telephone":"(123) 456-7890"}' \
     https://biometricscloud.net/api/v1/register
```

4. (OPTIONAL) Or login with the following request:

```shell
curl -X POST -H "Content-Type: application/json" \
     -d '{"username":"jsmith","password":"pleasechangeme"}' \
      https://biometricscloud.net/api/v1/login
```

5. You'll see `access_token` and `refresh_token`, please copy and paste those values and run the following in your terminal:

```shell
export BIOMETRICSCLOUD_TPA_ACCESS_TOKEN=R9-X9fDCQ5ii4UliBvHiMw
export BIOMETRICSCLOUD_TPA_REFRESH_TOKEN=SYnhlGOcRmKk3zGsS2wf6Q
```

6. Go and create our sample application. (Notice `ngrok` values used via `redirect_url`)

```shell
curl -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $BIOMETRICSCLOUD_TPA_ACCESS_TOKEN" \
    -d '{"name":"Third Party App","description":"An example of a third party app which lives on ngrok.","website_url":"https://github.com/BCI-Innovation/biometricscloud-thirdpartyapp-python","scope":"all","redirect_url":"https://8d4a-108-168-97-30.ngrok.io/appauth/code","image_url":"https://ipregnancy.tech/static/logo.png"}' \
    https://biometricscloud.net/api/v1/applications
```

7. (OPTIONAL) If you need to update anything due to `ngrok` changes callback URL.

```shell
curl -X PUT \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $BIOMETRICSCLOUD_TPA_ACCESS_TOKEN" \
    -d '{"name":"Third Party App","description":"An example of a third party app which lives on ngrok.","website_url":"https://github.com/BCI-Innovation/biometricscloud-thirdpartyapp-python","scope":"all","redirect_url":"https://8d4a-108-168-97-30.ngrok.io/appauth/code","image_url":"https://ipregnancy.tech/static/logo.png","state":5}' \
    https://biometricscloud.net/api/v1/application/2
```

8. You will get a result something like this.

```json
{
   "id":1,
   "uuid":"e5b6cca1-2ccd-45b6-b1f8-5ff9742269e9",
   "tenant_id":1,
   "name":"Third Party App",
   "description":"An example of a third party app which lives on ngrok.",
   "website_url":"https://github.com/BCI-Innovation/biometricscloud-thirdpartyapp-python",
   "scope":"all",
   "redirect_url":"https://8d4a-108-168-97-30.ngrok.io/appauth/code",
   "image_url":"https://ipregnancy.tech/static/logo.png",
   "state":5,
   "client_id":"cef72ea49ab97b18",
   "client_secret":"eda8c7f175ab89cd9e586dc4097234c15a168aef22789f3f2b691f69a07d3c646b1f7986fea7b521a86bcf2d806098c7ecc2e078d06d2fb233552ccbc15baeb7f6207809791e644997d660910b965027c7fb662d2aed24e26e86e73ef51e672a5e0bbff9fbc98f33cb4ad7d0169a57b7ececd62b5cfaa5b8d06b76c6fee18ad",
   "created_time":"2022-03-16T05:21:51.335478Z",
   "modified_time":"2022-03-16T05:21:51.335478Z"
}
```

9. Create a `.env` file with the following contents from the result:

```
#--------#
# Django #
#--------#
SECRET_KEY='django-insecure-^y6vfc^m#j_6f$*+)n01pnogp6owb^&&^&u9mz(!u53*w247%1'
DEBUG=True

#-------#
# oAuth #
#-------#
CLIENT_ID=cef72ea49ab97b18
CLIENT_SECRET=eda8c7f175ab89cd9e586dc4097234c15a168aef22789f3f2b691f69a07d3c646b1f7986fea7b521a86bcf2d806098c7ecc2e078d06d2fb233552ccbc15baeb7f6207809791e644997d660910b965027c7fb662d2aed24e26e86e73ef51e672a5e0bbff9fbc98f33cb4ad7d0169a57b7ececd62b5cfaa5b8d06b76c6fee18ad
CLIENT_REDIRECT_URL=https://8d4a-108-168-97-30.ngrok.io/appauth/code
CLIENT_REDIRECT_V2_URL=https://8d4a-108-168-97-30.ngrok.io/appauth/code
CLIENT_AUTHORIZE_URL=http://biometricscloud.net/authorize
CLIENT_BASE_URL=http://biometricscloud.net
CLIENT_TOKEN_URL=http://biometricscloud.net/token
```

10. Run the server.

```
python manage.py runserver;
```

11. Go in browser and follow link.

```
http://localhost:8000/
```

12. There will be a link to click on, please click. In essence you will be running an `oAuth2 Authorization grant` process.

```
http://biometricscloud.net/authorize?client_id=cef72ea49ab97b18&redirect_uri=https%3A%2F%2F8d4a-108-168-97-30.ngrok.io%2Fappauth%2Fcode&response_type=code&scope=all
```

13. Afterwords please login with the credentials you registered earlier.

```json
{
    "username": "jsmith",
    "password": "pleasechangeme"    
}
```

14. Finally you'll be receive a `token` and `refresh_token`. Here is an example of how it looks like:

```json
{
   "access_token":"e2nFT1l_QkSYoTVCGkgZgQ",
   "email":"",
   "expires_in":3600,
   "first_name":"",
   "language":"",
   "last_name":"",
   "refresh_token":"QxNX3tZURRGrbz12up0sGw",
   "role_id":2,
   "scope":"all",
   "tenant_id":1,
   "token_type":"Bearer",
   "user_id":1,
   "user_uuid":"46bebc75-fcbf-4349-b7a1-393ed07c0cfa",
   "username":"jsmith"
}
```
