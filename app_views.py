from flask import render_template, redirect, url_for
from flask.views import MethodView
from app_forms import CaloriesForm


class IndexView(MethodView):
    def get(self):
        return render_template("index.html")


class CaloriesFormView(MethodView):
    def get(self):
        calories_form = CaloriesForm()
        return render_template("calories_form.html", caloriesform=calories_form)

    def post(self):
        pass
