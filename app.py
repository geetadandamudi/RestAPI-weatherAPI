from flask import Flask, request, make_response, jsonify, abort
from flask_restful import Resource, Api
from sqlalchemy import create_engine

engine = create_engine('sqlite:///cloudproj.db')

app = Flask(__name__)
api = Api(app)


class daily_data(Resource):
    def get(self):
        connect = engine.connect()
        query = connect.execute("select Date from daily")
        data = {'Date': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        if data == {"Date": []}:
            return "Data not found"
        else:
            return data

class daily_date(Resource):
    def get(self, date):
        connect = engine.connect()
        query = connect.execute("select * from daily where Date='%s'"%date)
        data = {'Date': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        if data == {"Date": []}:
            return "Data not found"
        else:
            return data

@app.route('/historical/delete/<string:date>', methods=['GET','DELETE'])
def delete(date):
        connect = engine.connect()
        query = connect.execute("delete from daily where Date='%s'"%date)
        return make_response(jsonify({'Date deleted for': date}), 200)

class Insert(Resource):
    def get(self, date, Tmax, Tmin):
        connect = engine.connect()
        query = connect.execute("insert into daily(Date, Tmax, Tmin) values (?, ?, ?)",(date,Tmax,Tmin))
        return make_response(jsonify({'Date': date, 'Tmax': Tmax, 'Tmin': Tmin}), 201)

class future(Resource):
  def get(self, date):
    connect = engine.connect()
    date1 = int(date)
    end_date = date1 + 7
    query = connect.execute("SELECT @Date := @Date + 1 Date, FLOOR(RANDOM()*(TMAX*2)), FLOOR(RANDOM()*(TMIN*2)) FROM daily, (SELECT @Date := ?) dummy ORDER BY Date limit 7", (date1))
    data = {'Date': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
    if data == {"Date": []}:
        return "Data not found" 
    else:
        return data

api.add_resource(daily_data, '/historical/')
api.add_resource(daily_date, '/historical/<string:date>')
api.add_resource(Insert, '/historical/<string:date>,<string:Tmax>,<string:Tmin>')
api.add_resource(Future, '/historical/forecast/<string:date>')
if __name__ == '__main__':
     app.run()

