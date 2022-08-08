from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Minute
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/home')
def Main():
    return render_template("home.html", user=current_user)

    
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        dates = request.form.get('minute.dates')
        topic = request.form.get('minute.topic')
        attendees = request.form.get('minute.attendees')
        raised_by = request.form.get('minute.raised_by')
        action = request.form.get('minute.action')
        actionedby = request.form.get('minute.to_be_actionedby')
        info = request.form.get('minute.info')
        date_of_comp = request.form.get('minute.date_of_comp')
        new_minute = Minute(dates=dates,topic=topic,attendees=attendees,raised_by=raised_by,
        action=action,to_be_actionedby=actionedby,
        info=info, date_of_comp=date_of_comp, user_id=current_user.id)
        db.session.add(new_minute)
        db.session.commit()
        flash('Note added!', category='success')

    return render_template("minute_taker.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Minute.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

 