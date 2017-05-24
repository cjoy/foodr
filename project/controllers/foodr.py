# -*- coding: utf-8 -*-
import os, json, random
import Restaurant
from project import app
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

# Global Data Stores
Restaurants = []

# load restaruants from static json data using the restaraunts model
local_data = os.path.join(app.static_folder, 'data/restaurant.json')
with open(local_data) as f:
    lines = json.load(f)
    data = lines["Restaurants"]

    for r in data:
        Restaurants.append(Restaurant.Restaurant(r['name'], r['lng'], r['lat'], r['rating'], r['vicinity'], r['type'], r['cuisine'], str(r['alcohol']).lower(), str(r['wheelchair']).lower(), str(r['wifi']).lower()))


@app.route('/')
def start():
    query = request.args.get('q')
    return render_template('foodr/index.html', query=query, restaurants=Restaurants)

@app.route('/search')
def search():
    query = request.args.get('q')
    # linear search: append restaruants that contains the query
    results = []
    count = 0
    if query != "":
        querys = query.split(" ")
        # iterate over restaurant elements
        for q in querys:
            for r in Restaurants:
                # RESULT RANKING CONDITIONS PRIORITY (TODO: come up with a better way)
                if (q.lower() in r.name.lower()) and (q in r.cuisine) and (q.lower() in r.vicinity.lower()):
                    count = count + 1
                    results.insert(0, r)
                elif ((q.lower() in r.name.lower()) and (q.lower() in r.vicinity.lower())) or (q in r.cuisine):
                    # prevent duplicated results
                    if r not in results:
                        count = count + 1
                        results.append(r)
                elif ((q.lower() in r.name.lower()) and (q in r.cuisine)) or (q.lower() in r.vicinity.lower()):
                    if r not in results:
                        count = count + 1
                        results.append(r)
                elif (q.lower() in r.name.lower()) or ((q in r.cuisine) and (q.lower() in r.vicinity.lower())):
                    if r not in results:
                        count = count + 1
                        results.append(r)
                elif (q.lower() in r.name.lower()) or (q in r.cuisine) or (q.lower() in r.vicinity.lower()):
                    if r not in results:
                        count = count + 1
                        results.append(r)

    return render_template('foodr/search.html', query=query, results=results, count=count)

@app.route('/advsearch')
def advSearch():
    queryCuisine = request.args.get('c')
    queryVicinity = request.args.get('v')
    queryRating = request.args.get('r')
    queryType = request.args.get('t')
    queryAlcohol = request.args.get('a')
    queryWheelchair = request.args.get('wh')
    queryWifi = request.args.get("wi")

    results = []
    results.append([])
    for r in Restaurants:
        count = -1
        if (queryCuisine in r.cuisine):
            count = count + 1
        if (queryVicinity > r.vicinity):
            count = count + 1
        if (queryRating < r.rating):
            count = count + 1
        if (queryType == r.type):
            count = count + 1
        if (queryAlcohol == r.alcohol):
            count = count + 1
        if (queryWheelchair == r.wheelchair):
            count = count + 1
        if (queryWifi == r.wifi):
            count = count + 1
        if(count > -1):
            results[count].append(r)
    return render_template('foodr/advsearch.html')

@app.route('/restaurants/')
def restaurants():
    query = request.args.get('q')
    return render_template('foodr/index.html', query=query, restaurants=Restaurants)

@app.route('/deals/')
def deals():
    query = request.args.get('q')
    return render_template('foodr/deals.html', query=query)

@app.route('/saved/')
def saved():
    query = request.args.get('q')
    return render_template('foodr/saved.html', query=query)

@app.route('/saved/restaurants/')
def saved_restaurants():
    query = request.args.get('q')
    return render_template('foodr/saved_restaurants.html', query=query)

@app.route('/saved/deals/')
def saved_deals():
    query = request.args.get('q')
    return render_template('foodr/saved_deals.html', query=query)


# @app.route('/print', methods=['GET', 'POST'])
# def printer():
#     form = CreateForm(request.form)
#     if request.method == 'POST' and form.validate():
#         from project.models.Printer import Printer
#         printer = Printer()
#         printer.show_string(form.text.data)
#         return render_template('printer/index.html')
#     return render_template('printer/print.html', form=form)
