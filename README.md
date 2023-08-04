# Flask Contact Form Project

This is a simple Flask web application that allows users to submit a contact form with their name, email, and message. The submitted messages are displayed on a separate page.

## Table of Contents

- [Getting Started](#getting-started)
 - [Prerequisites](#prerequisites)
 - [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before running the application, you need to have the following installed:

- Python 3.x
- Flask (You can install it using pip: `pip install Flask`)
- Flask-WTF (You can install it using pip: `pip install Flask-WTF`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/flask-contact-form.git
2. Change to the project directory:

       cd flask-contact-form
3. Create a virtual environment (optional but recommended):

        python -m venv venv
        source venv/bin/activate  
        # For Windows, use: venv\Scripts\activate
4. Install the required dependencies:

        pip install -r requirements.txt
## Usage
To run the application, use the following command:
    
    python app.py
    
Visit http://localhost:5000 in your web browser to access the home page. You can navigate to the contact form page and submit messages through the form. The submitted messages will be displayed on the messages page.

## Features
- Simple contact form with name, email, and message fields.
- Client-side validation using JavaScript to check for empty fields and valid email format.
- Displaying submitted messages on a separate page.
## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
