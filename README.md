# AI Blog Generator (Python)
A Python-based command-line application that generates blog paragraphs using AI by integrating external APIs and secure environment variable handling.

## Features
- Generate AI-powered blog paragraphs from user input
- Interactive command-line interface
- Secure API key handling using environment variables
- Configurable creativity and response length
- Clean and modular Python code

## Tech Stack
- Python
- OpenAI API
- Environment Variables
- CLI Application

## Project Structure
ai-blog-generator/
├── blog_generator.py
├── README.md
├── .gitignore

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/your-username/ai-blog-generator.git

### 2. Install dependencies
pip install openai

### 3. Set environment variable
Windows:
setx OPENAI_API_KEY "your_api_key_here"

Linux/Mac:
export OPENAI_API_KEY="your_api_key_here"

### 4. Run the application
python blog_generator.py

## Example Usage
Write a paragraph? (Y/N): Y  
Topic: Artificial Intelligence  

Generated Paragraph:
AI-generated content...

## Security
- API keys are stored securely using environment variables
- Secrets are not hardcoded or committed to GitHub

## Learning Outcomes
- API integration in Python
- Secure environment variable management
- Error handling and debugging
- Writing clean and modular Python code

