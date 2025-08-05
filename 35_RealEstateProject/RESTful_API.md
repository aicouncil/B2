# Building a RESTful API for Machine Learning Models using Flask

This document provides a detailed explanation of using the Flask web microframework to build simple web applications and, more specifically, to deploy a pre-trained machine learning model as a RESTful API. The content is based on the `flask_demo.py` and `real_estate_price.py` Python files.

## 1. Flask Fundamentals: A "Hello, World!" Example (`flask_demo.py`)

**Definition:** Flask is a lightweight and extensible Python web framework. It is often referred to as a "microframework" because it keeps the core simple, but allows for easy extension with third-party libraries. Flask is ideal for building simple web applications and APIs.

* **Installation:** The `flask_demo.py` file begins by instructing to install Flask using pip.
    ```python
    #pip install Flask - to install Flask in the system
    ```
* **Initializing the App:** A Flask application instance is created. `Flask(__name__)` tells Flask to look for resources in the same directory as the script.
    ```python
    from flask import Flask
    app = Flask(__name__)
    ```
* **Routing and Endpoints:** The `@app.route()` decorator maps a URL path (an endpoint) to a specific Python function.
    * **`@app.route("/")`**: This maps the root URL (`/`) of the application to the `hello_world()` function. When a user visits `http://127.0.0.1:5000/`, this function is executed.
    * **`@app.route("/greet")`**: This maps the `/greet` endpoint to the `greetings()` function.
    ```python
    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    @app.route("/greet")
    def greetings():
        return "Welcome to our prediction model"
    ```
* **Running the Server:** `app.run()` starts the development web server. It listens for incoming HTTP requests and directs them to the appropriate functions based on the routes defined.
    ```python
    app.run()
    ```
* **Use Cases (General Flask):** Building small websites, simple REST APIs, and prototyping web applications.

## 2. Deploying a Machine Learning Model as an API (`real_estate_price.py`)

This file demonstrates how to extend Flask's capabilities to build a production-ready API for a pre-trained real estate price prediction model. It takes a JSON or form-encoded request, processes the data, and returns a prediction.

### 2.1. Loading Pre-trained Model Artifacts

Before the Flask application can handle requests, it must load the necessary machine learning artifacts that were saved during the model training phase. These are loaded once when the application starts, which is more efficient than loading them with every request.

* **Model:** The trained `LinearRegression` model is loaded from `real_estate.pkl`.
* **Scaler:** The `MinMaxScaler` object used for feature scaling is loaded from `feature_scaling.pkl`.
* **Feature Columns:** The list of features used to train the model, in the correct order, is loaded from `training_data_columns.json`.
    ```python
    import joblib
    import json
    import numpy as np
    from flask import Flask, request

    app = Flask(__name__)
    _model = joblib.load('real_estate.pkl')
    _scaling = joblib.load('feature_scaling.pkl')

    my_json_file = open("training_data_columns.json" , "r")
    my_json_file = json.load(my_json_file)
    _features = my_json_file['data_columns']
    ```

### 2.2. The Prediction API Endpoint

A dedicated endpoint, `/predict`, is created to handle incoming prediction requests.

* **Route and HTTP Method:** The `@app.route('/predict', methods=['POST'])` decorator defines a route that specifically accepts `POST` requests. This is the standard method for sending data to a server to create or update a resource.
* **`predict_home_price()` Function:** This function is executed whenever a `POST` request is sent to the `/predict` endpoint.

    * **Data Extraction:** The function first checks if the incoming request data is in JSON format (`request.is_json`). It then extracts the data from either `request.json` or `request.form`.
        ```python
        if request.is_json:
            data = request.json
        else:
            data = request.form
        # Extract features from the 'data' object
        area_type = data.get('areaType')
        availability = data.get('availability')
        location = data.get('location')
        size = data.get('size')
        total_sqft = data.get('totalSqft')
        bath = data.get('bath')
        balcony = data.get('balcony')
        ```
    * **Input Preprocessing:** The raw input data is meticulously preprocessed to match the format of the training data.
        * A zero-filled NumPy array is initialized with the length of the `_features` list.
        * The categorical features (`area_type`, `availability`) are mapped to their numerical counterparts (0 or 1) using the same lambda functions defined during training.
        * Numerical features are assigned to their correct positions in the array.
        * The one-hot encoded `location` feature is handled by finding its index in `_features` and setting the value to 1.
    * **Prediction and Output:**
        * The prepared input array is scaled using the loaded `_scaling` object.
        * The scaled input is passed to `_model.predict()`. The model returns a log-transformed price.
        * The `np.exp()` function is used to convert the log-price prediction back to the original price scale.
        * Finally, the predicted price is returned as a JSON response with the key `"Predicted_Price"`.
    ```python
    # Preprocessing steps for input
    # ...
    price_predicted = np.exp(_model.predict(_scaling.transform([input])))[0]
    return {"Predicted_Price" : price_predicted}
    ```
* **Running the Server:** The `app.run(debug=True)` command starts the server in debug mode, which automatically reloads the application when code changes and provides a debugger in case of errors.

### 2.3. Use Cases and Benefits of a Flask ML API

* **Use Cases:** Deploying machine learning models for real-time inference, creating microservices that perform specific predictive tasks, and integrating ML capabilities into larger applications or websites.
* **Benefits:**
    * **Decoupling:** Separates the model logic from the main application, allowing different parts to be updated independently.
    * **Scalability:** The API can be scaled to handle a large number of prediction requests.
    * **Language Agnostic:** Any programming language that can make an HTTP request can interact with this API.
    * **Centralized Logic:** Encapsulates complex preprocessing and prediction logic in one place.

* **Limitations:**
    * **Consistency is Key:** The API is highly dependent on receiving input data in the exact format, order, and with the same feature set as the training data. Mismatched or malformed input will cause errors.
    * **Error Handling:** The current implementation has basic error handling for the API; in a production environment, more robust validation and error messages would be needed for malformed requests or missing features.
    * **Scalability:** While `app.run()` is suitable for development, for production, a more robust and scalable WSGI server (e.g., Gunicorn or uWSGI) would be used in front of the Flask app.
