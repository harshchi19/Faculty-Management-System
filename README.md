## FacultyFlo - Faculty Management System
The FacultyFlo web application aims to simplify administrative and communication processes within educational institutions. It provides a user-friendly interface for faculty members to log in, submit leave applications, access essential tools and applications, and interact with an AI-powered chatbot for assistance.

**Table of Contents**


-Features
-Installation
-Usage
-Support
-Contributing
-License

## Features

- **App Hub:** Simplify app management by accessing and utilizing teaching apps from a centralized hub.
- **Chatbot:** Instantly get answers and support through an AI assistant, allowing you to focus more on your students.
- **Colleague Connect:** Enhance collaboration by connecting with colleagues, sharing resources, and learning from each other's expertise.
- **Course Planner:** Organize lessons, materials, and assessments in one central location to simplify curriculum creation.
- **Smart Scheduling:** Stay organized with a smart calendar that automates tasks, schedules meetings, and provides reminders.
- **Task Management:** Keep focused with a to-do list that helps manage deadlines and prioritize tasks with ease.
- **Institution Login:** Faculty members can log in securely using their credentials to access the application's features.
- **Leave Application Submission:** Faculty members can submit leave applications through the web interface, providing details such as the description, start date, and end date.
- **Access to Tools and Applications:** The application provides links to various tools and applications commonly used in educational settings, such as Microsoft and Google apps, as well as other useful websites.
- **AI-Powered Chatbot:** Users can interact with an AI-powered chatbot to get assistance with various queries and tasks.


## Installation

To run FacultyFlo locally, follow these steps:

1. Clone this repository.
   ```bash
   git clone https://github.com/harshchi19/Faculty-Management-System.git
   ```

2. Navigate into the project directory.
   ```bash
   cd FacultyFlo
   ```

3. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations.
   ```bash
   python manage.py migrate
   ```

5. Start the development server.
   ```bash
   python manage.py runserver
   ```

6. Access the application in your browser at `http://localhost:8000`.

## Community Chatroom

### chatroom_faculty
This HTML file extends the sidebar layout for faculty members. It provides a form with an image for the community space.

### chatroom_hod 
Similar to `chatroom_faculty.html`, this HTML file extends the sidebar layout for Head of Departments (HODs). It also provides a form with an image for the community space.

## User Choice Page

### Choice System
The `choice.html` file presents a choice page for users to select their role between faculty and admin. It features navigation links to meet the team and support, along with a button to reach out.

## Leave Application Form

### leave_application system
This HTML file is a form for creating leave applications. It includes fields for description, start date, and end date. The form is submitted using JavaScript and includes CSRF token protection.


## Usage

Once the server is running, you can explore the FacultyFlo application by navigating to different sections using the provided links in the navigation bar. Feel free to interact with the features and explore how FacultyFlo can simplify your faculty management tasks.

## Support

For any inquiries or support, please contact us:

- **Phone:** +919820904940
- **Email:** facultyflo.care@gmail.com

## Contribution

-Harsh Chitaliya
-Deep Jain 
- Gaurav Singh Khati
- Atharva Patkar


## License
This project is licensed under the **MIT License**.
