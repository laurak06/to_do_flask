from database.engine import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='In process')
    created_at = db.Column(db.String(50), nullable=False)

