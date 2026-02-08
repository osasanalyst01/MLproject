from flask import Flask, request, render_template
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Initialize Flask app
app = Flask(__name__)

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Prediction route
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    
    try:
        # Collect form data
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )

        # Convert to DataFrame
        pred_df = data.get_data_as_data_frame()
        print("Before Prediction:\n", pred_df)

        # Make prediction
        predict_pipeline = PredictPipeline()
        print("Mid Prediction")
        results = predict_pipeline.predict(pred_df)
        print("After Prediction:", results)

        # Return result to template
        return render_template('home.html', results=float(results[0]))

    except Exception as e:
        # Catch any errors and display
        print("Prediction error:", e)
        return render_template('home.html', results=f"Error: {e}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)



