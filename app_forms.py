from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange, InputRequired, Length, Regexp, ValidationError
from datetime import datetime


class CaloriesForm(FlaskForm):

    weight = DecimalField(label="Weight:", 
                       validators=[InputRequired(message="Height is required."),
                                   NumberRange(min=60, message="Height must be a positive number.")],
                       render_kw={"placeholder": "e.g., 170"})
    
    height= DecimalField(label="Height:", 
                       validators=[InputRequired(message="Weight is required."),
                                    NumberRange(min=50, message="Weight must be a positive number.")],
                       render_kw={"placeholder": "e.g., 60"})
    
    age = IntegerField(label="Age:", 
                       validators=[InputRequired(message="Age is required."),
                                    NumberRange(min=18, message="Age must be a positive number.")],
                       render_kw={"placeholder": "e.g., 30"})
    
    city = StringField(label="City:", 
                       validators=[DataRequired(message="City is required."),
                                    Length(min=3, max=20, message="City must be between 3 and 20 characters."),
                                    Regexp(regex='^ *[a-zA-Z]+ *$',  # 0 or more space char before and after
                                           message="City can only contain letters.")],
                       render_kw={"placeholder": "e.g., Washington"})

    country = SelectField(label="Country:",
                          choices=[('value1', 'Label 1'), ('value2', 'Label 2'), ('value3', 'Label 3')],
                          validators=[DataRequired(message="Country is required.")],
                          render_kw={"placeholder": "e.g., USA"})

    submit = SubmitField("Calculate")