# CalorieQuest

![CalorieQuest_logo](./static/assets/images/CalorieQuest_logo.png)

## Overview
CalorieQuest is a Flask application designed to help users calculate their daily calorie intake based on their personal information and environmental temperature. It provides users with a form to input their gender, weight, height, age, country, and city. Using this information, the application calculates the daily calorie intake using the Harris-Benedict equation and adjusts it based on the environmental temperature.

## Features
- **Calorie Calculation**: Calculate daily calorie intake based on personal information and environmental temperature.
- **Interactive Form**: User-friendly form to input personal details for accurate calorie calculation.
- **Temperature Adjustment**: Adjust calorie intake based on the environmental temperature for more accurate results.
- **Accurate Logger**: Utilizes a logger located at `assets/log/app.log` in to record debug and error messages accurately.

## Technologies Used
- **Flask**: A micro web framework for Python.
- **Flask-WTF**: Integrates Flask with WTForms, providing form rendering and validation.
- **lxml**: A library for processing XML and HTML.
- **pandas**: A data manipulation and analysis library.
- **python-dotenv**: A library for managing environment variables in .env files.
- **requests**: A library for making HTTP requests.
- **selectorlib**: A library for extracting data from web pages.
- **WTForms**: A flexible forms validation and rendering library for Python web development.
- **logging**: A module for tracking events that happen when software runs.

## Setup
1. Clone the repository.
2. Ensure Python 3.x is installed.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Configure the necessary parameters such as API keys and database connections in `constants.py`.
   - Ensure the required environment variables are set in `.flaskenv`.
5. Run the Flask application using `python app.py` or `flask run`.

## Usage
1. Navigate to the application directory in your terminal.
2. Set up your environment variables in the `.flaskenv` file:
    ```
    # Disable colored output for Flask logger
    # This prevents ANSI escape codes from being included in log files
    COLOREDLOGS_DISABLE=1

    # Set the environment to development mode. This enables features like the interactive debugger and reloader.
    FLASK_ENV=development

    # Enable debug mode
    FLASK_DEBUG=1
    ```
3. Run the Flask application using `python app.py` or `flask run`.
4. Access the application in your web browser at `http://localhost:5000`.
5. Fill out the form with your personal information and submit.
6. View the calculated daily calorie intake based on your inputs and the environmental temperature retrieved from [Time and Date](https://www.timeanddate.com/weather).

## Customization Options and Implementation Details
Users are free to add countries and cities to the CSV file in the `resources` directory to expand the available options.

## Implementation Details
Note: The views are implemented as class-based views using object-oriented programming (OOP) principles.

## Conclusion
Enjoy calculating your daily calorie intake with CalorieQuest!


## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.