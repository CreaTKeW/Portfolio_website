# Damian Ptaszkiewicz - Personal Portfolio Website

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

A dynamic and responsive personal portfolio website built with Python and Flask. This project showcases my skills and projects at the intersection of data analysis and web development. It features sections detailing my background, skills, projects, and a functional contact form for inquiries.

## ✨ Features

* **Responsive Design:** Adapts seamlessly to various screen sizes using Bootstrap 5 (dark theme).
* **Multi-Page Layout:** Includes Home, About Me, Projects, and Contact pages.
* **Interactive Skills Display:** 'About Me' page features hoverable categories revealing specific skills.
* **Dynamic Navigation:** Sticky navigation bar that hides on scroll-down and reappears on scroll-up.
* **Functional Contact Form:** Allows visitors to send messages directly via email (powered by Flask-Mail).
* **Smooth Animations:** Subtle CSS animations for gradient backgrounds and element transitions.
* **Clean Codebase:** Built with a standard Flask application structure for maintainability.

## 🛠️ Technologies & Skills

### Backend
* **Python 3**
* **Flask:** Micro web framework.
* **Flask-WTF:** Form handling and validation.
* **Flask-Mail:** Email sending for the contact form.
* **Jinja2:** Templating engine.

### Frontend
* **HTML5**
* **CSS3:** Custom styles and animations.
* **JavaScript:** DOM manipulation for dynamic navbar behavior.
* **Bootstrap 5:** Frontend component library.
* **Google Fonts:** "Inter" font family.

### Tools & Concepts
* **Git & GitHub:** Version control.
* **Virtual Environments:** Dependency management (`venv`).
* **Environment Variables:** Secure configuration management (`python-dotenv`).
* **SMTP:** Email protocol used via Gmail.
* **OOP Principles** (Mentioned in skills)
* **UI/UX Considerations** (Mentioned in skills)

### Key Skills Highlighted
* **Data Science & Analysis:** Pandas, NumPy, Scikit-learn, Plotly, Seaborn, Matplotlib.
* **Web Development:** Python, Flask, HTML, CSS, Bootstrap, API Integration.
* **Databases/Other:** SQL, Selenium.

## 📂 Project Structure

The project follows a standard Flask application structure:

```plaintext
.
├── app/                    # Main Flask application package
│   ├── static/             # Static assets (CSS, JS, images)
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── img/
│   │   │   ├── morse_app.png
│   │   │   ├── multi_regression.jpg
│   │   │   ├── profile.jpeg
│   │   │   ├── space.jpg
│   │   │   ├── space_analysis.png
│   │   │   └── tic.png
│   │   └── js/
│   │       └── script.js
│   ├── templates/          # HTML templates (Jinja2)
│   │   ├── about.html
│   │   ├── base.html
│   │   ├── contact.html
│   │   ├── index.html
│   │   └── projects.html
│   ├── __init__.py         # Application factory
│   ├── forms.py            # WTForms definitions
│   └── routes.py           # Application routes and view logic
├── .env                    # Environment variable file (!!! NOT IN GIT !!!)
├── .gitignore              # Specifies intentionally untracked files
├── config.py               # Configuration settings class
├── LICENSE                 # Project license file (MIT)
├── requirements.txt        # Python package dependencies
└── run.py                  # Script to run the Flask application
```

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.x
* pip (Python package installer)
* Git

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/CreaTKeW/Portfolio_website.git
    cd Portfolio_website
    ```
2.  **Create and activate a virtual environment:**
    * On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up environment variables:**
    Create a file named `.env` in the project's root directory and add the following variables:
    ```env
    # Flask Secret Key (generate a random string)
    SECRET_KEY='your_very_secret_flask_key'

    # Gmail SMTP Configuration
    MAIL_USERNAME='your_email@gmail.com'
    # IMPORTANT: Use a Gmail App Password, not your regular password!
    # See: (https://support.google.com/accounts/answer/185833)
    MAIL_PASSWORD='your_gmail_app_password'

    # Email address to receive messages from the contact form
    MAIL_RECIPIENT='recipient_email@example.com'
    ```
    **Note on `MAIL_PASSWORD`:** For security reasons, Gmail requires using "App Passwords" for applications accessing your account via SMTP. You need to enable 2-Step Verification for your Google Account and then generate an App Password.

5.  **Run the application:**
    ```bash
    flask run
    ```
    Alternatively, you can use:
    ```bash
    python run.py
    ```
    The application should now be running on `http://127.0.0.1:5000/` (or the default Flask port).

## 🖼️ Projects Showcase (Inferred)

* House Price Prediction Model
* Space Race Data Analysis
* Interactive Tic Tac Toe with a graphical user interface.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Damian Ptaszkiewicz**

* **LinkedIn:** [linkedin.com/in/ptaszkiewicz](https://www.linkedin.com/in/ptaszkiewicz/)
* **GitHub:** [@CreaTKeW](https://github.com/CreaTKeW)
