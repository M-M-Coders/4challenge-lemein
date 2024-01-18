#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)


class HomeResource(Resource):
    def get(self):
        response_data = {
            "message": "Welcome to the Superhero Universe!",
            "description": "Embark on an epic journey through a world filled with extraordinary beings, where courage, strength, and justice collide."
        }
        response = make_response(
            jsonify(response_data),
            200
        )
        return response


api.add_resource(HomeResource, '/')


class HeroesResource(Resource):
    def get(self):
        heroes = []
        for hero in Hero.query.all():
            hero_dict = {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name,
                "created_at": hero.created_at,
                "updated_at":hero.updated_at
            }
            heroes.append(hero_dict)
        response = make_response(
            jsonify(heroes),
            200
        )
        return response


api.add_resource(HeroesResource, '/heroes')

class HeroResource(Resource):
    def get(self, id):
        hero = Hero.query.filter_by(id=id).first()
        if hero:
            hero_dict = {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name,
                "powers": [
                    {
                        "id": hero_power.power.id,
                        "name": hero_power.power.name,
                        "description": hero_power.power.description
                    } for hero_power in hero.powers
                ]
            }
            response = make_response(
                jsonify(hero_dict),
                200
            )
        else:
            response = make_response(
                jsonify({"error": "Hero not found"}),
                404
            )

        return response
    
api.add_resource(HeroResource, '/heroes/<int:id>')

class PowersResource(Resource):
    def get(self):
        powers = []
        for power in Power.query.all():
            power_dict = {
                "id": power.id,
                "name": power.name,
                "description": power.description
            }
            powers.append(power_dict)
        response = make_response(
            jsonify(powers),
            200
        )
        return response


api.add_resource(PowersResource, '/powers')

class PowerResource(Resource):
    def get(self, id):
        power = Power.query.get_or_404(id)

        power_dict = {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }

        response = make_response(
            jsonify(power_dict),
            200
        )

        return response


api.add_resource(PowerResource, '/powers/<int:id>')

class UpdatePowerResource(Resource):
    def patch(self, id):
        power = Power.query.get(id)

        if power:
            data = request.get_json()
            if 'description' in data:
                power.description = data['description']
                db.session.commit()
                response = make_response(
                    jsonify({
                        "id": power.id,
                        "name": power.name,
                        "description": power.description
                    }),
                    200
                )
            else:
                response = make_response(
                    jsonify({"errors": ["No valid fields to update"]}),
                    400
                )
        else:
            response = make_response(
                jsonify({"error": "Power not found"}),
                404
            )

        return response


api.add_resource(UpdatePowerResource, '/powers/<int:id>')

class HeroPowersResource(Resource):
    def post(self):
        data = request.get_json()

        # Validate input data - You may need to add further validation based on your requirements.

        hero = Hero.query.get(data['hero_id'])
        power = Power.query.get(data['power_id'])

        if hero and power:
            hero_power = HeroPower(
                hero=hero,
                power=power,
                strength=data['strength']
            )

            db.session.add(hero_power)
            db.session.commit()

            # Get the updated hero data
            updated_hero = Hero.query.get(hero.id)
            hero_dict = {
                "id": updated_hero.id,
                "name": updated_hero.name,
                "super_name": updated_hero.super_name,
                "powers": [
                    {
                        "id": hero_power.power.id,
                        "name": hero_power.power.name,
                        "description": hero_power.power.description
                    } for hero_power in updated_hero.powers
                ]
            }

            response = make_response(
                jsonify(hero_dict),
                201  # 201 Created
            )
        else:
            response = make_response(
                jsonify({"errors": ["Invalid hero_id or power_id"]}),
                400  # 400 Bad Request
            )

        return response


api.add_resource(HeroPowersResource, '/hero_powers')

if __name__ == '__main__':
    app.run(port=5555, debug=True)