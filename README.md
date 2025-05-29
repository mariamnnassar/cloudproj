

````markdown
# 🕵️‍♀️ Fraud Detection Web App with Flask & Machine Learning

This project is a simple web application that uses a pre-trained Isolation Forest machine learning model to detect fraudulent transactions based on user input features.

## 🌐 Live Demo

The app is deployed and accessible via [Render](https://cloudproj-5.onrender.com/)

---

## 📦 Project Structure

```plaintext
📁 project-root/
│
├── app.py                  # Flask backend with ML model and API
├── model/
│   └── isolation_forest.joblib  # Pre-trained ML model
├── templates/
│   └── index.html          # Frontend HTML file
├── static/
│   └── script.js           # JavaScript to connect frontend to backend
├── requirements.txt        # Python dependencies
└── README.md               # Project description
````

---

## 🔧 Key Technologies

* **Python**
* **Flask**: Web framework to build RESTful API.
* **Flask-CORS**: Handle cross-origin requests from frontend to backend.
* **JavaScript (Fetch API)**: To send/receive data between client and server.
* **HTML/CSS**: For the frontend interface.
* **Machine Learning Model**: Isolation Forest (trained locally).
* **Render**: For deploying the Flask API and making it publicly accessible.

---

## 📋 Features

* Takes input for transaction-related features.
* Sends data to backend via REST API.
* Returns prediction: "Fraud" or "Legit".
* Real-time interaction between client and deployed ML model.

---

## 🧪 Local Development

1. Clone the repository:

   ```bash
   git clone https://github.com/mariamnnassar/cloudproj
   cd your-repo-name
   ```

2. Create virtual environment and activate:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app locally:

   ```bash
   python app.py
   ```

5. Open `index.html` in browser and test it locally.


## 🚀 Deployment

* The Flask backend and model were deployed using **Render Cloud Platform**.
* Start command on Render:

  ```bash
  gunicorn app:app
  ```
* Model hosted and served through `/predict` endpoint using RESTful API.


## 🧠 Authors

* Mariam Nassar 
* Aseel Sharsher
* Arwa Abulaila
* Rahaf Habaybeh
  University of Jordan


## 📌 Notes

* We used a REST API approach to connect the frontend to the backend.
* The app uses JSON for data exchange between client and server.
* Tested locally using virtual environment before deployment.

