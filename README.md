# Higher Lower Web Game
Guess the random number from 0 to 9 in this web game made with Python and Flask Framework <br>

## Modules that were used
* Random <br>
*  Flask <br> 

**In case you don't have Flask module installed just type the code below in a terminal:**
```
pip install Flask
```

## How to setup the game
After downloading and installing Flask, you must setup the _FLASK_APP_ environment variable:
> To run the application, use the flask command or python -m flask. Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:

#### BASH
```
export FLASK_APP=server.py
flask run
```
#### CMD
```
set FLASK_APP=server.py
flask run
```
#### POWERSHELL
```
$env:FLASK_APP = "server.py"
flask run
```
If anything is not running properly, I surely recommend you to search at the Flask Official Documentation:
> https://flask.palletsprojects.com/en/2.0.x/
