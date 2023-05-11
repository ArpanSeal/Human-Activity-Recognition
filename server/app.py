# # Final
# from flask import Flask, request
# import joblib
# from flask_cors import CORS
# import pandas as pd

# app = Flask(__name__)
# CORS(app)

# # Load the trained model from file
# with open('svm_model_new.pkl', 'rb') as f:
#     model = joblib.load(f)

# # @app.route('/')
# # def home():
# #     return 'Hello, World!'

# @app.route('/predict', methods=['POST'])

# def predict():
#     # Get the sensor data from the request
#     sensor_data = request.get_json()
#     print(sensor_data) # added to print the received data

#     # Create a pandas DataFrame from the sensor data
#     data = [[sensor_data['ax'], sensor_data['ay'], sensor_data['az'], sensor_data['gx'], sensor_data['gy'], sensor_data['gz'], sensor_data['aMagnitude'], sensor_data['gMagnitude']]]

#     # data = [[-0.049064, -0.084648,  0.212564,  4.188414, -1.571609,  34.644058]]

#     df = pd.DataFrame(data, columns=['ax', 'ay', 'az', 'gx', 'gy', 'gz', 'aMagnitude', 'gMagnitude'])

#     # Remove any rows that contain NaN values
#     df = df.dropna()

#     if df.empty:
#         return {'error': 'All values are NaN.'}

#     # Make the prediction
#     y_pred = model.predict(df)

#     # Return the prediction as JSON
#     # print(y_pred[0])

#     # print(df['aMagnitude'][0])

#     if df['aMagnitude'][0]<1: print("NO_ACTIVITY")
#     elif df['aMagnitude'][0]>1 and df['aMagnitude'][0]<4: print("WALKING")
#     else: print("JOGGING")

#     return {'prediction': y_pred[0]}

# if __name__ == '__main__':
#     app.run(host='192.168.177.200', port=5000, debug=True)


# from flask import Flask, request
# import joblib
# from flask_cors import CORS
# import pandas as pd
# import pyttsx3
# import time

# app = Flask(__name__)
# CORS(app)

# # Load the trained model from file
# with open('svm_model_new.pkl', 'rb') as f:
#     model = joblib.load(f)

# # Initialize the TTS engine
# engine = pyttsx3.init()

# def predict_and_speak():
#     # Get the sensor data from the request
#     sensor_data = request.get_json()
#     print(sensor_data) # added to print the received data

#     # Create a pandas DataFrame from the sensor data
#     data = [[sensor_data['ax'], sensor_data['ay'], sensor_data['az'], sensor_data['gx'], sensor_data['gy'], sensor_data['gz']]]

#     df = pd.DataFrame(data, columns=['ax', 'ay', 'az', 'gx', 'gy', 'gz'])

#     # Remove any rows that contain NaN values
#     df = df.dropna()

#     if df.empty:
#         return {'error': 'All values are NaN.'}

#     # Make the prediction
#     y_pred = model.predict(df)

#     # Convert the predicted activity to a voice message
#     activity = y_pred[0]
#     message = f"The predicted activity is {activity}"
#     engine.say(activity)
#     engine.runAndWait()

#     # Return the prediction as JSON
#     print(activity)
#     return {'prediction': activity}

# @app.route('/predict', methods=['POST'])
# def predict():
#     return predict_and_speak()

# if __name__ == '__main__':
#     while True:
#         predict_and_speak()
#         time.sleep(3)


# # GUI
# import tkinter as tk
# from flask import Flask, request
# import joblib
# from flask_cors import CORS
# import pandas as pd

# app = Flask(__name__)
# CORS(app)

# # Load the trained model from file
# with open('svm_model_new.pkl', 'rb') as f:
#     model = joblib.load(f)

# # @app.route('/')
# # def home():
# #     return 'Hello, World!'

# @app.route('/predict', methods=['POST'])

# def predict():
#     # Get the sensor data from the request
#     sensor_data = request.get_json()
#     print(sensor_data) # added to print the received data

#     # Create a pandas DataFrame from the sensor data
#     data = [[sensor_data['ax'], sensor_data['ay'], sensor_data['az'], sensor_data['gx'], sensor_data['gy'], sensor_data['gz'], sensor_data['aMagnitude'], sensor_data['gMagnitude']]]

#     # data = [[-0.049064, -0.084648,  0.212564,  4.188414, -1.571609,  34.644058]]

