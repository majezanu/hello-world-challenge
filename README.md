# hello-world-challenge
It's a challenge for an acceptance for a Go Bootcamp. It is an API Rest created using Flask. 
It contains two simple modules, first one is a "Hello world" API and the second one is a Pokemon API.

## Hello World
Contains logic to handle an endpoint that display a "Hello, World". If it recives a name in 
the URL path (Get method) or in the body (Post method), then it will display a "Hello, <name>"
with the name in those parameters.
  
## Pokemon API
Contains logic to handle two endpoints, also handles a provider to retrieve information about
pokemon using an external APi. First endpoint receives two values and try to calculate
a random integer, that integer is used to retrieve a Pokemon by its ID. The second endpoint
receives a name in the path parameter and uses that name to retrieve a Pokemon by its name.
  
## How to run:
1. Create a virtual environment
2. Execute the following command to install all required packages:
  ```bash
  $ pip install -r requirements.txt
  ```
3. Execute the following commands to run the flask server:
  ```bash
  $ export FLASK_APP=api 
  $ flask run
  ```
 4. Import the `hello_world_challenge.json` file into Postman and use the request to call the endpoints.
 
