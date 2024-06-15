import requests
import random
from selectorlib import Extractor
from constants import *


class ElementException(Exception):
    """
    Exception raised when an expected HTML element is not found during web scraping.

    This exception is raised when a specific HTML element that is expected to be present in the web page
    during scraping is not found. It indicates that the structure of the web page has changed or the element
    is missing, leading to a failure in data extraction.
    """

    def __init__(self, message="HTML element not found"):
        """
        Initialize the ElementException.

        Args:
            message (str, optional): Explanation of the error. Defaults to "HTML element not found".
        """
        super().__init__(message)


class Temperature:
    """
    Represents a temperature value extracted from the `https://www.timeanddate.com/weather` webpage.

    This class provides functionality to retrieve the current temperature for a specified country and city.

    Attributes:
        base_endpoint (str): The base URL for the weather information on the Time and Date website.
        headers (dict): The headers for the HTTP request to mimic a browser request and avoid blocking.
            It includes 'user-agent' and 'accept-language'.
        yaml_file (str): The path to the YAML file containing the extraction rules for the webpage content.
        country (str): The country for which to retrieve the temperature, provided in lowercase.
        city (str): The city for which to retrieve the temperature, provided in lowercase.
        url (str): The constructed URL for the weather information for the specified country and city.
    """
    base_endpoint = "https://www.timeanddate.com/weather"
    headers = {
        'user-agent': random.choice(USER_AGENT_LIST),
        'accept-language': ACCEPT_LANGUAGE
    }
    yaml_file = YAML_FILE

    def __init__(self, country: str, city: str) -> None:
        """
        Initializes the Temperature object with a specific country and city.

        Args:
            country (str): The country for which to get the temperature.
            city (str): The city for which to get the temperature.
        """
        self.country = country.replace(" ", "-").lower()
        self.city = city.replace(" ", "-").lower()
        self.url = self._build_url()

    def _build_url(self) -> str:
        """
        Builds the URL for fetching weather information.

        Returns:
            str: The constructed URL.
        """
        url = f"{self.base_endpoint}/{self.country}/{self.city}"
        return url

    def _scrape(self) -> str:
        # Make the HTTP GET request to fetch the webpage content
        response = requests.get(url=self._build_url(), headers=self.headers)

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        # Extract data from the webpage using the predefined YAML extractor
        extractor = Extractor.from_yaml_file(self.yaml_file)
        raw_data = extractor.extract(response.text)

        return raw_data

    def get(self) -> (float, str):
        """
        Retrieves the current temperature for the specified country and city.

        Returns:
            tuple: A tuple containing the current temperature in degrees (assumed to be Celsius) and an error message.
                   If the temperature is successfully retrieved, the error message will be None.
                   If an error occurs, the temperature will be None and the error message will provide details.

        Raises:
            Exception: If an error occurs during the HTTP request or data extraction.
        """
        try:

            # Scrape temperature raw data
            data = self._scrape()

            # Check if the temperature element is present (walrus operator)
            if (temp := data.get('temperature')) is None:
                raise ElementException

            # Extract the temperature value from the extracted data and convert it to float
            temp = float(temp.split()[0])

            return temp, None

        except requests.RequestException as e:
            # Handle exceptions related to the HTTP request
            error_message = f"Error during HTTP request: {e}"

        except ElementException:
            # Handle exceptions when the temperature element is not found in the extracted data
            error_message = "Temperature element not found."

        except Exception as e:
            # Handle any other exceptions that may occur
            error_message = f"Error occurred: {e}"

        return None, error_message


class Calorie:
    def __init__(self, gender, weight_kg, height_cm, age_years, temperature_celsius):
        """
        Initialize the Calorie object with the given parameters.

        Parameters:
            gender (str): Gender of the individual ('male' or 'female').
            weight_kg (float): Weight of the individual in kilograms.
            height_cm (float): Height of the individual in centimeters.
            age_years (int): Age of the individual in years.
            temperature_celsius (float): Temperature in Celsius of the individual's environment.
        """
        # Convert gender to lowercase for consistency
        self.gender = gender.lower()
        self.weight_kg = weight_kg
        self.height_cm = height_cm
        self.age_years = age_years
        self.temperature_celsius = temperature_celsius

    def bmr(self):
        """
        Calculate the Basal Metabolic Rate (BMR) based on gender using the Harris-Benedict equations.

        Returns:
            float: The calculated BMR.
        """
        if self.gender == 'male':
            # Harris-Benedict equation for males
            bmr = 88.362 + (13.397 * self.weight_kg) + \
                (4.799 * self.height_cm) - (5.677 * self.age_years)
        elif self.gender == 'female':
            # Harris-Benedict equation for females
            bmr = 447.593 + (9.247 * self.weight_kg) + \
                (3.098 * self.height_cm) - (4.330 * self.age_years)
        else:
            raise ValueError(
                "Invalid gender. The gender must be specified as 'male' or 'female'.")

        return bmr

    def calculate(self):
        """
        Calculate the daily calorie intake based on the Basal Metabolic Rate (BMR) and temperature factor.

        The daily calorie intake is estimated using the Harris-Benedict equation:

        - For males:
            BMR = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age_years)
        - For females:
            BMR = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age_years)

        The resulting BMR is adjusted based on the environmental temperature:
        - If temperature <= 10°C: Calorie intake is decreased by 20%.
        - If 10°C < temperature <= 25°C: Calorie intake remains unchanged.
        - If temperature > 25°C: Calorie intake is increased by 20%.

        If temperature is not provided, calorie intake is assumed to be under moderate conditions.

        Returns:
            float: The estimated daily calorie intake.
        """
        bmr = self.bmr()

        # Check if temperature is provided
        if self.temperature_celsius is None:
            # If temperature is not provided, assume moderate conditions
            temperature_factor = 1.0
        else:
            # Determine temperature factor based on the environmental temperature
            if self.temperature_celsius <= 10:
                temperature_factor = 0.8  # Cold
            elif self.temperature_celsius <= 25:
                temperature_factor = 1.0  # Moderate
            else:
                temperature_factor = 1.2  # Hot

        # Calculate calorie intake based on BMR and temperature factor
        calorie_intake = bmr * temperature_factor
        return calorie_intake


if __name__ == "__main__":

    temp, error = Temperature("lebanon", "beirut").get()

    if temp is None:
        print(f"\n\n--- {error} ---\n\n")

    else:
        daily_calorie_intake = Calorie(gender='female',
                                       weight_kg=70,
                                       height_cm=165,
                                       age_years=30,
                                       temperature_celsius=20).calculate()

    print(f"\n\n>> Temperature: {temp} °C.")
    print(f"\n>> Daily Calorie Intake: {daily_calorie_intake:.2f} kcal.\n\n")
