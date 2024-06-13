import requests
import random
from selectorlib import Extractor
from constants import *


class ElementException(Exception):
    pass


class Calorie:
    """
    Represents the optimal calorie amount a person needs to take today.

    Attributes:
        weight (float): The person's weight in kilograms.
        height (float): The person's height in centimeters.
        age (int): The person's age in years.
        temperature (float): The current temperature in degrees Celsius.
    """

    def __init__(self, weight: float, height: float, age: int, temperature: float) -> None:
        """
        Initializes the Calorie object with the specified weight, height, age, and temperature.

        Args:
            weight (float): The person's weight in kilograms.
            height (float): The person's height in centimeters.
            age (int): The person's age in years.
            temperature (float): The current temperature in degrees Celsius.
        """
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self) -> float:
        """
        Calculates the optimal calorie intake for the day based on the given attributes.

        The formula used is a simplified version of the Harris-Benedict equation adjusted for temperature:
        calorie_intake = 10 * weight + 6.5 * height + 5 - temperature * 10

        Returns:
            float: The calculated optimal calorie intake.
        """
        # Calculate the calorie requirement using the given formula
        calorie_intake = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10

        return calorie_intake



class Temperature:
    """
    Represents a temperature value extracted from the `https://www.timeanddate.com/weather` webpage.

    Attributes:
        base_endpoint (str): The base URL for the weather information.
        country (str): The country for which to get the temperature, in lowercase.
        city (str): The city for which to get the temperature, in lowercase.
        url (str): The constructed URL for the weather information for the specified country and city.
    """
    base_endpoint = "https://www.timeanddate.com/weather"

    def __init__(self, country: str, city: str) -> None:
        """
        Initializes the Temperature object with a specific country and city.

        Args:
            country (str): The country for which to get the temperature.
            city (str): The city for which to get the temperature.
        """
        self.country = country.lower()
        self.city = city.lower()
        self.url = f"{self.base_endpoint}/{self.country}/{self.city}"

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
            # Define headers for the HTTP request to mimic a browser request and avoid blocking
            headers = {
                'user-agent': random.choice(USER_AGENT_LIST),
                'accept-language': ACCEPT_LANGUAGE
            }

            # Make the HTTP GET request to fetch the webpage content
            response = requests.get(self.url, headers=headers)

            # Raise an exception if the request was unsuccessful
            response.raise_for_status()

            # Extract data from the webpage using the predefined YAML extractor
            extractor = Extractor.from_yaml_file(YAML_FILE)
            data = extractor.extract(response.text)
           
            # Check if the temperature element is present (walrus operator)
            if temp := data.get('temperature') is None:
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


if __name__ == "__main__":
    
    temp, error = Temperature("lebanon", "beirut").get()

    if temp is None:
        print(f"\n\n--- {error} ---\n\n")

    else:
        optimal_calorie_intake = Calorie(weight=65.5,
                                         height=170,
                                         age=33,
                                         temperature=temp).calculate()

        print(f"\n\n>> Temperature is: {temp} °C.")
        print(f"\n>> Optimal Calories Intake is: {optimal_calorie_intake}.")