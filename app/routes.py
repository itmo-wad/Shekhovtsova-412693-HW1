from flask import render_template,redirect,url_for,send_from_directory
from app import server

@server.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@server.route('/')
def index():
    return redirect(url_for('profile'))

@server.route('/profile')
def profile():
    name="Irina Shekhovtsova"
    return render_template('index.html',name=name)