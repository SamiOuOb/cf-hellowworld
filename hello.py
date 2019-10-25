from flask import Flask, render_template, Markup
import os
import json
import random
import time
import _thread
from multiprocessing import Pool
from multiprocessing import cpu_count
import signal
from receive import receive_data
from send import send_data

app = Flask(__name__)

# get CF environment variables
port = int(os.getenv("PORT"))




stop_loop = 0
def exit_chld(x, y):
    global stop_loop
    stop_loop = 1

def f(x):
    global stop_loop
    while not stop_loop:
        x*x

signal.signal(signal.SIGINT, exit_chld)

def run_gogo():
    processes = cpu_count()
    print('-' * 20)
    print('Running load on CPU(s)')
    print('Utilizing %d cores' % processes)
    print('-' * 20)
    pool = Pool(processes)
    pool.map(f, range(processes))
    content = Markup(processes)
    return content

def hello():
    # send_data()
    receive_data()

@app.route('/')
def hello_world():
    _thread.start_new_thread( hello, () )
    
    return render_template("index.html", content=content)
    # return render_template("index.html")

@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    return response
def start():
    app.run(host='10.10.0.13', port=port)
if __name__ == '__main__':

    _thread.start_new_thread( start, () )
    # run_gogo()
    
