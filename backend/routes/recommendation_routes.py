from flask import Blueprint, request, jsonify
from models.recommendation_model import get_recommendations

rec_bp = Blueprint('rec_bp', __name__)

@rec_bp.route('/recommend', methods=['POST'])
def recommend():
    # Get user preferences from request
    data = request.get_json()
    # Generate recommendations
    recommendations = get_recommendations(data)
    return jsonify({'recommendations': recommendations})

@rec_bp.route('/rate', methods=['POST'])
def rate():
    # Get rating data from user
    data = request.get_json()
    # Update model with new rating
    # (Implement the logic to update the model)
    return jsonify({'message': 'Rating received'})