#     df = pd.DataFrame(data, columns=['ax', 'ay', 'az', 'gx', 'gy', 'gz', 'aMagnitude', 'gMagnitude'])

#     # Remove any rows that contain NaN values
#     df = df.dropna()

#     if df.empty:
#         return {'error': 'All values are NaN.'}

#     # Make the prediction
#     y_pred = model.predict(df)

#     # Create a GUI window
#     root = tk.Tk()
#     root.geometry('500x500')

#     # Set the activity name based on the prediction
#     activity = ''
#     if y_pred[0] == "NO_ACTIVITY":
#         activity = 'NO_ACTIVITY'
#         photo = tk.PhotoImage(file='img\NO_ACTIVITY.png')
#     elif y_pred[0] == "WALKING":
#         activity = 'WALKING'
#         photo = tk.PhotoImage(file='img\WALKING.png')
#     elif y_pred[0] == "JOGGING":
#         activity = 'JOGGING'
#         photo = tk.PhotoImage(file='img\JOGGING.png')

#     # Create a label to display the activity name and photo
#     label = tk.Label(root, text=activity, image=photo, compound='top')
#     label.pack()

#     # Run the GUI window
#     root.mainloop()

#     # Return the prediction as JSON
#     print(y_pred[0])
#     return {'prediction': y_pred[0]}


# if __name__ == '__main__':
#     app.run(host='192.168.177.200', port=5000, debug=True)


# # Last
# from flask import Flask, request
# from tkinter import *
# import joblib
# from flask_cors import CORS
# import pandas as pd

# app = Flask(__name__)
# CORS(app)

# # Create a Tkinter window
# root = Tk()

# # Set the window title and size
# root.title("Predicted Activity")
# root.geometry("300x100")

# # Create a Label widget to display the predicted activity
# activity_label = Label(root, text="Waiting for activity...")
# activity_label.pack()

# # Load the trained model from file
# with open('svm_model_new.pkl', 'rb') as f:
#     model = joblib.load(f)

# @app.route('/predict', methods=['POST'])

# def predict():
#     # Get the sensor data from the request
#     sensor_data = request.get_json()
#     print(sensor_data) # added to print the received data

#     # Create a pandas DataFrame from the sensor data
#     data = [[sensor_data['ax'], sensor_data['ay'], sensor_data['az'], sensor_data['gx'], sensor_data['gy'], sensor_data['gz'], sensor_data['aMagnitude'], sensor_data['gMagnitude']]]

#     df = pd.DataFrame(data, columns=['ax', 'ay', 'az', 'gx', 'gy', 'gz', 'aMagnitude', 'gMagnitude'])

#     # Remove any rows that contain NaN values
#     df = df.dropna()

#     if df.empty:
#         return {'error': 'All values are NaN.'}

#     # Make the prediction
#     y_pred = model.predict(df)

#     # Return the prediction as JSON
#     print(y_pred[0])

#     activity = y_pred[0]

#     # Update the activity label
#     activity_label.config(text=activity)

#     return {'prediction': y_pred[0]}

# if __name__ == '__main__':
#     app.run(host='192.168.177.200', port=5000, debug=True)

#     # Start the Tkinter event loop
#     root.mainloop()


# # GUI somehow successful
# import tkinter as tk
# from tkinter import ttk
# from tkinter.font import Font
# from flask import Flask, request
# import joblib
# from flask_cors import CORS
# import pandas as pd

# app = Flask(__name__)
# CORS(app)

# # Load the trained model from file
# with open('svm_model_new.pkl', 'rb') as f:
#     model = joblib.load(f)

# @app.route('/predict', methods=['POST'])
# def predict():

#     # Create the GUI window and widgets
#     root = tk.Tk()
#     root.title("Activity Prediction")
#     root.geometry("600x600")

#     label = tk.Label(root, text="Predicted Activity:", font=Font(size=16))
#     label.pack()

#     prediction_label = tk.Label(root, text="", font=Font(size=20))
#     prediction_label.pack()

#     # Get the sensor data from the request
#     sensor_data = request.get_json()
#     print(sensor_data) # added to print the received data

#     # Create a pandas DataFrame from the sensor data
#     data = [[sensor_data['ax'], sensor_data['ay'], sensor_data['az'], sensor_data['gx'], sensor_data['gy'], sensor_data['gz'], sensor_data['aMagnitude'], sensor_data['gMagnitude']]]

#     df = pd.DataFrame(data, columns=['ax', 'ay', 'az', 'gx', 'gy', 'gz', 'aMagnitude', 'gMagnitude'])

