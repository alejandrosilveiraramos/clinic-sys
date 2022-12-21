#class Admin(db.Model):
    
#    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#   password = db.Column(db.String(64), nullable=False)
#    email = db.Column(db.String(64), nullable=False)
#    cpf = db.Column(db.String(14), nullable=False)
#    position = db.Column(db.String(64), nullable=False)

#    def __repr__(self):
#        return '<Name %r>' % self.name
    
#class Person(db.Model):
#    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#    name = db.Column(db.String(64), nullable=False)
#    email = db.Column(db.String(64), nullable=False)
#    cpf = db.Column(db.String(14), nullable=False)

#    def __repr__(self):
#        return '<Name %r>' % self.name