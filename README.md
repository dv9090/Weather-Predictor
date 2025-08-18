# Weather Predictor 🌦️

A simple and elegant web-based weather application that provides real-time weather data for any city. The app features a clean, modern user interface with a dynamic background that changes to reflect the current weather conditions.

## Features

* **Real-Time Weather Data:** Get up-to-the-minute weather information, including temperature, humidity, and wind speed.
* **City Search:** Easily search for any city in the world to get its current weather.
* **Dynamic Backgrounds:** The background image changes to match the current weather conditions (e.g., sunny, cloudy, rainy).
* **Responsive Design:** The application is designed to look great on all devices, from desktops to mobile phones.
* **Clean UI:** A minimalist and intuitive user interface for a seamless user experience.

## Technologies Used

* **HTML:** For the structure and content of the application.
* **Tailwind CSS:** For modern and responsive styling.
* **JavaScript:** For application logic, API calls, and DOM manipulation.
* **OpenWeatherMap API:** To fetch the real-time weather data.
* **Unsplash:** For the high-quality, dynamic background images.

## Setup and Usage

This project is a single HTML file and requires no complex setup.

1. **Get an API Key:**
   * You will need an API key from [OpenWeatherMap](https://openweathermap.org/api). Sign up for a free account to get your key.

2. **Add Your API Key:**
   * Open the `index.html` file.
   * Find the following line in the `<script>` section at the bottom:
     ```javascript
     const openWeatherApiKey = "e7602e0a5cc41c486b812006b0bcfa5b";
     ```
   * Replace `"e7602e0a5cc41c486b812006b0bcfa5b"` with your actual OpenWeatherMap API key.

3. **Run the Application:**
   * Simply open the `index.html` file in your web browser.
   * For the best experience during development, use a live server extension (like "Live Server" in VS Code).

## Acknowledgements

* Weather data provided by [OpenWeatherMap](https://openweathermap.org).
* Background images provided by [Unsplash](https://unsplash.com).
