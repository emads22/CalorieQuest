import os
import logging
from flask import Flask
from dotenv import load_dotenv
from app_views import IndexView, CalorieFormView
from constants import LOG_FILE


load_dotenv()

# Configure the logging format and level (DEBUG level is typically used for detailed diagnostic information, good for for developers or system administrators to troubleshoot issues)
logging.basicConfig(filename=LOG_FILE,
                    format='%(asctime)s - %(levelname)s - %(message)s (%(module)s:%(filename)s:%(lineno)d)', level=logging.DEBUG)

app = Flask(__name__)

app.secret_key = os.getenv('APP_SECRET_KEY')  # Required for flashing messages


app.add_url_rule('/', view_func=IndexView.as_view('index_view'))
app.add_url_rule(
    '/calorie_form', view_func=CalorieFormView.as_view('calorie_form_view'), methods=['GET', 'POST'])


if __name__ == "__main__":
    app.run(debug=True)
