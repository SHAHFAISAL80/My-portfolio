from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    intro = {
        "name": "Shah Faisal",
        "title": "Computer Vision & AI Expert",
        "email": "shahfaisal15401@gmail.com",
        "whatsapp": "+923125094307",
        "github": "SHAHFAISAL80",
        "instagram": "shahfaisal1628",
        "linkedin": "Shah Faisal",
        "twitter": "faisal806784"
    }
    return render_template('index.html', intro=intro)

@app.route('/projects')
def projects():
    projects = [
        {"title": "AI-Powered Fight Detection", "video": r"videos\fight.mp4", "desc": "Real-time violent activity detection using YOLOv11 for object detection and LSTM for sequential classification. Enhances public safety in places like malls and schools with instant alerts."},
        {"title": "Cricket Fielding Analytics", "video": r"videos\cricket.mp4", "desc": "Inspired by Glenn Phillips’ catches, this AI system uses YOLO for real-time tracking of ball, batsman, bowler, and fielder, plus pose estimation to analyze reflexes and optimize fielding strategies."},
        {"title": "Exam Cheating Detection", "video": r"videos\cheating.mp4", "desc": "AI-driven model for online exams using YOLO and LSTM to detect suspicious behaviors like 'Looking Around' or 'Talking,' ensuring academic integrity with real-time alerts."},
        {"title": "Retail Theft Detection", "video": r"videos\retail.mp4", "desc": "Advanced system combining YOLO for object detection and LSTM for behavior sequence analysis to predict and prevent retail theft, reducing false alarms and improving loss prevention."}
    ]
    return render_template('projects.html', projects=projects)

@app.route('/experience')
def experience():
    experiences = [
        {"company": "D2AI.ca Inc. (Canada)", "role": "Computer Vision Engineer", "desc": "AI-powered vision applications, object detection & tracking."},
        {"company": "InLights (Pakistan)", "role": "AI Developer", "desc": "Facial recognition, biometric authentication using CNNs & GANs."},
        {"company": "Vital Tech Ind. (Brazil)", "role": "AI Specialist", "desc": "AI for autonomous vehicles and smart city projects."},
        {"company": "Rapidev (Pakistan)", "role": "Computer Vision Engineer", "desc": "Medical imaging and anomaly detection with PyTorch & TensorFlow."},
        {"company": "SITEL BRA (Brazil)", "role": "AI Engineer", "desc": "Object detection and real-time processing on edge devices."},
        {"company": "INOVA (Belgium)", "role": "ML Engineer", "desc": "Image classification, action recognition, reinforcement learning."},
        {"company": "RMIT University (Australia)", "role": "Researcher", "desc": "Eye tracking research using CNNs & Transformers."},
        {"company": "EWS USA Bank (USA)", "role": "Data Analyst", "desc": "Tableau development and predictive analytics."},
        {"company": "Venture Forward LLC (UAE)", "role": "AI Developer", "desc": "AI-driven business intelligence software."},
        {"company": "Cloudlem Pvt Ltd (USA)", "role": "Data Scientist", "desc": "Big data, NLP, and predictive modeling."},
        {"company": "Freelancing", "role": "Computer Vision & AI Expert", "desc": "Object detection, pose estimation, OCR, GANs, and AI automation."}
    ]
    return render_template('experience.html', experiences=experiences)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)