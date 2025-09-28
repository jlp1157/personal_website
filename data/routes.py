from flask import Blueprint, render_template, flash, redirect, request, url_for


data = Blueprint('data', __name__,
                        template_folder='templates')

@data.route('/projects')
def projects():
    return render_template('static.html')

@data.route('/projects/progress')
def progress():
    return render_template('static.html')

@data.route('/aboutme')
def projects():
    return render_template('static.html')