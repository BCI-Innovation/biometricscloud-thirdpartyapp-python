python3 -m venv env
source env/bin/activate
pip install - requirements.txt

cd thirdpartyapp
./runserver.sh

browser: http://localhost:8002/


**Step 1:** In your [osin-example](http://github.com/BCI-Innovation/biometricscloud-backend) project run:

```
go run main.go add_client --client_id=pythirdparty \
                          --client_secret=pleasechange \
                          --redirect_uri=http://127.0.0.1:8002/appauth/code
```

**Step 2:** In your [osin-thirdparty-example](https://github.com/BCI-Innovation/biometricscloud-thirdpartyapp-golang) project please run the following:

```
go run main.go serve --client_id=thirdparty \
                     --client_secret=pleasechange \
                     --redirect_uri=http://127.0.0.1:8001/appauth/code \
                     --authorize_uri=http://localhost:8000/authorize \
                     --token_url=http://localhost:8000/token

```

**Step 3:** In your browser, go to [http://127.0.0.1:8001](http://127.0.0.1:8001). Click the `Login` link and you will be redirected to the `osin` auth server. Fill in your credentials that you created previously and then you will be taken to the success page.
