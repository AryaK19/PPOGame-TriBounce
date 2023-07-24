# PPOGame-TriBounce
This repo contains a CNN and MLP Based algorithm ands a trained model for the game Tri-Bounce all the game files 

I considered using the OpenAi's GYM for this project.
for MLP I used PPO-mlpPolicy where states where basically a (6,) list containing the player position and 4 enemies positions
for CNN I used PPO-cnnPolicy where states where a numpy array of the pixels of each frame

rewards where based on the player progress

by looking at the code u can find the model implimentation and etc.

here is how u can navigate through:
The 'TriBounce' folder contail the raw game (which can be played my palyer )

The 'RL in Tribaounce' folder contains the CNN and MLP based algos/scouce code in a jupiter file format
In MLP The '200k_Reward.zip' model is the best model of all which is already loaded in MLP file
CNN is still under development....
