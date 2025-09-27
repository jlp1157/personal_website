from flask import Blueprint, render_template, flash, redirect, request, url_for


data = Blueprint('data', __name__,
                        template_folder='templates')

@data.route('/projects')
def projects():
    return render_template('projects.html')

@data.route('projects/progress')
def progress():
    return render_template('progress.html')

@data.route('/aboutme')
def projects():
    return render_template('aboutme.html')