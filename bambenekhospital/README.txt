# Project     :		Access Control Models on Professional Environments
# Designed by :		Doruk Tan Ozdogan
# Date        :		May 3, 2018
# Description :		A very simple website designed to mimic the functionality of a Hospital's
#					Patient admission and Control system. Role Based Access Control is used
#					and tested on the project.
# Presentation :	https://www.youtube.com/watch?v=Ml4b95Z-n5M&feature=youtu.be
# University of Illinois, Urabana Champaign
# Cs460 - Security Laboratory Final Project
# Designed on Django Web Framework
# Requirements
# -Python 3, pip3, Django
# My Versions during production : Python 3.6.5, pip 10.0.1, Django 2.0.4


### -- SOURCES -- ####
# The project was designed with the help of following educational Documentations:
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django
# https://docs.djangoproject.com/en/2.0/
### -- SOURCES -- ###


### -- SETUP -- ###
#   Install requirements
# - Ubuntu:$ sudo apt-get install python3-pip
#	optional virtualenvironment setup:$ sudo pip3 install virtualenvwrapper
#	inside .bashrc add
#	export WORKON_HOME=$HOME/.virtualenvs
#	export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
#	export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
#	export PROJECT_HOME=$HOME/Devel
#	source /usr/local/bin/virtualenvwrapper.sh
#	on terminal : $ source ~/.bashrc
#	$ mkvitualenv my_django_environment
#	$ pip3 install django
# - Windows 10: ttps://www.python.org/downloads/ download python 3
#	$ pip3 install virtualenvwrapper-win
#	$ mkvirtualenv my_django_environment
#	$ pip3 install django
### -- RUN THE PROJECT -- ###
#	inside bambenekhospital directoryt hat contains manage.py, do the following on terminal
#	$ python3 manage.py makemigrations ( py -3 manage.py makemigrations # if on windows 10)
#	$ python3 manage.py migrate
#	$ python3 manage.py createsuperuser
#	fill in the info for admin/root account on project
#	$ python3 manage.py runserver
#   Project running on localhost you can view it at : 127.0.0.1:8000
### -- CUSTOMIZE and TEST THE PROJECT -- ###
#	You can add new roles(groups), users, permissions, patients, doctors, titles, gender
#	on the highly intuitive Django admin GUI at 127.0.0.1:8000/admin
#	log in as superuser
#	Special Permissions:
#	-the Permission "set patient as assigned" on any user together with staff status 
#	will enable that user to see "All Patients Assigned" Tab on project.
#	-the Permission "User can treat patient" on any user together with staff status
# 	will enable that user to see "My Patients" Tab on project.
#	-the Permission "He is the boss" on any user together with staff status
#	will enable that user to see "BOSS" and related Tabs on project.