#     # Remove any rows that contain NaN values
#     df = df.dropna()

#     if df.empty:
#         return {'error': 'All values are NaN.'}

#     # Make the prediction
#     y_pred = model.predict(df)

#     # Update the GUI with the prediction value
#     if df['aMagnitude'][0]<1:
#         prediction = "NO_ACTIVITY"
#     elif df['aMagnitude'][0]>1 and df['aMagnitude'][0]<4:
#         prediction = "WALKING"
#     else:
#         prediction = "JOGGING"

#     print(prediction)

#     prediction_label.config(text=prediction) # update the label with the prediction

#     root.mainloop() # start the GUI event loop

#     return str(y_pred[0])

# if __name__ == '__main__':
#     app.run(host='192.168.177.200', port=5000, debug=True)


# # Final
# import tkinter as tk
# from tkinter import ttk
# from tkinter.font import Font
# from PIL import Image, ImageTk
# from flask import Flask, request
# import joblib
# from flask_cors import CORS
# import pandas as pd
# import threading

# app = Flask(__name__)
# CORS(app)

# # Load the trained model from file
# with open('svm_model_new.pkl', 'rb') as f:
#     model = joblib.load(f)

# # Define a dictionary mapping each activity to its corresponding image file path
# activity_image_paths = {
#     'NO_ACTIVITY': 'img\NO_ACTIVITY.png',
#     'WALKING': 'img\WALKING.png',
#     'JOGGING': 'img\JOGGING.png'
# }

# # Create the GUI window and widgets
# root = tk.Tk()
# root.title("Activity Prediction")
# root.geometry("600x600")

# label = tk.Label(root, text="Predicted Activity:", font=Font(size=16))
# label.pack()

# prediction_label = tk.Label(root, text="", font=Font(size=20))
# prediction_label.pack()

# image_label = tk.Label(root)
# image_label.pack()

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the sensor data from the request
#     sensor_data = request.get_json()
#     print(sensor_data) # added to print the received data

#     # Create a pandas DataFrame from the sensor data
#     data = [[sensor_data['ax'], sensor_data['ay'], sensor_data['az'], sensor_data['gx'], sensor_data['gy'], sensor_data['gz'], sensor_data['aMagnitude'], sensor_data['gMagnitude']]]

#     df = pd.DataFrame(data, columns=['ax', 'ay', 'az', 'gx', 'gy', 'gz', 'aMagnitude', 'gMagnitude'])

#     # Remove any rows that contain NaN values
#     df = df.dropna()

#     if df.empty:
#         return {'error': 'All values are NaN.'}

#     # Make the prediction
#     y_pred = model.predict(df)
#     prediction = y_pred[0]

#     # Update the GUI with the prediction value
#     # if df['aMagnitude'][0]<1:
#     #     prediction = "NO_ACTIVITY"
#     # elif df['aMagnitude'][0]>1 and df['aMagnitude'][0]<4:
#     #     prediction = "WALKING"
#     # else:
#     #     prediction = "JOGGING"

#     print(prediction)

#     prediction_label.config(text=prediction) # update the label with the prediction
#     image_path = activity_image_paths.get(prediction)
#     if image_path:
#         image = Image.open(image_path)
#         image = image.resize((300, 350))
#         photo = ImageTk.PhotoImage(image)
#         image_label.configure(image=photo)
#         image_label.image = photo  # keep a reference to the photo to prevent garbage collection

#     return str(y_pred[0])

# def run_flask():
#     app.run(host='192.168.177.200', port=5000)

# if __name__ == '__main__':
#     # Start the Flask app in a separate thread
#     flask_thread = threading.Thread(target=run_flask)
#     flask_thread.start()

#     # Start the GUI event loop in the main thread
#     root.mainloop()


# # New Final
# import tkinter as tk
# from tkinter import ttk
# from tkinter.font import Font
# from PIL import Image, ImageTk
# from flask import Flask, request
# import joblib
# from flask_cors import CORS
# import pandas as pd
# import threading

# app = Flask(__name__)
# CORS(app)

# # Load the trained model from file
# with open('svm_model_new.pkl', 'rb') as f:
#     model = joblib.load(f)

# # Define a dictionary mapping each activity to its corresponding image file path
# activity_image_paths = {
#     'NO_ACTIVITY': 'img/NO_ACTIVITY.png',
#     'WALKING': 'img/WALKING.png',
#     'JOGGING': 'img/JOGGING.png'
# }

