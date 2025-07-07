# 🚗 Best Cars Dealership – IBM Full Stack Capstone Project

This is the final capstone project for the IBM Full Stack Software Developer Professional Certificate. It is a full-stack web application to showcase car dealerships, view dealer reviews, and submit new reviews. The backend is built using Django, the frontend is built with React, and the reviews are analyzed using a sentiment analysis microservice.

---

## 📁 Project Structure
 
bestcars/  
├── djangoapp/ # Main Django app for dealership data   
├── pages/ # Static pages like Home, About, Contact  
├── server/ # Express + MongoDB microservice for dealer reviews  
├── client/ # React frontend application  
├── templates/ # HTML templates for Django  
├── static/ # CSS and images  
├── manage.py  
└── README.md  


---

## 🔧 Technologies Used

- 🐍 **Python** (Django)
- ⚛️ **React.js**
- ☁️ **IBM Cloud Code Engine** (for sentiment analysis)
- 🧾 **MongoDB** (for storing reviews)
- 🐳 **Docker** (for containerizing services)
- 🚀 **GitHub Actions** (for CI/CD)

---

## 📦 Setup Instructions

### ✅ Backend – Django

1. **Clone this repository:**
   ```bash
   git clone https://github.com/badalrai21/capstone-bestcars.git
   cd capstone-bestcars
   ```

2. **Create & activate virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
  ```bash
  pip install -r requirements.txt
```

4. **Run the Django server:**
  ```bash
  python manage.py runserver
  ```

5. **Access pages:**

  Home: http://localhost:8000/  

  About: http://localhost:8000/about/  

  Contact: http://localhost:8000/contact/  

  Login/Signup: http://localhost:8000/login/ or /signup/  

  Dealerships: http://localhost:8000/dealerships/  


### ✅ Frontend – React
  1. **Go to React app folder:**
  ```bash
  cd client
  ```

  2. **Install dependencies:**
  ```bash
  npm install
  ```

  3. **Start the frontend server:**
  ```bash
  npm start
  ```
  Visit: http://localhost:3000

### ✅ Microservices
  Sentiment Analysis: Hosted on IBM Code Engine (connects via proxy)  

  Dealer Review Service: Node.js Express API using MongoDB Atlas  

### 🧪 Features Implemented
 Static pages (Home, About, Contact)  

 Django models for CarMake, CarModel  

 Django admin interface for car data  

 JWT-based login/signup  

 Get dealerships from cloud function  

 Get dealer details with reviews  

 Post reviews to MongoDB  

 Sentiment analysis on reviews  

 React frontend integration  

 Docker & containerized backend/frontend  

 CI/CD GitHub Actions workflows  

 Project deployed to GitHub + IBM Cloud  

 
   ### 📃 License
   This project is licensed under the MIT License.
   
   ### 👤 Author
   Badal Kumar Rai  
   GitHub: [@badalrai21](https://github.com/badalrai21).  
   LinekdIn: [@BadalRai](https://www.linkedin.com/in/badal-rai)      
   Discord: Join our Discord Server [@NO2](https://discord.gg/Dnw4ZjEg)   


