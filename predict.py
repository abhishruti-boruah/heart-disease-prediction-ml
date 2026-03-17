import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

print("Enter patient details")

age = int(input("Age: "))
sex = int(input("Sex (1=Male, 0=Female): "))
cp = int(input("Chest Pain Type (0-3): "))
trestbps = int(input("Resting Blood Pressure: "))
chol = int(input("Cholesterol: "))
fbs = int(input("Fasting Blood Sugar >120 (1=True,0=False): "))
restecg = int(input("Resting ECG (0-2): "))
thalach = int(input("Maximum Heart Rate: "))
exang = int(input("Exercise Induced Angina (1=Yes,0=No): "))
oldpeak = float(input("ST depression: "))
slope = int(input("Slope (0-2): "))
ca = int(input("Number of major vessels (0-3): "))
thal = int(input("Thal (1=normal,2=fixed defect,3=reversible defect): "))

features = np.array([[age,sex,cp,trestbps,chol,fbs,restecg,
                      thalach,exang,oldpeak,slope,ca,thal]])

prediction = model.predict(features)

if prediction[0] == 1:
    print("Prediction: Heart Disease Detected")
else:
    print("Prediction: No Heart Disease Detected")
