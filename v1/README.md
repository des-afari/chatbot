# Keyword Based Chatbot
This project is a simple rule-based chatbot designed to provide instant responses based on specific keywords found in user inputs.

## How It Works
The chatbot uses a dictionary to map keywords to responses. When a user inputs a message, the chatbot scans for keywords and returns the corresponding response. If no keywords are found, a default message is returned.

## Example Interactions
#### Greetings
**You**: "Hi" \
**Chatboot**: "Hello! How can I assist you today?"

#### Weather
**You**: "What's the weather like?" \
**Chatbot**: "Today's weather is sunny with a high of 75°F."

#### Reminders
**You**: "Set a reminder for my meeting at 3 PM." \
**Chatbot**: "Got it, I'll remind you to do that at the specified time."

## Getting Started
To run the chatbot, simply clone this repository and execute the Python script:

```
git clone https://github.com/des-afari/chatbot.git
cd v1
python chatbot.py
```