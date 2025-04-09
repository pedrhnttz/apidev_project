import os
from flask import Flask # type: ignore

app = Flask(__name__)
app.config['HOST'] = '127.0.0.1'
app.config['PORT']=5000
app.config['DEBUG'] = True