# # Create the GUI window and widgets
# root = tk.Tk()
# root.title("Activity Prediction")
# root.geometry("600x600")

# label = tk.Label(root, text="Predicted Activity:", font=Font(size=16))
# label.pack()

# prediction_label = tk.Label(root, text="", font=Font(size=20))
# prediction_label.pack()

# image_label = tk.Label(root)
# image_label.pack()

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the sensor data from the request
#     sensor_data = request.get_json()
#     print(sensor_data) # added to print the received data

#     # Create a pandas DataFrame from the sensor data
#     data = [[sensor_data['ax'], sensor_data['ay'], sensor_data['az'], sensor_data['gx'], sensor_data['gy'], sensor_data['gz'], sensor_data['aMagnitude'], sensor_data['gMagnitude']]]

#     df = pd.DataFrame(data, columns=['ax', 'ay', 'az', 'gx', 'gy', 'gz', 'aMagnitude', 'gMagnitude'])

#     # Remove any rows that contain NaN values
#     df = df.dropna()

#     if df.empty:
#         return {'error': 'All values are NaN.'}

#     # Make the prediction
#     y_pred = model.predict(df)
#     prediction = y_pred[0]

#     # Update the GUI with the prediction value
#     root.attributes('-topmost', 1) # make the GUI window the topmost window
#     prediction_label.config(text=prediction) # update the label with the prediction
#     image_path = activity_image_paths.get(prediction)
#     if image_path:
#         image = Image.open(image_path)
#         image = image.resize((300, 350))
#         photo = ImageTk.PhotoImage(image)
#         image_label.configure(image=photo)
#         image_label.image = photo  # keep a reference to the photo to prevent garbage collection
#     root.attributes('-topmost', 0) # remove the topmost attribute from the GUI window

#     return str(y_pred[0])

# def run_flask():
#     app.run(host='192.168.177.200', port=5000)

# if __name__ == '__main__':
#     # Start the Flask app in a separate thread
#     flask_thread = threading.Thread(target=run_flask, daemon=True)
#     flask_thread.start()

#     # Start the GUI event loop in the main thread
#     try:
#         root.mainloop()
#     except KeyboardInterrupt:
#         pass


# # Latest Final
# import tkinter as tk
# from tkinter import ttk
# from tkinter.font import Font
# from PIL import Image, ImageTk
# from flask import Flask, request
# import joblib
# from flask_cors import CORS
# import pandas as pd
# import threading

# app = Flask(__name__)
# CORS(app)

# # Load the trained model from file
# with open('svm_model_new.pkl', 'rb') as f:
#     model = joblib.load(f)

# # Define a dictionary mapping each activity to its corresponding image file path
# activity_image_paths = {
#     'NO_ACTIVITY': 'img/NO_ACTIVITY.png',
#     'WALKING': 'img/WALKING.png',
#     'JOGGING': 'img/JOGGING.png'
# }

# # Create the GUI window and widgets
# root = tk.Tk()
# root.title("Activity Prediction")
# root.geometry("600x630")

# # Set the background color and font
# root.configure(bg="#F0F0F0")

# # Define custom fonts
# title_font = Font(family="Helvetica", size=28, weight="bold")
# prediction_label_font = Font(family="Helvetica", size=18)
# prediction_value_font = Font(family="Helvetica", size=24, weight="bold")

# # Add a label for the title
# title_label = tk.Label(root, text="Activity Prediction", font=title_font, bg="#F2F2F2", fg="#006699")
# title_label.pack(pady=20)

# # Add a separator for visual separation
# separator = ttk.Separator(root, orient="horizontal")
# separator.pack(fill="x", pady=10)

# # Add a label for the predicted activity
# prediction_label = tk.Label(root, text="Predicted Activity:", font=prediction_label_font, bg="#F0F0F0", fg="#444444")
# prediction_label.pack()

# # Add a label for the prediction value
# prediction_value_label = tk.Label(root, text="", font=prediction_value_font, bg="#F0F0F0", fg="#006699")
# prediction_value_label.pack(pady=20)

# # Add a label for the activity image
# image_label = tk.Label(root, bg="#F0F0F0")
# image_label.pack(pady=10)

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the sensor data from the request
#     sensor_data = request.get_json()
#     print(sensor_data) # added to print the received data

#     # Create a pandas DataFrame from the sensor data
#     data = [[sensor_data['ax'], sensor_data['ay'], sensor_data['az'], sensor_data['gx'], sensor_data['gy'], sensor_data['gz'], sensor_data['aMagnitude'], sensor_data['gMagnitude']]]

