from flask import Blueprint, jsonify
from flask import request
from services.weather_api import get_weather
from app.models import Rilevazione
from app.extensions import db

main_bp=Blueprint('main_bp',__name__)

@main_bp.route('/abc',)
def weather():
    city=request.args.get('city','milano')
    data= get_weather(city)

    rilevazione=Rilevazione(
        id=1,
        citta=data['city'],
        tempo=data['description']
    )

    db.session.add(rilevazione)
    db.session.commit()
    
    return jsonify(data)

