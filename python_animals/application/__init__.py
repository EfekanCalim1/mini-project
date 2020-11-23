from flask import Flask, jsonify
app = Flask(__name__)
from application import routes
import random