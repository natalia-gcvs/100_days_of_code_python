from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import random

#API documentation link
# https://documenter.getpostman.com/view/26871285/2s93XvWQgB

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    # db.create_all()

    @app.route("/")
    def home():
        return render_template("index.html")


    ## HTTP GET - Read Record
    @app.route("/random")
    def get_random_cafe():
        random_cafe = db.session.query(Cafe).order_by(func.random()).first()
        print(f'teste: {jsonify(cafe=random_cafe.to_dict())}')
        return jsonify(cafe=random_cafe.to_dict())

    ## HTTP GET - Read Record
    @app.route("/all")
    def get_all_cafes():
        all_cafes = db.session.query(Cafe).all()
        return jsonify(cafe=[cafe.to_dict() for cafe in all_cafes])

    ## HTTP GET - Read Record
    @app.route("/search")
    def find_cafe():
        cafes = Cafe.query.filter_by(location=request.args.get('loc')).all()
        if cafes:
            return jsonify(cafe=[cafe.to_dict() for cafe in cafes])
        return jsonify(error={'Not found': "Sorry we don't have a cafe at that location"})


    ## HTTP POST - Create Record
    @app.route("/add", methods=['POST'])
    def add_cafe():
        fields = ['name', 'map_url', 'img_url', 'location', 'seats', 'has_toilet',
                  'has_wifi', 'has_sockets', 'can_take_calls', 'coffee_price']
        cafe_input = {field: request.args.get(field) for field in fields}
        new_cafe = Cafe(
            name=request.args.get('name'),
            map_url=request.args.get('map_url'),
            img_url=request.args.get('img_url'),
            location=request.args.get('location'),
            has_toilet=bool(request.args.get('has_toilet')),
            has_wifi=bool(request.args.get('has_wifi')),
            has_sockets=bool(request.args.get('has_sockets')),
            can_take_calls=bool(request.args.get('can_take_calls')),
            seats=request.args.get('seats'),
            coffee_price=request.args.get('coffee_price'),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={'sucess': 'Successfully added the new cafe.'})

    ## HTTP PUT/PATCH - Update Record
    @app.route("/update-price", methods=['PATCH'])
    def update_price():
        cafe_id = request.args.get('id')
        cafe_to_update = Cafe.query.get(cafe_id)
        if cafe_to_update:
            coffee_price = request.args.get('new_price')
            cafe_to_update.coffee_price = coffee_price
            db.session.commit()
            return jsonify(response={'Success': 'Successfully updated price.'})
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


    ## HTTP DELETE - Delete Record
    @app.route("/delete-cafe", methods=['DELETE'])
    def delete_cafe():
        api_key = request.args.get('api_key')
        api_key_list = ['321654987', '22332151484']
        if api_key in api_key_list:
            cafe_id = request.args.get('id')
            cafe_to_delete = Cafe.query.get(cafe_id)
            if cafe_to_delete:
                db.session.delete(cafe_to_delete)
                db.session.commit()
                return jsonify(response={'Success': 'Successfully deleted.'})
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


    if __name__ == '__main__':
        app.run(debug=True)
