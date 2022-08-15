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
     
        if len(name) > 20:
            flash('Meeting name can only be 20 characters long.', category='error')
        else:
             new_meeting = Meeting(name=name, date=date, user_id=current_user.id)
             db.session.add(new_meeting)
             db.session.commit()
             flash('Meeting added!', category='success')
             return redirect('/')
   
    return render_template("minute_taker.html", user=current_user)
    
@views.route('/min/<int:id>', methods=['GET', 'POST'])
@login_required

def minute(id):
    task = Meeting.query.get_or_404(id)
    meeting = Meeting.query.filter_by(id=id).first()
    current_meeting = Meeting.query.filter_by(id=id).first()
     #need to get table for each meeting sorted
    user_id = current_user.id
    id = current_user.id
    if id == user_id and meeting == current_meeting:
        if request.method == 'POST':
            dates = request.form.get('minute.dates')
            topic = request.form.get('minute.topic')
            attendees = request.form.get('minute.attendees')
            raised_by = request.form.get('minute.raised_by')
            action = request.form.get('minute.action')
            actionedby = request.form.get('minute.to_be_actionedby')
            info = request.form.get('minute.info')
            date_of_comp = request.form.get('minute.date_of_comp')
            if len(topic) > 20:
                flash('Topic can only be 20 characters long.', category='error')
            else:    
                new_minute = Minute(dates=dates,topic=topic,attendees=attendees,raised_by=raised_by,
                action=action,to_be_actionedby=actionedby,
                info=info, date_of_comp=date_of_comp, user_id=current_user.id)
                db.session.add(new_minute)
                db.session.commit()
                flash('Note added!', category='success')
    return render_template("min.html", user=current_user, task=task, meeting=current_meeting)
    

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

 