from flask import Blueprint, jsonify, request
from models.food_group import Food_Group

api = Blueprint('food_group_api', __name__)

@api.route('/food_groups', methods=['GET'])
def list_food_group():
    
    food_groups = Food_Group.query.all()
    food_groups = list(map(lambda food_group: food_group.serialize(), food_groups))

    return jsonify(food_groups), 200

@api.route('/food_groups', methods=['POST'])
def add_food_group():

    food_group = Food_Group()
    food_group.name = data['name']
    food_group.description = data['description']
    food_group.save()
    return jsonify({ "message": "POST Food group"}), 200

@api.route('/food_groups/{id}', methods=['PUT'])
def update_food_group():



    return jsonify({ "message": "PUT Food group"}), 200

@api.route('/food_groups/{id}', methods=['DELETE'])
def remove_food_group():

    food_group = Food_Group().query.get(id)
    food_group.delete()

    return jsonify({ "message": "Delete Food group"}), 200