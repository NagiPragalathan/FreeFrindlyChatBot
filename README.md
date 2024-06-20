# FreeFriendlyChatBot

FreeFriendlyChatBot is an open-source chatbot framework designed to facilitate the creation of friendly and interactive chatbots. The framework is developed using Python and leverages natural language processing (NLP) techniques to understand and respond to user queries effectively.

## Overview

FreeFriendlyChatBot provides a flexible and easy-to-use platform for building chatbots that can be integrated into various applications. It supports a wide range of functionalities, including basic conversational abilities, custom responses, and integration with external APIs for enhanced capabilities.

## Features

- **User-Friendly Interface**: Simple and intuitive interface for both developers and users.
- **Customizable Responses**: Easily define and customize responses to user queries.
- **NLP Integration**: Leverage natural language processing to understand and process user inputs.
- **API Integration**: Integrate with external APIs to extend the chatbot's functionality.
- **Multi-Language Support**: Support for multiple languages to cater to a diverse user base.
- **Extensible**: Easily extend and add new features to the chatbot as needed.

## Technologies Used

- **Backend**: Python, Flask
- **Natural Language Processing**: NLTK (Natural Language Toolkit)
- **Database**: SQLite3
- **APIs**: Integration with various external APIs for added functionalities

## Installation and Setup

### Prerequisites

- Python 3.x
- pip (Python Package Installer)

### Steps

1. **Clone the Repository**
    
    bash
    
    Copy code
    
    `git clone https://github.com/NagiPragalathan/FreeFriendlyChatBot.git
    cd FreeFriendlyChatBot` 
    
2. **Install Dependencies**
    
    bash
    
    Copy code
    
    `pip install -r requirements.txt` 
    
3. **Run the Chatbot Server**
    
    bash
    
    Copy code
    
    `python app.py` 
    
4. **Access the Chatbot**
    
    Open your browser and navigate to `http://localhost:5000` to start interacting with the FreeFriendlyChatBot.
    

## Project Structure

arduino

Copy code

`FreeFriendlyChatBot/
├── app.py
├── chatbot/
│   ├── __init__.py
│   ├── bot.py
│   ├── responses.py
│   └── training_data.py
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── requirements.txt
└── README.md` 

## Usage

- **Customizing Responses**: Modify the `responses.py` file to customize the bot's responses to various queries.
- **Training Data**: Update the `training_data.py` file to add new phrases and improve the bot's understanding of user inputs.
- **API Integration**: Use the `bot.py` file to integrate external APIs for additional functionalities.

## Contribution

Contributions to the FreeFriendlyChatBot project are welcome! If you would like to contribute, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](https://chatgpt.com/c/LICENSE) file for details.
