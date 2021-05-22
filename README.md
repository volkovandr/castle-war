# castle-war
A simple castle war game with PyGame

## How to run

### Ubuntu

Assuming you already have python3 installed, create a virtual environment and install the necessary libraries as follows:

```
$ python3 -m virtualenv venv -p python3
(venv) $ source venv/bin/activate
(venv) $ pip install pygame
```

To start the game please run 

```
$ source venv/bin/activate 
(venv) $ python game/start.py
```

## How to test

### Ubuntu

Assuming you already have python3 installed, create a virtual environment and install the necessary libraries as follows:

```
$ python3 -m virtualenv venv -p python3
(venv) $ source venv/bin/activate
(venv) $ pip install pygame
(venv) $ pip install nose
```

Then run the test from the project root folder as follows:

```
$ source venv/bin/activate 
(venv) $ nosetests
```
