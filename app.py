import os
from flask import Flask
from dotenv import load_dotenv
from app_views import IndexView, CaloriesFormView

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('APP_SECRET_KEY')  # Required for flashing messages


app.add_url_rule('/', view_func=IndexView.as_view('index_view'))
app.add_url_rule(
    '/calories_form', view_func=CaloriesFormView.as_view('calories_form_view'), methods=['GET', 'POST'])


if __name__ == "__main__":
    app.run(debug=True)
