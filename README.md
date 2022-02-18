# Async Vs Sync Framework


This project will help you understand how Asynchronous and Synchronous frameworks performs using single thread.

### Frameworks used:

- Flask (Synchronous)
- Starlette (Asynchronous)

### Description

Here we will start both app using single worker thread using **gunicorn**. Both the app have two endpoints.

- {base_url}/sleeper

    ```
    sleeper is an example of blocking code that takes large 
    time to execute (in example 10 seconds). These blocking 
    could be due to io bound actions like database interactions, 
    network calls, etc.
    ```

- {base_url}/activer

    ```
    activer is simple get request that takes virtually no time 
    to execute.
    ```

Now the difference that you'll feel is that, using asynchronous framework like starlette, you'll be able to execute more requests on single thread. Internally it uses an event-loop to achieve this, more on this at [documentation](https://docs.python.org/3/library/asyncio-eventloop.html).

Clone this repository and run both apps. Check how both the system behaves when *sleeper* is called first and then *activer* (within 10 seconds).


### Installing requirements

Create a virtualenv. You can use any method, one of the easiest method is to use python-virtualenv

    virtualenv -p python3.x .venv

Activate the virtualenv

    source .venv/bin/activate

Install dependencies

    pip install -r requirements.txt

## flaskapp

Flask is a synchronous framework i.e. it runs the code in synchronous fashion. More about this on [documentation](https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application)

To run flask app, simply execute **run.sh** which will execute following bash command

    gunicorn -w 1 -b 127.0.0.1:8002 app:app

App will run on port 8002 so url endpoints will be

- http://127.0.0.1:8002/sleeper
- http://127.0.0.1:8002/activer


## starletteapp

Starlette is an asynchronous framework i.e. it runs code inside an event loop. More about this on [documentation](https://www.starlette.io/)

To run starlette app, simply execute **run.sh** which will execute following bash command

    gunicorn -w 1 -k uvicorn.workers.UvicornWorker -b 127.0.0.1:8001 app:app

App will run on 8001 so url endpoints will be

- http://127.0.0.1:8002/sleeper
- http://127.0.0.1:8002/activer


## Conclusion

If some issue persist, make sure caching is not enabled in the browser. You can also test it using curl command as:

    curl -XGET <url>

I really hope you'll grasp the knowledge and will gain curiousity for async-await. If you feel you've understood a little better, give a thumps up to this project. :D
