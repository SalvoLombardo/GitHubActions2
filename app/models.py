from app.extensions import db

class Rilevazione(db.Model):
    __tablename__='rilevazioni'
    id=db.Column(db.Integer, primary_key=True)
    citta=db.Column(db.String, nullable=False)
    tempo=db.Column(db.String, nullable=False)