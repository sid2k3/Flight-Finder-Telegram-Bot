# Flight-Finder-Telegram-Bot
This is a telegram bot written in python which enables users to find
flights (domestic/international) with the most economical prices.  
  
# Steps to create your own version of this bot
1) Get a secure access token by creating a new bot on telegram using BotFather.  
For more info https://core.telegram.org/bots
2) Replace the bot id in the code by the token you received in step1 or create a keys.env file and add "telegram_bot_id= your_token" this line.  
3) For getting flight data you will need to access the tequila API, to do that first register on the site https://tequila.kiwi.com/portal/login.  
Now login into your account and go to my solutions tab and create a online booking solution, complete all the steps and you'll get an API key.  
4) Replace the API_KEY and FLIGHT_API_KEY by the key you received in step2 or add this entry to your keys.env file "API_KEY=your_api_key"
5) Run main.py
6) Find your bot on telegram using the username of the bot which you would have received in step1.  
7) Message /help to the bot to get started.
