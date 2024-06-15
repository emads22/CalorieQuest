import logging
from flask import render_template, redirect, url_for, request, flash
from flask.views import MethodView
from app_forms import CalorieForm
from app_utils import Temperature, Calorie


class IndexView(MethodView):
    def get(self):
        return render_template("index.html")


class CalorieFormView(MethodView):
    def get(self):
        calorie_form = CalorieForm()
        return render_template("calorie_form.html", calorieform=calorie_form)

    def post(self):
        calorie_form = CalorieForm(request.form)

        if not calorie_form.validate_on_submit():
            # Flash a message to inform the user that there are errors in the form
            flash('Please ensure all fields are filled correctly.', 'danger')
            # Render the template with the populated form and return a 400 status code (Bad Request)
            # to indicate that the client's request was incorrect and could not be processed.
            return render_template('calorie_form.html', calorieform=calorie_form), 400

        try:
            # Extract data from the form
            gender = calorie_form.gender.data.strip()
            weight = float(calorie_form.weight.data)
            height = float(calorie_form.height.data)
            age = int(calorie_form.age.data)
            country = calorie_form.country.data.strip()
            city = calorie_form.city.data.strip()

            # Retrieve temperature data for the specified country and city
            temperature, error = Temperature(country, city).get()

            # If temperature data is not available, log and display an error message
            if temperature is None:
                # Log a detailed error message along with the traceback for debugging purposes
                logging.error(f"Failed to retrieve temperature data: {
                              error}", exc_info=True)
                # Flash a user-friendly error message
                flash(
                    "An error occurred while retrieving temperature data. Please try again later.", 'danger')
                # Return from the function to indicate that the request cannot be processed further
                return render_template('calorie_form.html', calorieform=calorie_form), 400

            # Calculate the daily calorie intake based on the retrieved data
            calorie_intake = Calorie(gender=gender,
                                     weight_kg=weight,
                                     height_cm=height,
                                     age_years=age,
                                     temperature_celsius=temperature).calculate()

            # Round the calculated calorie intake to two decimal places
            calorie_intake = round(calorie_intake, 2)

            # Render the result of the calculated calories intake in the same template
            # along with the populated form (we can also send CalorieForm() which is
            # a new instance of the form to clear any previous data),
            # and return a 200 status code (OK) to indicate that the request was successful.
            return render_template(
                'calorie_form.html',
                calorieform=calorie_form,
                daily_calorie_intake=calorie_intake), 200

        except Exception as e:
            # If an unexpected error occurs during form processing, log the error
            logging.error(f"An error occurred while processing the form: {
                          e}", exc_info=True)
            # If an unexpected error occurs during form processing, flash an error message
            # and redirect to the form page. Return a 500 status code (Internal Server Error)
            # to indicate that an unexpected error occurred on the server.
            flash(
                "An unexpected error occurred while processing the form. Please try again later.", 'danger')
            return redirect(url_for('calorie_form_view')), 500
