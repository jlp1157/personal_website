from flask import Blueprint, render_template, flash, redirect, request, url_for


data = Blueprint('data', __name__,
                        template_folder='templates')

@data.route('/projects')
def projects():
    return render_template('projects.html')