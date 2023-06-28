from application import app,db
from application import routes
from flask import jsonify,request
from flask import render_template, redirect, url_for,flash, get_flashed_messages
from application.models import Menu
from application.forms import UserDataForm, UpdateUserDataForm


import json



@app.route("/")

def index():
    entries = Menu.query.order_by(Menu.votes.asc()).all()
    entry_list = []
    form = UserDataForm()
    for entry in entries:
        entry_list.append(format_menu(entry))
    return render_template( "index.html",entries=entry_list, form=form)

def format_menu(entry):
    return {
        "id":entry.id,
        "item": entry.item,
        "votes": entry.votes
    }


@app.route("/add_menu", methods=["POST", "GET"])

def add_menu():
    form = UserDataForm()
    if form.validate_on_submit():
        entry = Menu(item=form.item.data, votes=form.votes.data)
        db.session.add(entry)
        db.session.commit()
        flash(f"{form.item.data} has been added to the menu", "success")
        return redirect(url_for("index"))
    return render_template("add.html", title="Add menu", form=form, )

@app.route("/delete_menu/<int:id>")
def delete_menu(id):
    delete_menu = Menu.query.get_or_404(int(id))
    print(delete_menu)
    db.session.delete(delete_menu)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for("index"))

@app.route("/update_menu/<int:id>", methods=["POST", "GET"])

def update_menu(id):
    form =  UpdateUserDataForm()
    if form.validate_on_submit():
        entry = Menu.query.get_or_404(int(id))

        if "item" in form.data:
           entry.item = form.item.data
        if "votes" in form.data:
           entry.votes = form.votes.data
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("update.html", title="update menu", form=form )

@app.route("/dashboard")
def dashboard():
    menu_votes = db.session.query(Menu.id, Menu.item, db.func.sum(Menu.votes)).group_by(Menu.item, Menu.id).order_by(Menu.item, Menu.id).all()

    menu_votes_chart = []
    for menu in menu_votes:
        menu_dict = {'id': menu[0], 'item': menu[1], 'votes': menu[2]}
        menu_votes_chart.append(menu_dict)

    return render_template("dashboard.html", menu_votes_chart=menu_votes_chart)







