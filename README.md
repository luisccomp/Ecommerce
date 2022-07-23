# Django simple ecommerce app

This is a simple ecommerce application written using Python and Django framework. The purpose of this application is
for educational reason only and there is no intent to release in production other than demonstration of my skills
using this tool. This `README` file will explain how to setup and run project locally and how to deploy this project
on a cloud container.

## Local project setup

Before install project's dependencies, is strongly recommended to create a virtual environment in order to isolate
project dependencies and not mess up with other projects running locally. To do that you must run the following
command:

Linux/Mac OSX:
```sh
$ python3 -m venv venv
```
Windows:
```
> python -m venv venv
```

And then activate it:

Linux/Mac OSX:
```
$ source venv/bin/activate
```

Windows:
```
> .\venv\Scripts\activate
```

After creation of virtual environment and it's activation, now it's time to download project dependencies. First,
update package manager and install it's latest version:

Linux/Mac OSX/Windows
```
python -m pip install --upgrade pip
```

Then install the packages:

Linux/Mac OSX/Windows
```
pip install -r requirements.txt
```

To run the server locally, just type:

```
python manage.py runserver
```