#     df = pd.DataFrame(data, columns=['ax', 'ay', 'az', 'gx', 'gy', 'gz', 'aMagnitude', 'gMagnitude'])

#     # Remove any rows that contain NaN values
#     df = df.dropna()

#     if df.empty:
#         return {'error': 'All values are NaN.'}

#     # Make the prediction
#     y_pred = model.predict(df)
#     prediction = y_pred[0]

#     # Update the GUI with the prediction value
#     root.attributes('-topmost', 1) # make the GUI window the topmost window
#     prediction_value_label.config(text=prediction, fg="#006699") # update the label with the prediction
#     image_path = activity_image_paths.get(prediction)
#     if image_path:
#         image = Image.open(image_path)
#         image = image.resize((300, 350))
#         photo = ImageTk.PhotoImage(image)
#         image_label.configure(image=photo)
#         image_label.image = photo  # keep a reference to the photo to prevent garbage collection
#     root.attributes('-topmost', 0) # remove the topmost attribute from the GUI window
#     prediction_value_label.config(text=prediction, fg="#006699") # update the label with the prediction
#     image_path = activity_image_paths.get(prediction)
#     if image_path:
#         image = Image.open(image_path)
#         image = image.resize((300, 350))
#         photo = ImageTk.PhotoImage(image)
#         image_label.configure(image=photo)
#         image_label.image = photo  # keep a reference to the photo to prevent garbage collection
#     root.attributes('-topmost', 0) # remove the topmost attribute from the GUI window

#     return str(y_pred[0])

# def run_flask():
#     app.run(host='192.168.177.200', port=5000)

# if __name__ == '__main__':
#     # Start the Flask app in a separate thread
#     flask_thread = threading.Thread(target=run_flask, daemon=True)
#     flask_thread.start()

#     # Start the GUI event loop in the main thread
#     try:
#         root.mainloop()
#     except KeyboardInterrupt:
#         pass


# # Somehow percentage
# import tkinter as tk
# from tkinter import ttk
# import tkinter
# from tkinter.font import Font
# from PIL import Image, ImageTk
# from flask import Flask, request
# import joblib
# from flask_cors import CORS
# import pandas as pd
# import threading
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# app = Flask(__name__)
# CORS(app)

# # Load the trained model from file
# with open('svm_model_new.pkl', 'rb') as f:
#     model = joblib.load(f)

# # Define a dictionary mapping each activity to its corresponding image file path
# activity_image_paths = {
#     'NO_ACTIVITY': 'img/NO_ACTIVITY.png',
#     'WALKING': 'img/WALKING.png',
#     'JOGGING': 'img/JOGGING.png'
# }

# # Create the GUI window and widgets
# root = tk.Tk()
# root.title("Activity Prediction")
# root.geometry("800x630")

# # Set the background color and font
# root.configure(bg="#F0F0F0")

# # Define custom fonts
# title_font = Font(family="Helvetica", size=28, weight="bold")
# prediction_label_font = Font(family="Helvetica", size=18)
# prediction_value_font = Font(family="Helvetica", size=24, weight="bold")

# # Add a label for the title
# title_label = tk.Label(root, text="Activity Prediction", font=title_font, bg="#F2F2F2", fg="#006699")
# title_label.pack(pady=20)

# # Add a separator for visual separation
# separator = ttk.Separator(root, orient="horizontal")
# separator.pack(fill="x", pady=10)

# # Add a label for the predicted activity
# prediction_label = tk.Label(root, text="Predicted Activity:", font=prediction_label_font, bg="#F0F0F0", fg="#444444")
# prediction_label.pack()

# # Add a label for the prediction value
# prediction_value_label = tk.Label(root, text="", font=prediction_value_font, bg="#F0F0F0", fg="#006699")
# prediction_value_label.pack(pady=20)

# # Add a label for the activity image
# image_label = tk.Label(root, bg="#F0F0F0")
# image_label.pack(pady=10)

# # Add a canvas for the bar plot
# canvas = tk.Canvas(root, bg="#F0F0F0")
# canvas.pack(pady=10)


# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the sensor data from the request
#     sensor_data = request.get_json()
#     print(sensor_data) # added to print the received data

#     # Create a pandas DataFrame from the sensor data
#     data = [[sensor_data['ax'], sensor_data['ay'], sensor_data['az'], sensor_data['gx'], sensor_data['gy'], sensor_data['gz'], sensor_data['aMagnitude'], sensor_data['gMagnitude']]]

