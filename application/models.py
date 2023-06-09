from application import app,db 

app.app_context().push()
db.create_all()

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    votes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"my menu items are {self.item} {self.votes}"

    def __init__(self, item, votes):
        self.item = item
        self.votes = votes

     

with app.app_context():
    db.create_all()

   

    print("Item added to the database.")

if __name__ == '__main__':
    app.run()



