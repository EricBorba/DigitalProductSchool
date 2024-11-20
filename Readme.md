# Accident Predictor App

This project provides a machine learning-based application that predicts accident occurrences based on various input features. It has been deployed on Heroku using Docker.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Dataset Cleaning and Model Training](#datasetcleaningmodeltraining)
- [Usage](#usage)
- [Testing the Deployed App](#testing-the-deployed-app)
- [Deployment](#deployment)
- [Notes](#notes)

## Features

- Predicts the likelihood of accidents based on input data.
- Easy deployment using Docker.
- Exposes a REST API that can be interacted with to get predictions.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Docker (for containerization)
- Heroku account (for deployment)
- Git (for version control)
- A text editor or IDE of your choice

### Install Dependencies

1. Clone the repository:

```bash
git clone https://github.com/your-username/accident-predictor.git
cd accident-predictor
```
2. Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

3. For Docker (optional but recommended for local testing), build the Docker image:

```bash
docker build -t accident-predictor .
```

### Dataset Cleaning and Model Training

The dataset cleaning and model training steps are handled in the main.ipynb Jupyter notebook. This notebook contains the entire pipeline from loading and cleaning the dataset to training the machine learning model that powers the accident prediction functionality in this app.

You can open and execute the notebook in Jupyter to see how the model is trained and the dataset is preprocessed.

## Usage 

### Run the App Locally

1. If you're running the app in a Docker container, you can start it using:

```bash
docker run -p 5000:5000 accident-predictor
```

2. Alternatively, you can start the app without Docker by running:

```bash
python app.py
```
The app will be available at http://localhost:5000/.

### Send a Prediction Request

To get a prediction from the app, make a POST request to the /predict endpoint with the following JSON data:

```bash
{
  "feature1": value1,
  "feature2": value2,
  ...
}
```
- Replace feature1, feature2, etc., with the actual features the model expects.
- value1, value2, etc., should be the values you wish to predict on.

## Testing the Deployed App

Once the app is deployed, you can test the functionality by running the script in testingEndPoint.py. This script will automatically send a request to the deployed app and allow you to interact with the accident predictor.

Simply execute:

```bash
python testingEndPoint.py
```
It will trigger the prediction process on the deployed app and display the response.

## Deployment

The app is deployed on Heroku using Docker. To deploy it yourself:

- Push the code to your GitHub repository.
- Connect the repository to Heroku and deploy.
- Heroku uses Docker to run the app. Make sure to check the heroku.yml file for the necessary build and run configurations.

```bash
build:
  docker:
    web: Dockerfile

run:
  web: gunicorn -b 0.0.0.0:$PORT app:app
```
This ensures that the application will be started with gunicorn on the correct port that Heroku assigns dynamically.

## Notes

This project uses Docker to containerize the app for easy deployment and portability.
If you'd like to run the app locally, make sure to have the correct dependencies installed.
The model for accident prediction is simple for demonstration purposes, and you may need to adjust it based on more comprehensive data or complex modeling.




