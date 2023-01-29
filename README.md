# my_chat_buddy
my_chat_buddy is a chat bot based on a machine learning framework called rasa.
# How to use 
Install Rasa with python version 3.8 or 3.7
Install MiniConda

After installing miniconda, Follow below commands to create a virtual environment in conda. This will allow you to run Rasa without errors.

 "conda install python=3.6"
  
  "conda create -n rasa python=3.6"
  
  "source activate rasa"
  
After this, clone the repository in vs code and open chatbuddy folder.
Now open a new terminal and run the command "rasa train" to train the model.
Once the model is trained, split the terminal and run "rasa run actions" in one terminal.
Once the action server is up and running, you have to run the command "rasa shell" in another terminal to speak to the bot.
Now you can talk to the bot.
this bot will give u motivational quotes and jokes as well.
