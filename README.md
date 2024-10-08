# Flask Knowledge Base Application

This is a Flask application that allows users to interact with a knowledge base through a web interface. Users can ask questions, receive answers based on a predefined knowledge base, and update the knowledge base with new question-answer pairs. It also include static assets such as CSS files and an images

## Features

- **Home Page**: Displays stored information and allows users to add or delete items.
- **Login Page**: Provides a login interface (currently not functional).
- **Quiz Page**: Displays a quiz interface.
- **About Page**: Shows information about the application.
- **Chat Page**: Allows users to ask questions and receive answers based on the knowledge base.
- **Update Knowledge**: Enables users to add new question-answer pairs to the knowledge base.
- Static assets including CSS and images.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Junate-World/Junate-Bot.git
   cd Junate-Bot

2.  Set up a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies.

pip install -r requirements.txt

4. Create a Knowledge Base File
Create a knowledge_base.json file in the root directory with the following content:

{
  "questions": []
}

Note: The program creates the knowledge base file if it doesn't exist.

6. Running the Application

Start the Flask Development Server

python chat3.py

7. Access the Application

Open your web browser and go to http://127.0.0.1:5000 to see the application in action.

8. API Endpoints

GET /: Home page.
POST /store: Add information to the storage.
GET /delete/int:index: Delete information from the storage.
GET /login: Login page (not functional).
GET /quiz: Quiz page (not functional).
GET /about: About page.
GET /chat: Chat page.
POST /chat: Receive answers based on user input.
POST /update_knowledge: Update the knowledge base with new question-answer pairs.

9. Development
To modify the application, you may need to edit the following files:

chat3.py: Main application code.
templates/: Directory containing HTML templates.

10. Contributing
Feel free to submit issues or pull requests. Please ensure your changes are well-documented and tested.
Please note that one of the major issue faced with this project is that it fails to fetch updated responses even after successfully updating the json file. The prompt kept on popping up requesting for update. The only way it manages to fetch updated responses is when the program is restarted.

11. License
This project is licensed under the MIT License. See the LICENSE file for details.

12. Contact
For any questions, you can contact the maintainer at [abel.ogbonna26@gmail.com].

Feel free to adjust any details to better fit your project or preferences!