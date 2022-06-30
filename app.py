#### Set Up the Flask Weather App
# Import dependencies

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

####################################
## Module 9.5.1 ##
# Set Up the Database
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into a new model
Base = automap_base()
# reflect the tables into SQLAlchemy
Base.prepare(engine, reflect=True)

# Save our references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database
session = Session(engine)

##################################
# Create a new Flask App #
##################################
app = Flask(__name__)

