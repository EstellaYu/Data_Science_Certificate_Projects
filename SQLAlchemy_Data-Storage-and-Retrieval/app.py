import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify, redirect


#################################################
# Connect with Database
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same_thread': False})
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

####   HOME   ###################################
@app.route("/")
def welcome():
    return (
        f"Welcome Hawaii Weather API!<br/><br/>"
        f"Here are the Available Routes:<br/><br/>"

        f"/api/v1.0<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/'start_date' <br>"
        f"/api/v1.0/'start_date'/'end_date' <br>"
    )

####   PRECIPITATION   ############################
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return date and precipitation as json"""

    prcp_all = session.query(Measurement.date, func.avg(Measurement.prcp)).\
               group_by(Measurement.date).\
               order_by(Measurement.date.desc()).all()

    # dictionary of {"date": "date-val", "prcp" : "prcp-val"}   
    prcp_all_list = []

    for prcp in prcp_all:
    	prcp_all_list.append({"date": prcp[0], "prcp": prcp[1]})

    return jsonify(prcp_all_list)

####   STATIONS   #################################
@app.route("/api/v1.0/stations")
def stations():
    """Return the list of all stations as json"""
    
    stations = session.query(Station.station, Station.name).group_by(Station.station).all()

    stations_list = []
    for sta in stations:
    	stations_list.append({"id": sta[0], "name": sta[1]})

    return jsonify(stations_list)

####   TEMP OVSERVATIONS   ########################
@app.route("/api/v1.0/tobs")
def tobs():
	last_date = session.query(Measurement.date).group_by(Measurement.date).order_by(Measurement.date.desc()).first()
	last_date = dt.datetime.strptime(last_date[0],'%Y-%m-%d').date()
	one_year_from_last_day = dt.date(last_date.year - 1, last_date.month, last_date.day)

	temp_over_1_year = session.query(func.avg(Measurement.tobs), Measurement.date).\
								filter(Measurement.date > one_year_from_last_day).\
								filter(Measurement.date <= last_date).\
								group_by(Measurement.date).\
								order_by(Measurement.date.desc()).all()

	temp_over_1_year_list = []

	for temp in temp_over_1_year:
		temp_over_1_year_list.append({"date": temp[1], "temp": temp[0]})

	return jsonify(temp_over_1_year_list)

####   MIN, AVG, MAX TEMP    #######################
@app.route("/api/v1.0/<start>")
def min_avg_max_start(start):
	start_date = dt.datetime.strptime(start,'%Y-%m-%d').date()
	end_date = session.query(Measurement.date).group_by(Measurement.date).order_by(Measurement.date.desc()).first()
	end_date = dt.datetime.strptime(end_date[0],'%Y-%m-%d').date()

	return jsonify(calc_temp(start_date, end_date))

@app.route("/api/v1.0/<start>/<end>")
def min_avg_max_start_end(start, end):
	start_date = dt.datetime.strptime(start,'%Y-%m-%d').date()
	end_date = dt.datetime.strptime(end,'%Y-%m-%d').date()

	return jsonify(calc_temp(start_date, end_date))


def calc_temp(start, end):
	last_date = session.query(Measurement.date).group_by(Measurement.date).order_by(Measurement.date.desc()).first()
	last_date = dt.datetime.strptime(last_date[0],'%Y-%m-%d').date()

	# check if start < end
	if start > end:
		tempo = end
		end = start
		start = tempo
	# check outbound
	if end > last_date:
	 	end = last_date

	temp_over_period = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
								filter(Measurement.date >= start).\
								filter(Measurement.date <= end).\
								all()

	return [{"min_temp": temp_over_period[0][0], "avg_temp": temp_over_period[0][1], "max_temp": temp_over_period[0][2]}]


@app.route("/api/v1.0")
def index():
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
