# Simple API with authentication  

## Introduction: 

The following project is a simple python flask program that hosts a REST API with support for user authentication and storing data on a postgres sql db. 

The program uses postgres sql database, one for testing and another for development. Both need to be set-up before starting with this project. The program also requires python3 installed in your computer. If you want the simplest way to deploy, please skip to Heroku Deployment.


## Set-up and Installation and Testing 

### A) Pre-requisites 

1) Make sure you have python3 installed 

2) Make sure you have postgres sql database installed 

## B) Installation 

1) Make sure you have pipenv installed if not please run ``` pip install pipenv  ```

1) ```git clone https://github.com/araa47/Flask-API-for-Authentication ```

2) ``` cd Flask-API-for-Authentication  ```

3) ``` pipenv install```

4) Make sure you create databases for both testing and production. This can be simply done using the following command ``` createdb dna ```  and ``` createdb dna-testing ```

5) Once you have both the databases, create a user with only read and write acess to the database 

6) Currently there are a few config variables you will need to set in order to run the program they can be found in the .env.sample file. This file needs to be copied, and renamed as .env  . Afer this you can modify the variables to the values you need

7) Once you have these values populated, you can initialize a migration ```python manage.py db init```. This should create a new migration subfolder in the project directory 

8) Now you can run the script to populate files ```python manage.py db migrate ```

9) Finally apply changes to db by running ```python manage.py db upgrade```

10) You can confirm if the tables were created by running the ```psql``` command then running ```\connect dna``` and finally ```\dt``` to check wheter the users table was created. 

11) Since the project is ready to run on heroku already, if you want to test on your local environment you will need to make a few minor changes. You will have to adjust the api_url to localhost on all the .html files under /src/templates/. This is so each page sends the requests to the correct API. It has although been changed to the heroku URL for current deployment. 

12) If everything went smoothly you are ready to run this project on a local environment for development. Simply run  ```python run.py``` to run the project. This should get the API running and also allow acess to the simple User Interface for testing. 



## C) Testing 

The project currently has tests in the /src/tests/test_users.py file. In order to run the tests simply run ```pytest --cov=src``` which currently has about 90% coverage of all the code in this project. If all the tests pass you are ready for running the website and API. 


## D) Heroku Deployment 

1) Clone project to your own github 

2) Create app on Heroku 

3) Connect to github project 

4) Add postgresql to the project or host your own database and note down the URL

5) Go into Heroku app settings and "Reveal Config Vars"

6) Fill in the config variables just like in the sample.env file. If you used the addon database, the database URL should be auto populated. 

7) Finally open the console on Heroku and run the db migration commands to fill the database. This is only required if its the first time using a new database. 


## Website 

To acess the website simply go to the url of the API followed by /login.html, in my case its "http://0.0.0.0:5000/login.html" This will bring you to a login page, click on Register if you wish to register. Once sucesfully logged in the page will display a stats page with information about the user. Currently it is three simple static files, "login.html", "signup.html" and "stats.html" that has been built for the simple user interface. 

## API and Endpoints 

Currently there are a couple of endpoints that have been developed and tested but not all endpoints are used by the website.

1) POST: /api/v1/users - create a user(CREATE). You will need to enter the following json information in the body as application json. Genetic result and policy are not required and are not filled in by the user when logging in through the login page. Currently the simplest method to update this would be to directly talk to the database or use the PUT method in method 5. 
```
{
"email":"testemail@email.com",
"password": "testpass",
"first_name": "Testname",
"last_name": "Lastname",
"dob": "1995-02-02",
"genetic_result": {"DNA": "XY","XDNA": "YY"},
"policy":"A1B2C3D4"
}
```
The above request will get either a json response with "error" describing the error or return a jwt-token which will be needed to be saved to be used to acess the stats of the user. 

2) POST: /api/v1/users/login - user login. You will need to enter the following json information in the body.

```
{
"email":"testemail@email.com",
"password": "testpass"
}
```
The above request will get either a json response with "error" describing the error or return a jwt-token which will be needed to be saved to be used to acess the stats of the user. 

2) GET /api/v1/users - get all registered users(READ). (this was used for testing and can be removed in the final deployment)

jwt-token will be required to be added in the 'HEADERS' of the get request as 'api-token'

3) GET /api/v1/users/<user_id> - get a user(READ) (this was used for testing and can be removed in the final deployment)
jwt-token will be required to be added in the 'HEADERS' of the get request as 'api-token'

4) GET /api/v1/users/me - get my info(READ) 
jwt-token will be required to be added in the 'HEADERS' of the get request as 'api-token'

5) PUT /api/v1/users/me - update my account(UPDATE)
jwt-token will be required to be added in the 'HEADERS' of the post request as 'api-token'. Plus any information to be changed needs to be added to the body. 
```
{

"first_name": "NewFirstName"

}
```
6) DELETE /api/v1/users/me - Delete my account(DELETE)
jwt-token will be required to be added in the 'HEADERS' of the delete request as 'api-token'



## Design

### Database 
I chose PostgreSQL for the database and Flask for the API. Everything is simply connected using manage.py file that helps with migrations as decsribed in steps 7-9 of the installation instructions. The database model can be found in the /src/models/UserModel.py file. Currenlty everything is stored in a single table for simplicity, but in the future I would like to keep authentication in a single table and the Genetic Result and Policy info in a different one. This also ensures users only may be able to modify their personal infomration and not the policy number or genetic result. However this was not done to save time for this deployment. The user only is able to modify the other values since the frontend restricts acess however using the POST API it is possible to modify any of these values. In the future this seperation would allow user accounts with mutliple users inside, making it easy to build solutions for corporate accounts with multiple users using the new db model. 

### API 
For the API I have used python flask due to ease of development and deployment using services such as heroku. The User API is mostly avaialbale in the /src/views/UserView file while the 3 simple static pages are being served from the Home API in the /src/views/HomeView file. In order to encrypt communication JWT tokens are being used for authentication, for further security, SSL certificate would be required to ensure all the communication is encrypted. 

### Scaling 

There are multiple ways to approach this problem. This whole project could be run in a docker container, running multiple instances of the flask server connected to the same database through a load balancing server. This would make scaling up and down easy but still would require some modifcations. For even simpler scaling, this could be run using gunicorn on Heroku allowing you to simply scale the project by inceeasing the number of instances. However this may be slightly more pricey. 

## Future Updates 

1) Remove unecessary API endpoints 
2) Create a new table for genetics and policy number 
3) Create custom methods to modify these genetics and policy that are only available for admins 
4) Work on a better User Interface and handle some more checks in the front-end 
5) Instead of using the url to trasnfer the jwt-token between pages, use a different method that does not give away the jwt-token in the URL (maybe localstorage)
6) Add captcha, remember me on login page 
7) Imporve API by limiting acess if more than 3 failed consecutive login attempts are made 
8) Add some regex to ensure password is strong, and also add minimum characters to make it more secure 
9) Enable SSL encryption on the server 






