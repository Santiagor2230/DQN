# DQN
Implementation of Deep Q Nework

# Requirements
gym == 0.22.0

gym[box2d] == 2.3.5

pytorch-lightining == 1.6.0

pyglet == 1.5.27

torch == 2.0.1

# collab installations
!apt-get install -y xvfb
!pip install \
    gym \
    gym[box2d] \
    pytorch-lightning==1.6.0 \
    pyglet==1.5.27 \
    pyvirtualdisplay
    
#if issues with box2d use this installation before:
!apt install swig

# Description
DQN is a deep neural model created through the works of Q table in order to approximate predictions to a continous state space , this implementation allows us to map each state with their predicted return based on each action. Rewards are used to compared and find the loss of the DQN in order to get to the most optimal path in the game that will maximize the rewards that the agent can obtain.

# Game
Lunar Landing

# Architecture
Regular DQN

# optimizer
AdamW

# loss function
smooth L1 loss function

# Video Result:

https://github.com/Santiagor2230/DQN/assets/52907423/97015acb-87b4-4627-b04c-60614582f3b3



https://github.com/Santiagor2230/DQN/assets/52907423/43edaeb3-0754-46f0-a4fc-86110e8e6aac

