# Welcome to Anastasia's Volteras API Challenge!

## Running the app

Running the app is composed of (1) starting the API server and (2) running the React app.
First: clone the repo. Then go ahead and do the following to get our server running:

    cd backend
    python -m venv venv
    pip install requirements.txt
    sh start.sh
    uvicorn app.main:app --reload --host localhost --port 8001
    
To open the web app, in another tab run:

    cd ..
    cd frontend
    npm install
    npm start

... and we should be good to go! The app should be running on `localhost:3000`.

To run tests:

    cd backend
    pytest app/test/test_main.py
    pytest app/test_endpoints.py

## Overview and features

This was built with FastAPI and React. It includes:

 - [X] Created model for `VehicleData` type
 - [X] Implemented `GET` and `POST` endpoints
 - [X] Added error checks for passed parameters
 - [X] Loaded sample data through automatic loading in 	`data` folder
 - [X] Included documentation and testing [see: `backend/app/test`]
 - [X] Styled React app with Bootstrap components for clean interface
 - [X] Implemented filtering, searching, sorting, pagination, and *export* of table


## Notes

 - I leaned heavily on [this](https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-1-hello-world/) tutorial. This was my first time using FastAPI and it was incredibly helpful
 - Export functionality works by writing a .csv file to working directory!

**What I could do with more time:**

 - Right now sorting is done on the client-side and only sorts for the current page; can implement on-click functionality that rerenders data from server-side response
 - The app can use more testing, it's definitely minimal
 - Deployment to netlify/heroku
 - Form validation on frontend