#     df = pd.DataFrame(data, columns=['ax', 'ay', 'az', 'gx', 'gy', 'gz', 'aMagnitude', 'gMagnitude'])

#     # Remove any rows that contain NaN values
#     df = df.dropna()

#     if df.empty:
#         return {'error': 'All values are NaN.'}

#     # Make the prediction
#     y_pred = model.predict(df)
#     prediction = y_pred[0]

#     activity_count = {
#         'NO_ACTIVITY': 0,
#         'WALKING': 0,
#         'JOGGING': 0
#     }

#     # Make the prediction and update the activity count
#     y_pred = model.predict(df)
#     prediction = y_pred[0]
#     activity_count[prediction] += 1
#     tot_per = activity_count["NO_ACTIVITY"] + activity_count["WALKING"] + activity_count["JOGGING"]

#     SITTInG_Per = (activity_count["NO_ACTIVITY"]*100)/tot_per
#     WALKING_Per = (activity_count["WALKING"]*100)/tot_per
#     JOGGING_Per = (activity_count["JOGGING"]*100)/tot_per

#     # Update the GUI with the prediction value
#     root.attributes('-topmost', 1) # make the GUI window the topmost window
#     prediction_value_label.config(text=prediction, fg="#006699") # update the label with the prediction
#     image_path = activity_image_paths.get(prediction)
#     if image_path:
#         image = Image.open(image_path)
#         image = image.resize((300, 350))
#         photo = ImageTk.PhotoImage(image)
#         image_label.configure(image=photo)
#         image_label.image = photo  # keep a reference to the photo to prevent garbage collection
#     root.attributes('-topmost', 0) # remove the topmost attribute from the GUI window
#     prediction_value_label.config(text=prediction, fg="#006699") # update the label with the prediction
#     image_path = activity_image_paths.get(prediction)
#     if image_path:
#         image = Image.open(image_path)
#         image = image.resize((300, 350))
#         photo = ImageTk.PhotoImage(image)
#         image_label.configure(image=photo)
#         image_label.image = photo  # keep a reference to the photo to prevent garbage collection
#     root.attributes('-topmost', 0) # remove the topmost attribute from the GUI window

#     # Create the data for the bar plot
#     activity_labels = ['NO_ACTIVITY', 'WALKING', 'JOGGING']
#     activity_percentages = [NO_ACTIVITY_Per, WALKING_Per, JOGGING_Per]

#     # Create the bar plot
#     fig, ax = plt.subplots()
#     ax.bar(activity_labels, activity_percentages)
#     ax.set_ylabel('Percentage')

#     # Display the plot
#     plt.show()

#     # Convert the plot to a Tkinter compatible image
#     canvas = FigureCanvasTkAgg(fig, master=root)
#     canvas.draw()

#     # Get the Tkinter image and display it in the GUI
#     tkinter_image = canvas.get_tk_widget()
#     tkinter_image.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#     return str(y_pred[0])

# def run_flask():
#     app.run(host='192.168.177.200', port=5000)

# if __name__ == '__main__':
#     # Start the Flask app in a separate thread
#     flask_thread = threading.Thread(target=run_flask, daemon=True)
#     flask_thread.start()

#     # Start the GUI event loop in the main thread
#     try:
#         root.mainloop()
#     except KeyboardInterrupt:
#         pass


# Latest Final
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
    app.run(host="192.168.177.200", port=5000)


if __name__ == "__main__":
    # Start the Flask app in a separate thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Start the GUI event loop in the main thread
    try:
        root.mainloop()
    except KeyboardInterrupt:
        pass


# # nearly final
# import tkinter as tk
# from tkinter import ttk
# from tkinter.font import Font
# from PIL import Image, ImageTk
# from flask import Flask, request
# import joblib
# from flask_cors import CORS
# import pandas as pd
# import threading

# app = Flask(__name__)
# CORS(app)

# # Load the trained model from file
# with open('svm_model_new.pkl', 'rb') as f:
#     model = joblib.load(f)

# # Define a dictionary mapping each activity to its corresponding image file path
# activity_image_paths = {
#     'NO_ACTIVITY': 'img/NO_ACTIVITY.png',
#     'WALKING': 'img/WALKING.png',
#     'JOGGING': 'img/JOGGING.png'
# }

# # Create the GUI window and widgets
# root = tk.Tk()
# root.title("Activity Prediction")
# root.geometry("600x630")

