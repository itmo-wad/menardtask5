from flask import Flask
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
app.secret_key = 'secret key'
app.config.from_object(__name__)
UPLOAD_FOLDER = os.path.join(app.root_path, 'uploads')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["MONGO_URI"] = "mongodb://localhost:27017/task4_database"
Bootstrap(app)

#from main import views // Modified
from . import views
