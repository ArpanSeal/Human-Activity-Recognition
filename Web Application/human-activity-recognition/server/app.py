import json
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from PIL import Image, ImageTk
from bson import ObjectId
from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS
import pandas as pd
import threading
from connection import MongoClient, db, collection

app = Flask(__name__)
CORS(app)

# Load the trained model from file
with open("svm_model_new.pkl", "rb") as f:
    model = joblib.load(f)

# Define a dictionary mapping each activity to its corresponding image file path
activity_image_paths = {
    "NO_ACTIVITY": "img/NO_ACTIVITY.png",
    "WALKING": "img/WALKING.png",
    "JOGGING": "img/JOGGING.png",
}

# Create the GUI window and widgets
root = tk.Tk()
root.title("Activity Prediction")
root.geometry("600x630")

# Set the background color and font
root.configure(bg="#F0F0F0")

# Define custom fonts
title_font = Font(family="Helvetica", size=28, weight="bold")
prediction_label_font = Font(family="Helvetica", size=18)
prediction_value_font = Font(family="Helvetica", size=24, weight="bold")

# Add a label for the title
title_label = tk.Label(
    root, text="Activity Prediction", font=title_font, bg="#F2F2F2", fg="#006699"
)
title_label.pack(pady=20)

# Add a separator for visual separation
separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill="x", pady=10)

# Add a label for the predicted activity
prediction_label = tk.Label(
    root,
    text="Predicted Activity:",
    font=prediction_label_font,
    bg="#F0F0F0",
    fg="#444444",
)
prediction_label.pack()

# Add a label for the prediction value
prediction_value_label = tk.Label(
    root, text="", font=prediction_value_font, bg="#F0F0F0", fg="#006699"
)
prediction_value_label.pack(pady=20)

# Add a label for the activity image
image_label = tk.Label(root, bg="#F0F0F0")
image_label.pack(pady=10)

activity_counts = {"NO_ACTIVITY": 0, "WALKING": 0, "JOGGING": 0, "Total": 0}


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)


@app.route("/predict", methods=["POST"])
def predict():
    # Get the sensor data from the request
    sensor_data = request.get_json()
    print(sensor_data)  # added to print the received data

    # Create a pandas DataFrame from the sensor data
    data = [
        [
            sensor_data["ax"],
            sensor_data["ay"],
            sensor_data["az"],
            sensor_data["gx"],
            sensor_data["gy"],
            sensor_data["gz"],
            sensor_data["aMagnitude"],
            sensor_data["gMagnitude"],
        ]
    ]

    df = pd.DataFrame(
        data, columns=["ax", "ay", "az", "gx", "gy", "gz", "aMagnitude", "gMagnitude"]
    )

    # Remove any rows that contain NaN values
    df = df.dropna()

    if df.empty:
        return {"error": "All values are NaN."}

    # Make the prediction
    # y_pred = model.predict(df)
    # prediction = y_pred[0]
    
    # Update the GUI with the prediction value
    if df['aMagnitude'][0]<1:
        prediction = "NO_ACTIVITY"
    elif df['aMagnitude'][0]>1 and df['aMagnitude'][0]<5:
        prediction = "WALKING"
    else:
        prediction = "JOGGING"
    
    prediction_l = ""
    
    if prediction == "NO_ACTIVITY":
        prediction_l = "NO ACTIVITY"
    else:
        prediction_l = prediction

    activity_counts["NO_ACTIVITY"]=0
    activity_counts["WALKING"]=0
    activity_counts["JOGGING"]=0

    # Update the activity counts
    if prediction == "NO_ACTIVITY":
        activity_counts["NO_ACTIVITY"] = 1
    elif prediction == "WALKING":
        activity_counts["WALKING"] = 1
    elif prediction == "JOGGING":
        activity_counts["JOGGING"] = 1
    
    activity_counts["Total"] = (
        activity_counts["JOGGING"]
        + activity_counts["NO_ACTIVITY"]
        + activity_counts["WALKING"]
    )

    # Update the GUI with the prediction value
    root.attributes("-topmost", 1)  # make the GUI window the topmost window
    prediction_value_label.config(
        text=prediction_l, fg="#006699"
    )  # update the label with the prediction
    image_path = activity_image_paths.get(prediction)
    if image_path:
        image = Image.open(image_path)
        image = image.resize((250, 350))
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo)
        image_label.image = (
            photo  # keep a reference to the photo to prevent garbage collection
        )
    root.attributes("-topmost", 0)  # remove the topmost attribute from the GUI window
    
    prediction_value_label.config(
        text=prediction_l, fg="#006699"
    )  # update the label with the prediction
    image_path = activity_image_paths.get(prediction)
    if image_path:
        image = Image.open(image_path)
        image = image.resize((250, 350))
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo)
        image_label.image = (
            photo  # keep a reference to the photo to prevent garbage collection
        )
    root.attributes("-topmost", 0)  # remove the topmost attribute from the GUI window

    # Create a dictionary containing the prediction and activity counts
    response_data = {"last_prediction": prediction, "activity_counts": activity_counts}

    json_string = json.dumps(response_data, cls=CustomJSONEncoder)

    print(prediction, response_data, activity_counts["JOGGING"]
        , activity_counts["NO_ACTIVITY"]
        , activity_counts["WALKING"])

    existing_doc = collection.find_one({})
    if existing_doc is None:
        # If the database is empty, insert a new document with the prediction and activity counts
        collection.insert_one(json.loads(json_string))

    else:
        # Fetch the existing activity counts from the database
        existing_counts = collection.find_one({}, {"activity_counts": 1})[
            "activity_counts"
        ]

        if existing_counts["Total"] > 10800:
            # If Total is greater than 10800, reset all activity counts and prediction
            existing_counts = activity_counts
            prediction = prediction
        else:
            # Add the predicted activity counts to the existing activity counts
            for activity in activity_counts:
                existing_counts[activity] += activity_counts[activity]
        # Update the activity counts in the database
        collection.update_one(
            {},
            {
                "$set": {
                    "activity_counts": existing_counts,
                    "last_prediction": prediction,
                }
            },
            upsert=True,
        )

    return {'prediction': prediction_l}


@app.route("/percentage", methods=["GET"])
def get_response_data():
    # Get the response data from the database
    existing_doc = collection.find_one({})
    if existing_doc is None:
        response_data = {"last_prediction": "", "activity_counts": activity_counts}
        json_string = json.dumps(response_data, cls=CustomJSONEncoder)
        return json.dumps(json_string)
    else:
        # Convert the dictionary to a JSON string and return it
        return json.dumps(existing_doc, default=str)


def run_flask():
    app.run(host="192.168.155.200", port=5000)


if __name__ == "__main__":
    # Start the Flask app in a separate thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Start the GUI event loop in the main thread
    try:
        root.mainloop()
    except KeyboardInterrupt:
        pass