# # Set the background color and font
# root.configure(bg="#F0F0F0")

# # Define custom fonts
# title_font = Font(family="Helvetica", size=28, weight="bold")
# prediction_label_font = Font(family="Helvetica", size=18)
# prediction_value_font = Font(family="Helvetica", size=24, weight="bold")

# # Add a label for the title
# title_label = tk.Label(root, text="Activity Prediction", font=title_font, bg="#F2F2F2", fg="#006699")
# title_label.pack(pady=20)

# # Add a separator for visual separation
# separator = ttk.Separator(root, orient="horizontal")
# separator.pack(fill="x", pady=10)

# # Add a label for the prediction value
# prediction_value_label = tk.Label(root, text="", font=prediction_value_font, bg="#F0F0F0", fg="#006699")
# prediction_value_label.pack(pady=20)

# # Add a label for the activity image
# image_label = tk.Label(root, bg="#F0F0F0")
# image_label.pack(pady=10)

# def show_activity_window(activity, image_path):
#     if hasattr(root, 'activity_window'):
#         activity_window = root.activity_window
#         activity_window.title("Activity Prediction")
#         activity_window.geometry("400x500")
#         activity_label = activity_window.activity_label
#         activity_value_label = activity_window.activity_value_label
#         activity_image_label = activity_window.activity_image_label
#     else:
#         activity_window = tk.Toplevel(root)
#         root.activity_window = activity_window
#         activity_window.title("Activity Prediction")
#         activity_window.geometry("400x500")
#         activity_window.configure(bg="#F0F0F0")
#         activity_label = tk.Label(activity_window, text="Predicted Activity:", font=prediction_label_font, bg="#F0F0F0", fg="#444444")
#         activity_label.pack()
#         activity_value_label = tk.Label(activity_window, font=prediction_value_font, bg="#F0F0F0", fg="#006699")
#         activity_value_label.pack(pady=20)
#         activity_image_label = tk.Label(activity_window, bg="#F0F0F0")
#         activity_image_label.pack(pady=10)
#         activity_window.activity_label = activity_label
#         activity_window.activity_value_label = activity_value_label
#         activity_window.activity_image_label = activity_image_label

#     activity_value_label.configure(text=activity)

#     # Load the image
#     if image_path:
#         image = Image.open(image_path)
#         image = image.resize((300, 350))
#         photo = ImageTk.PhotoImage(image)
#         activity_image_label.configure(image=photo)
#         activity_image_label.image = photo  # keep a reference to the photo to prevent garbage collection

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the sensor data from the request
#     sensor_data = request.get_json()
#     print(sensor_data) # added to print the received data

#     # Create a pandas DataFrame from the sensor data
#     data = [[sensor_data['ax'], sensor_data['ay'], sensor_data['az'], sensor_data['gx'], sensor_data['gy'], sensor_data['gz'], sensor_data['aMagnitude'], sensor_data['gMagnitude']]]

#     df = pd.DataFrame(data, columns=['ax', 'ay', 'az', 'gx', 'gy', 'gz', 'aMagnitude', 'gMagnitude'])

#     # Remove any rows that contain NaN values
#     df = df.dropna()

#     if df.empty:
#         return {'error': 'All values are NaN.'}

#     # Make the prediction
#     y_pred = model.predict(df)
#     prediction = y_pred[0]

#     # Show the activity window
#     image_path = activity_image_paths.get(prediction)
#     show_activity_window(prediction, image_path)

#     return str(y_pred[0])

# # Add a button to predict the activity
# predict_button = tk.Button(root, text="Predict Activity", font=prediction_label_font, bg="#F2F2F2", fg="#006699", command=predict)
# predict_button.pack(pady=20)

# def run_flask():
#     app.run(host='192.168.177.200', port=5000)

# if __name__ == '__main__':
#     # Start the Flask app in a separate thread
#     flask_thread = threading.Thread(target=run_flask, daemon=True)
#     flask_thread.start()

#     # Start the GUI event loop in the main thread
#     try:
#         root.mainloop()
#     except KeyboardInterrupt:
#         pass


# # nearly final
# import tkinter as tk
# from tkinter import ttk
# from tkinter.font import Font
# from PIL import Image, ImageTk
# from flask import Flask, request
# import joblib
# from flask_cors import CORS
# import pandas as pd
# import threading

# app = Flask(__name__)
# CORS(app)

# # Load the trained model from file
# with open('svm_model_new.pkl', 'rb') as f:
#     model = joblib.load(f)

