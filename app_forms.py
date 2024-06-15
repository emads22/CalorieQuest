import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange, InputRequired, Length, Regexp, ValidationError


# class CaloriesForm(FlaskForm):

#     gender = StringField(label="Gender:",
#                           validators=[DataRequired(message="Gender is required."),
#                                       Length(
#                                           min=4, max=6, message="Gender must be between 4 and 6 characters."),
#                                       Regexp(regex='^(male|female)$',
#                                              flags=re.IGNORECASE,  # Using re.IGNORECASE flag (2)
#                                              message="Gender must be 'male' or 'female' only.")],
#                           render_kw={"placeholder": "e.g., Female"},
#                           default='Male')

#     weight = DecimalField(label="Weight:",
#                           validators=[InputRequired(message="Height is required."),
#                                       NumberRange(min=60, message="Height must be a positive number.")],
#                           render_kw={"placeholder": "e.g., 170"},
#                           default=65.5)

#     height = DecimalField(label="Height:",
#                           validators=[InputRequired(message="Weight is required."),
#                                       NumberRange(min=50, message="Weight must be a positive number.")],
#                           render_kw={"placeholder": "e.g., 60"},
#                           default=170)

#     age = IntegerField(label="Age:",
#                        validators=[InputRequired(message="Age is required."),
#                                    NumberRange(min=18, message="Age must be a positive number.")],
#                        render_kw={"placeholder": "e.g., 30"},
#                        default=33)


#     country = StringField(label="Country:",
#                           validators=[DataRequired(message="Country is required."),
#                                       Length(
#                                           min=3, max=20, message="Country must be between 3 and 20 characters."),
#                                       Regexp(regex='^ *[a-zA-Z]+ *$',  # 0 or more space char before and after
#                                              message="Country can only contain letters.")],
#                           render_kw={"placeholder": "e.g., USA"},
#                           default='Lebanon')

#     city = StringField(label="City:",
#                        validators=[DataRequired(message="City is required."),
#                                    Length(
#                                        min=3, max=20, message="City must be between 3 and 20 characters."),
#                                    Regexp(regex='^ *[a-zA-Z]+ *$',  # 0 or more space char before and after
#                                           message="City can only contain letters.")],
#                        render_kw={"placeholder": "e.g., Washington"},
#                        default='Beirut')

#     submit = SubmitField("Calculate")


class CaloriesForm(FlaskForm):

    gender = SelectField(label="Gender:",
                         choices=[('male', 'Male'), ('female', 'Female')],
                         validators=[DataRequired(
                             message="Gender is required.")],
                         default='male')

    weight = DecimalField(label="Weight (kg):",
                          validators=[DataRequired(message="Weight is required."),
                                      NumberRange(min=0, message="Weight must be a positive number.")],
                          default=70.0)

    height = DecimalField(label="Height (cm):",
                          validators=[DataRequired(message="Height is required."),
                                      NumberRange(min=0, message="Height must be a positive number.")],
                          default=170.0)

    age = IntegerField(label="Age:",
                       validators=[DataRequired(message="Age is required."),
                                   NumberRange(min=0, message="Age must be a positive number.")],
                       default=25)

    country = SelectField(label="Country:",
                          choices=[('USA', 'USA'), ('Canada', 'Canada'),
                                   ('UK', 'UK'), ('Australia', 'Australia')],
                          validators=[DataRequired(
                              message="Country is required.")],
                          default='USA')

    city = SelectField(label="City:",
                       choices=[('New York', 'New York'), ('Los Angeles', 'Los Angeles'),
                                ('London', 'London'), ('Sydney', 'Sydney')],
                       validators=[DataRequired(message="City is required.")],
                       default='New York')

    submit = SubmitField("Calculate", render_kw={"class": "calculate-btn"})
