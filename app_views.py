from flask import render_template, redirect, url_for, request, flash
from flask.views import MethodView
from app_forms import CaloriesForm
from classes import Temperature, Calorie


class IndexView(MethodView):
    def get(self):
        return render_template("index.html")


class CaloriesFormView(MethodView):
    def get(self):
        calories_form = CaloriesForm()
        return render_template("calories_form.html", caloriesform=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)

        if not calories_form.validate_on_submit():
            for field, errors in calories_form.errors.items():
                for error in errors:
                    field_obj = getattr(calories_form, field, None)
                    if field_obj is not None and hasattr(field_obj, 'label') and hasattr(field_obj.label, 'text'):
                        field_label = field_obj.label.text
                    else:
                        field_label = field
                    flash(f"Error in '{field_label}': {error}", 'danger')
            # returns a 400 status code (Bad Request) to indicate that the client's request was incorrect and could not be processed.
            return render_template('calories_form.html', caloriesform=calories_form), 400

        try:
            # Extract data from the form
            gender = calories_form.gender.data.strip()
            weight = float(calories_form.weight.data)
            height = float(calories_form.height.data)
            age = int(calories_form.age.data)

            country = calories_form.country.data.strip()
            city = calories_form.city.data.strip()

            temperature, error = Temperature(country, city).get()
            if temperature is None:
                flash(error, 'danger')

            calorie_intake = Calorie(gender=gender,
                                     weight_kg=weight,
                                     height_cm=height,
                                     age_years=age,
                                     temperature_celsius=temperature).calculate()
            
            calorie_intake = round(calorie_intake, 2)

            # Render the result of the calculated calories intake of today in the same template, returns a 200 status code (OK) to indicate that the request was successful and the resource (in this case, the redirected page) is being returned.
            return render_template(
                'calories_form.html',
                caloriesform=CaloriesForm(),
                daily_calorie_intake=calorie_intake), 200

        except Exception as e:
            flash(f"An error occurred while processing the form: {e}")
            # Redirect to the form page if there's an error, return a 500 status code (Internal Server Error) to indicate that an unexpected error occurred on the server.
            return redirect(url_for('calories_form_view')), 500