# # Define a dictionary mapping each activity to its corresponding image file path
# activity_image_paths = {
#     'NO_ACTIVITY': 'img/NO_ACTIVITY.png',
#     'WALKING': 'img/WALKING.png',
#     'JOGGING': 'img/JOGGING.png'
# }

# # Create the GUI window and widgets
# root = tk.Tk()
# root.title("Activity Prediction")
# root.geometry("600x630")

# # Set the background color and font
# root.configure(bg="#F0F0F0")

# # Define custom fonts
# title_font = Font(family="Helvetica", size=28, weight="bold")
# prediction_label_font = Font(family="Helvetica", size=18)
# prediction_value_font = Font(family="Helvetica", size=24, weight="bold")

# # Add a label for the title
# title_label = tk.Label(root, text="Activity Prediction", font=title_font, bg="#F2F2F2", fg="#006699")
# title_label.pack(pady=20)

# # Add a separator for visual separation
# separator = ttk.Separator(root, orient="horizontal")
# separator.pack(fill="x", pady=10)

# # Add a label for the prediction value
# prediction_value_label = tk.Label(root, text="", font=prediction_value_font, bg="#F0F0F0", fg="#006699")
# prediction_value_label.pack(pady=20)

# # Add a label for the activity image
# image_label = tk.Label(root, bg="#F0F0F0")
# image_label.pack(pady=10)

# def show_activity_window(activity, image_path):
#     if hasattr(root, 'activity_window'):
#         activity_window = root.activity_window
#         activity_window.title("Activity Prediction")
#         activity_window.geometry("400x500")
#         activity_label = activity_window.activity_label
#         activity_value_label = activity_window.activity_value_label
#         activity_image_label = activity_window.activity_image_label
#     else:
#         activity_window = tk.Toplevel(root)
#         root.activity_window = activity_window
#         activity_window.title("Activity Prediction")
#         activity_window.geometry("400x500")
#         activity_window.configure(bg="#F0F0F0")
#         activity_label = tk.Label(activity_window, text="Predicted Activity:", font=prediction_label_font, bg="#F0F0F0", fg="#444444")
#         activity_label.pack()
#         activity_value_label = tk.Label(activity_window, font=prediction_value_font, bg="#F0F0F0", fg="#006699")
#         activity_value_label.pack(pady=20)
#         activity_image_label = tk.Label(activity_window, bg="#F0F0F0")
#         activity_image_label.pack(pady=10)
#         activity_window.activity_label = activity_label
#         activity_window.activity_value_label = activity_value_label
#         activity_window.activity_image_label = activity_image_label

#     activity_value_label.configure(text=activity)

#     # Load the image
#     if image_path:
#         image = Image.open(image_path)
#         image = image.resize((300, 350))
#         photo = ImageTk.PhotoImage(image)
#         activity_image_label.configure(image=photo)
#         activity_image_label.image = photo  # keep a reference to the photo to prevent garbage collection

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the sensor data from the request
#     sensor_data = request.get_json()
#     print(sensor_data) # added to print the received data

#     # Create a pandas DataFrame from the sensor data
#     data = [[sensor_data['ax'], sensor_data['ay'], sensor_data['az'], sensor_data['gx'], sensor_data['gy'], sensor_data['gz'], sensor_data['aMagnitude'], sensor_data['gMagnitude']]]

#     df = pd.DataFrame(data, columns=['ax', 'ay', 'az', 'gx', 'gy', 'gz', 'aMagnitude', 'gMagnitude'])

#     # Remove any rows that contain NaN values
#     df = df.dropna()

#     if df.empty:
#         return {'error': 'All values are NaN.'}

#     # Make the prediction
#     y_pred = model.predict(df)
#     prediction = y_pred[0]

#     # Show the activity window
#     image_path = activity_image_paths.get(prediction)
#     show_activity_window(prediction, image_path)

#     return str(y_pred[0])

# predict_button = tk.Button(root, text="Predict Activity", font=prediction_label_font, bg="#F2F2F2", fg="#006699", command=predict)
# predict_button.pack(pady=20)

# def run_flask():
#     app.run(host='192.168.177.200', port=5000)

# if __name__ == '__main__':
#     # Start the Flask app in a separate thread
#     flask_thread = threading.Thread(target=run_flask, daemon=True)
#     flask_thread.start()

#     # Start the GUI event loop in the main thread
#     try:
#         root.mainloop()
#     except KeyboardInterrupt:
#         pass
