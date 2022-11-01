# PYTHON ZOOM REST API SCRIPT TEMPLATE

## Installation
[Download](https://www.python.org/downloads/) and Install the latest python version.


Clone this project
```
git clone LINK HERE
```
Install dependencies
```
pip install -r requirements.txt
```

## Usage
This project should act as a GUI to interact with the Zoom REST API
Authentication is Handled through a Zoom [Server to Server OAuth application](https://marketplace.zoom.us/docs/guides/build/server-to-server-oauth-app/)
Tokens are stored in a sqlite3 db and only updated when expired
Be Sure to Add the necessary scopes to your marketplace app

You will need to create a ```.env``` file  in the root of the project with the following
```
ACCOUNTID="yourAccountID"
CLIENTID="yourClientID"
CLIENTSECRET="yourClientSecret"
LOGGING_LEVEL="DEBUG"
```
LOGGING_LEVEL must be an  upper-case string and can be set to INFO, DEBUG, or WARNING
#### Running the script
In your terminal navigate to the root folder where you cloned this project
##### on Mac
```
python3 app.py
```
##### on Windows
```
python app.py
```
## Logging
A logfile is generate for you in ``` ./logs/log.log```
This logfile will contain all of the information you need to debug your Zoom REST API requests