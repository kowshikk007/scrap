from flask import Flask, render_template, request
import pickle
import numpy as np
app = Flask(__name__)
@app.route('/')
def hello():
    """test functions"""
    return "Welcome to PVP college"
app.run()
