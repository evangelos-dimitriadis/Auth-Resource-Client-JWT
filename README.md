# A simple Auth-Resource-Client JWT example in Flask

This is an example as how a system with 3 services and JWT (JSON Web Tokens) works.
Instead of heaving the authentication at the same service as the resources are, we devide those into two dedicated services. Public-key cryptography is being used where the authorization has access to the user database and can generate tokens using the private key (`jwt-key`), while the resource server can use those to grant access to the API using the public key (jwt-key.pub). This way only one service has access to the database which includes the hashed passwords and potential many more information, while other services can verify the tokens without having to make a call to the authentication server.


## Requirements

python3.11
libpython3.11-dev (Ubuntu) or similar for other OS, for installation of uWSGI and a C compiler (gcc and clang are supported)

You can also use the docker-compose.


## How to run the project

### Using virtual enviroment for the servers

1. From the auth folder enter the virtual enviroment, install the libraries and start the server
`python3.11 -m venv env`
`source env/bin/activate`
`pip install -r requirements.txt`
`uwsgi --ini uwsgi.ini --honour-std`
  
2. From the resources-server folder enter the virtual enviroment, install the libraries and start the server
`python3.11 -m venv env`
`source env/bin/activate`
`pip install -r requirements.txt`
`uwsgi --ini uwsgi.ini --honour-std`


### Using the containers for the servers

Build and start the containers:

`docker-compose build`
`docker-compose up`


### Run the client

3. From the client folder enter the virtual enviroment, install the libraries and start the server
`python3.11 -m venv env`
`source env/bin/activate`
`pip install -r requirements.txt`
`python client.py`


## Testing

Both servers can be tested by typing from each folder:

`python -m pytest  tests`
