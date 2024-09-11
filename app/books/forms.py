from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired, Length



class bookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(2, 40)])
    image= FileField("Image", validators=[DataRequired()]) 
    pages = IntegerField("Number of Pages")
    description = StringField("Description", validators=[DataRequired()]) 
    submit = SubmitField("Save new Student")

   