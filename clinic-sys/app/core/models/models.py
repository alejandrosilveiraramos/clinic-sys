from main import db

class Admin(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    position = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
    
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

class Reports(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idPerson = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(128), nullable=False)
    date_time = db.Column(db.date, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name