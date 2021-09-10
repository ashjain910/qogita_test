# ASSUMPTIONS

1. Address duplication detection is a very complex problem. We can find duplicate addresses based on lat/lon, data cleansing and finding similar address (st vs street, apt vs aparments etc). But for the purpose of this exercise, I am assuming that simple string match works. That is a address is duplicate only if the same text is entered in all fields i.e. state, country, pincode, street and state.
2. Address validation not done. For the sake of simplicity, I am skipping validation of the entered address and assuming correct address is entered. We should be using google or some libraries for address validation 
3. No projects should be sent without unit tests. But there is only so much we can do in a 3 hour window. So skipping unit tests for now.
4. Not required but I have also setup a docker file that can be used to run this.

# DEVELOPER SETUP
(Not required but I have also setup a docker file that can be used to run this. Just do ```docker-compose up``` and you should be good!!)


clone this repository (master branch) and run the below commands
The below commands sets up the virutal env, loads the .env file and set up the database

```
python3 -m venv env    
source env/bin/activate
pip install -r requirements.txt 
set -a; source .env ; set +a
./manage.py makemigrations
./manage.py migrate 

```

- To run the server locally
`% ./manage.py runserver`


- Create a dummy user for testing
```
>>> from django.contrib.auth.models import User
>>> u = User.objects.create( first_name = 'qogita', last_name = 'user', email = 'ash@qogita.com', username= 'ash@qogita.com')
>>> u.set_password('ash')
>>> u.save()
```

## USER DOCUMENTATION
- We will be using httpie for simulating the REST calls

### Authenticate the user
- We are using token authentication to authenticate a user. The token will be sent as header in all further requests to identify this user.

Request :
```
http post 'http://127.0.0.1:8000/api-token-auth/' username=ash@qogita.com password=ash
```

Response: (200 OK)
```
{
    "token": "35540ab019d7b208f3c2f81bce826000fb23c2bb"
}
```



### Create an Address for this user

#### Request with validation error

Request :
```
http post 'http://127.0.0.1:8000/address/' Authorization:'Token 35540ab019d7b208f3c2f81bce826000fb23c2bb'
```

Error Response : (403 ERROR)
```
{
    "city": [
        "This field is required."
    ],
    "country": [
        "This field is required."
    ],
    "pincode": [
        "This field is required."
    ],
    "state": [
        "This field is required."
    ],
    "street": [
        "This field is required."
    ]
}
```

#### Successful request/response

Request : 
```
http post 'http://127.0.0.1:8000/address/' Authorization:'Token 35540ab019d7b208f3c2f81bce826000fb23c2bb' city=Chennai country=India pincode=600024 state=TamilNadu street='123 chennai'
```

Response (200 OK)
```
{}
```

#### Duplicate user request

Request : 
```
http post 'http://127.0.0.1:8000/address/' Authorization:'Token 35540ab019d7b208f3c2f81bce826000fb23c2bb' city=Chennai country=India pincode=600024 state=TamilNadu street='123 chennai'
```

Response (200 OK)
```
{
    "error": "Duplicate address found. Please add a new unique address"
}
```


### Get All addresses for this user

Request:
```
http get 'http://127.0.0.1:8000/address/' Authorization:'Token 35540ab019d7b208f3c2f81bce826000fb23c2bb'
```

Response:
```
[{
    "city" : "Chennai",
    "country": "India",
    "state": "TamilNadu",
    "street": "123 chennai",
    "pincode": "600024",
    "id" : 1

},{

    "city" : "Chennai",
    "country": "India",
    "state": "TamilNadu",
    "street": "123 tamil",
    "pincode": "600025",
    "id" : 2

}
```

### FILTER ADDRESSES

```
http get 'http://127.0.0.1:8000/address/?pincode=600025' Authorization:'Token 35540ab019d7b208f3c2f81bce826000fb23c2bb'
```

### PAGINATION (first 10 only sent by default)

```
http get 'http://127.0.0.1:8000/address/?limit=10&offset=10' Authorization:'Token 35540ab019d7b208f3c2f81bce826000fb23c2bb'
```

### Update Address

```
http PUT 'http://127.0.0.1:8000/address/10/' Authorization:'Token 35540ab019d7b208f3c2f81bce826000fb23c2bb' city=Andhra
```

### Delete single Address

```
http DELETE 'http://127.0.0.1:8000/address/10/' Authorization:'Token 35540ab019d7b208f3c2f81bce826000fb23c2bb'
```

### Delete multiple Addresses
- Provide a list of ids in the body as comma seperate value

```
http post 'http://127.0.0.1:8000/address/10/' Authorization:'Token 35540ab019d7b208f3c2f81bce826000fb23c2bb' ids=1,2,3
```



