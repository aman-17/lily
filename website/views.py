from os import abort
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, send_file
from flask_login import login_required, current_user
from flask.globals import session
import json
from flask import flash, render_template, redirect, url_for, Response, request
from flask_login import current_user, login_user, login_required, logout_user
import os
import time
import ffmpy
import time
import os
import math


views = Blueprint('views',__name__,template_folder="templates/",static_folder="../static/")# static_url_path="/static")

@views.route('/', methods=['GET','POST'])
# @login_required
def mainpage():
    
    return render_template("index.html", user=current_user) 

@views.route('/enterdetails', methods=['GET', 'POST'])
#@login_is_required
def enterdetails():
        

    return render_template("enterdetails.html", user=current_user)

@views.route('/login', methods=['GET','POST'])
# @login_required
def login():
    
    return render_template("login.html", user=current_user)   

@views.route('/about', methods=['GET','POST'])
# @login_required
def about():
      
    return render_template("about.html", user=current_user)