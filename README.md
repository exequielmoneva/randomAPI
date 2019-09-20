Random API
===================

This is a REST API created with Python. The main functionality of *Random API* is to get some specific information (Lastname, Firstname, E-Mail, Picture, Address) from the [ randomuser.me API](https://randomuser.me/api/?ud).

----------


Installation
-------------
First of all, you will need to install [Python](https://www.python.org/downloads/) and [Postman](https://www.getpostman.com/downloads/).
After that, you must use the package manager [pip](https://pip.pypa.io/en/stable/) to install virtualenv:
```bash
pip3 install virtualenv
```
> **Note:**

> - If pip3 command is not recognised by your terminal, try using **pip** instead.

Then, you should create your own virtual environment. If you don't know how to do it, you can follow [this tutorial](https://realpython.com/lessons/creating-virtual-environment/).

In order to install the exact same dependencies inside your virtual environment, you should use the requirements.txt file from the project using the following command:
```bash
pip install -r requirements.txt
``` 
#### Usage
In order to use this project, you will have to use your terminal. Inside your virtual environment, run the following task:
```bash
> set FLASK_APP=app.py
> flask run
```

Now, you should be able to try some POST requests on Postman.

## POST user's information
```
>POST http://localhost:5000/users
```
POST  request example
```
{
	"user_id":2
}
```
POST response example
```
{
    "user": {
        "Address": {
            "City": "lille - sarthe",
            "Street": "4047 avenue de l'abbé-roussel"
        },
        "E-Mail": "alban.morin@example.com",
        "Firstname": "alban",
        "Lastname": "morin",
        "Picture": "https://randomuser.me/api/portraits/men/79.jpg"
    }
}
```
## ToDo
List of possible improvements:

 - [ ] Write unit tests for all cases 
 - [ ] Find a way to decide the order of the JSON's objects

