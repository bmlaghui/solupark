from bson import json_util
from flask import Flask, Response, request, render_template, jsonify
import pymongo
import json
from bson.objectid import ObjectId
app = Flask(__name__)


try:
    mongo = pymongo.MongoClient(
        host ="localhost",
        port=27017,
        serverSelectionTimeoutMS = 1000
    )
    db = mongo.solupark
    mongo.server_info()
except:
    print("ERREUR-Impossibe de se connecter à la BDD")


def remove_key(d):
    if isinstance(d, dict):
        if 'badKey' in d:
            del d['badKey']
        for v in d.values():
            remove_key(v)
    elif isinstance(d, list):
        for v in d:
            remove_key(v)



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/admin')
def admin_dashbord():

    return render_template('dashboard.html', name='dashbord')

@app.route('/admin/users')
def admin_users():
    users = get_some_users().get_json();
    data = remove_key(users)

    return render_template('dashboard-booking.html', data = users)


@app.route('/admin/parkings')
def admin_parkings():
    parkings = get_some_parkings().get_json();
    data = remove_key(parkings)

    return render_template('dashboard-my-listings.html', data = parkings)

@app.route('/users', methods=["GET"])
def get_some_users():
    try:
        data = list(db.users.find())
        for user in data:
            user["_id"] = str(user["_id"])
        return Response(
            response=json.dumps(data),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "cannot get users"}),
            status=500,
            mimetype="application/json"
        )

@app.route('/users', methods=["POST"])
def create_user():
        try:
            user = {"username": "test@gmail.com",
                    "password": "test",
                    "telephone": "0707070707",
                    "codePostal": "757575",
                    "ville": "Paris 11eme",
                    "No": "99",
                    "rue": "street",
                    "complemetAdresse": "adress complement"}
            dbResponse = db.users.insert_one(user)
            for attr in dir(dbResponse):
                print(attr)
            return Response(
                response=json.dumps({"message": "user created", "id": f"{dbResponse.inserted_id}"}),
                status=200,
                mimetype="application/json"
            )
        except Exception as ex:
            print(ex)

@app.route('/users/<id>', methods=["DELETE"])
def delete_user(id):
    try:
        dbResponse = db.users.delete_one(
            {"_id": ObjectId(id)}
        )
        if dbResponse.deleted_count >= 1:
            return Response(
                response=json.dumps({"message": "user deleted"}),
                status=200,
                mimetype="application/json"
            )
        else:
            return Response(
                response=json.dumps({"message": "no user to delete"}),
                status=200,
                mimetype="application/json"
            )

    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "cannot delete user"}),
            status=500,
            mimetype="application/json"
        )

@app.route('/users/<id>', methods=["PATCH"])
def update_user(id):
    try:
        dbResponse = db.users.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"username": request.form["username"]}}
        )
        if dbResponse.modified_count >= 1:
            return Response(
                response=json.dumps({"message": "user updated"}),
                status=200,
                mimetype="application/json"
            )
        else:
            return Response(
                response=json.dumps({"message": "Nothing to update"}),
                status=200,
                mimetype="application/json"
            )


    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "cannot update user"}),
            status=500,
            mimetype="application/json"
        )


@app.route('/parkings', methods=["GET"])
def get_some_parkings():
    try:
        data = list(db.parking.find())
        for parking in data:
            parking["_id"] = str(parking["_id"])
        return Response(
            response=json_util.dumps(data),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "cannot get parkings"}),
            status=500,
            mimetype="application/json"
        )

@app.route('/parking', methods=["GET"])
def get_parkings():
    try:
        limit = int(request.args['limit'])
        offset = int(request.args['offset'])

        starting_id = db.parking.find().sort('_id', 1)
        last_id = starting_id[offset]['_id']

        data = list(db.parking.find({'_id' : {'$gte' : last_id}}).sort('_id', 1).limit(limit))
        output = []

        for parking in data:

            output.append({'nom' : parking['nom'], '_id': str(parking['_id']), 'emplacement' : parking['emplacement'] , 'surface': parking['surface'], 'hauteur': parking['hauteur'],'niveau':parking['niveau'], 'nro': parking['nro'], 'rue': parking['rue'], 'codePostal': parking['codePostal'], 'ville': parking['ville'], 'latitude': parking['latitude'], 'longitude': parking['longitude'], 'couvert': parking['couvert'], 'charge': parking['charge'], 'charge': parking['charge'], 'charge': parking['charge'], 'charge': parking['disponibiltes'], 'images': parking['images'], 'ratings': parking['ratings']
 })

        next_url = '/parking?limit=' + str(limit) + '&offset=' + str(limit + offset)
        previous_url = '/parking?limit=' + str(limit) + '&offset=' + str(limit - offset)

        return jsonify({ 'result' : output, 'next_url' : next_url, 'previous_url' : previous_url})
    except Exception as ex:
        print(ex)
        return Response(
        response=json.dumps({"message": "cannot get parkings"}),
        status=500,
        mimetype="application/json"
            )
@app.route('/admin/parkings-listing')
def admin_parking():
    parkings = get_parkings().get_json();
    data = remove_key(parkings)

    return render_template('parkings.html', data = parkings)
if __name__ == '__main__':
    app.run()
