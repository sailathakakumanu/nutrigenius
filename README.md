
---

# NutriGenius 🍏🤖

**NutriGenius** is a personalized diet planning web application that leverages **Generative AI** to create customized meal plans tailored to your health conditions, fitness goals, and dietary preferences. Built using **Django**, **Tailwind CSS**, and **Gemini AI**, NutriGenius delivers balanced, nutritious, and goal-oriented diet recommendations in a user-friendly interface.

***

## 🛠 Tech Stack

- **Frontend:** Tailwind CSS, HTML5  
- **Backend:** Django (Python)  
- **AI Integration:** Gemini AI API  
- **Database:** SQLite (default), easily switchable to MySQL/PostgreSQL  
- **APIs & Libraries:** Google Generative AI SDK  

***

## 🚀 Features

- **Personalized Health Profiles:** Input your age, weight, height, health conditions, fitness goals, and dietary preferences.
- **AI-Powered Meal Plans:** Get weekly meal plans tailored to your specific needs using **Gemini AI**.
- **Intuitive UI:** Clean, modern, and responsive design with **Tailwind CSS**.
- **Session Management:** Save and revisit generated meal plans without refilling the form.
- **Scalable Codebase:** Easily extendable for new features or integrations.

***

## 📝 Getting Started

### 1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/nutrigenius.git
cd nutrigenius
```

### 2. **Configure Gemini AI API**
- Sign up for [Google Cloud AI Studio](https://aistudio.google.com/).
- Generate your API key.
- Open `views.py` and configure your API key:
  ```python
  genai.configure(api_key="your_api_key_here")
  ```

### 3. **Run the Application**
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000` in your browser.

***

## 🔑 Key Components

- **`get_started.html`:** User form to input health profile.
- **`views.py`:** Handles form data, interacts with **Gemini AI**, and generates meal plans.
- **`forms.py`:** Manages form fields and validation.
- **`meal_plan.html`:** Displays AI-generated diet plans.

***

## 📧 Contact

For any inquiries or suggestions, feel free to reach out:

- **Email:** sailatha8724@gmail.com
- **GitHub:** [sailathakakumanu](https://github.com/sailathakakumanu)

---
