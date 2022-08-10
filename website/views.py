from tkinter import Button
from tkinter.tix import Form
from flask import Blueprint, redirect, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from numpy import delete
from .models import Meeting, Minute, User
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/home')
def Main():
    return render_template("home.html", user=current_user)
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

   
    if request.method == 'POST' :
        
        name = request.form.get('meeting.name')
        date = request.form.get('meeting.date')
        new_meeting = Meeting(name=name, date=date, user_id=current_user.id)
        db.session.add(new_meeting)
        db.session.commit()
        flash('Note added!', category='success')
        return redirect('/')
    else:    
        meets = Meeting.query.order_by(Meeting.id).all()
    return render_template("minute_taker.html", user=current_user, meets=meets)
    
@views.route('/min/<int:id>', methods=['GET', 'POST'])
@login_required
def minute(id):
    task = Meeting.query.get_or_404(id)
    meetings_Id = request.get_data('meeting.id') #need to get table for each meeting sorted
    user_id = current_user.id
    id = current_user.id
    if id == user_id: 
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
            db.session.add(new_minute, task)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("min.html", user=current_user, task=task )

@views.route('/delete/<int:id>')
@login_required
def delete(id):
    
    task = Meeting.query.get_or_404(id)
    user_id = current_user.id
    id = current_user.id
    if id == user_id:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')


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

 