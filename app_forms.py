import pandas as pd
from flask_wtf import FlaskForm
from wtforms import SubmitField, DecimalField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange
from constants import COUNTRIES_FILE


class CalorieForm(FlaskForm):

    gender = SelectField(label="Gender:",
                         choices=[('', 'Select gender'),
                                  ('female', 'Female'), ('male', 'Male')],
                         validators=[DataRequired(
                             message="Gender is required.")])

    weight = DecimalField(label="Weight (kg):",
                          validators=[DataRequired(message="Weight is required."),
                                      NumberRange(min=0, message="Weight must be a positive number.")],
                          render_kw={"placeholder": "Enter weight in kilograms"})

    height = DecimalField(label="Height (cm):",
                          validators=[DataRequired(message="Height is required."),
                                      NumberRange(min=0, message="Height must be a positive number.")],
                          render_kw={"placeholder": "Enter height in centimeters"})

    age = IntegerField(label="Age:",
                       validators=[DataRequired(message="Age is required."),
                                   NumberRange(min=0, message="Age must be a positive number.")],
                       render_kw={"placeholder": "Enter your age"})

    country = SelectField(label="Country:",
                          choices=[('', 'Select country')],
                          validators=[DataRequired(
                              message="Country is required.")])

    city = SelectField(label="City:",
                       choices=[('', 'Select city')],
                       validators=[DataRequired(message="City is required.")])

    submit = SubmitField("Calculate", render_kw={"class": "calculate-btn"})

    def __init__(self, *args, **kwargs):
        """
        Initialize the CalorieForm.

        This constructor reads the countries data from a CSV file,
        sorts the DataFrame by 'Country', and sets the choices for
        the 'country' and 'city' fields.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        # Read the countries data from a CSV file
        df = pd.read_csv(COUNTRIES_FILE)
        # Sort the DataFrame by 'Country'
        self.countries_df = df.sort_values(by='Country')
        # Sort the DataFrame by 'City'
        self.cities_df = df.sort_values(by=['City'])
        # Set the choices for the 'country' field
        self.country.choices += self.get_countries()
        # Set the choices for the 'city' field
        self.city.choices += self.get_cities()

    def get_countries(self):
        """
        Get the list of countries.

        Returns:
            list: A list of tuples containing country names.
        """
        countries = [(row['Country'], row['Country'])
                     for _, row in self.countries_df.iterrows()]
        return countries

    def get_cities(self):
        """
        Get the list of cities.

        Returns:
            list: A list of tuples containing city names.
        """
        cities = [(row['City'], row['City'])
                  for _, row in self.cities_df.iterrows()]
        return cities
