SMS Scam Detection System

1. Project Overview

The SMS Scam Detection System is a machine-learning-based web application designed to help users identify suspicious SMS messages. Users can enter a text message into the system, and the application analyses the message and displays a prediction indicating whether it is likely to be spam or ham (not spam).

The purpose of this project is to demonstrate how machine learning can support the identification of potentially fraudulent or unwanted text messages.

2. Project Objectives

To develop a simple web application for analysing SMS messages.

To train a machine learning model using a labelled SMS dataset.

To classify messages as spam or ham.

To provide users with a simple interface for testing messages.

3. Main Features

Message Input: Allows users to enter an SMS message.

Machine Learning Classification: Analyses the message using a trained model.

Prediction Results: Displays the predicted message category.

Simple User Interface: Provides an easy-to-use interface for testing SMS messages.

4. Technologies Used

Python – Main programming language.

Flask – Web application framework.

Scikit-learn – Machine learning and text classification.

Pandas – Dataset processing.

HTML and CSS – Web interface design.

Joblib – Saving and loading the trained model.

5. Dataset

The system uses the SMS Spam Collection dataset, which contains labelled SMS messages classified as spam or ham. The dataset is used to train the machine learning model.

The dataset contains general SMS examples and may not represent every type of scam message used in Malawi.

6. Project Structure

sms_scam_detection/
│
├── app.py
├── train_model.py
├── sms_model.joblib
├── requirements.txt
├── README.md
│
├── data/
│   └── SMSSpamCollection
│
└── templates/
    └── index.html

Note: This structure assumes these files and folders are included in the repository. Adjust it if your actual project structure is different.

7. How to Run the System

Step 1: Install Python

Install a compatible version of Python on your computer.

Step 2: Install the required packages

Open a terminal in the project folder and run:

pip install -r requirements.txt

Step 3: Start the application

Run:

python app.py

Step 4: Open the application

Open a web browser and visit:

http://127.0.0.1:5000

Enter an SMS message into the input field and submit it to view the prediction.

8. Example Messages for Testing

Example 1 — Potential spam

Congratulations! You have won a free prize. Click this link now to claim your reward!

Example 2 — Ordinary message

Hi, are we still meeting at 10 tomorrow? Please let me know.

The predictions depend on the trained model and the messages it learned from the dataset.

9. Limitations

The system may incorrectly classify some legitimate or suspicious messages.

Its performance depends on the quality and variety of the training dataset.

The dataset may not cover all scam patterns, local languages, or common fraud techniques in Malawi.

A spam prediction does not prove that a message is fraudulent, and a ham prediction does not guarantee that it is safe.

The application is intended as a screening aid, not a guarantee of message safety.

10. Future Improvements

Add more scam examples relevant to Malawi.

Improve the model's ability to identify local scam patterns and language variations.

Evaluate the model using additional performance measures.

Deploy the application online so users can access it through the internet.

11. Academic Use

This project demonstrates the application of machine learning and web development to SMS spam classification. It is intended for educational and research purposes.
