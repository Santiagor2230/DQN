import torch
from torch import Tensor, nn 

class DQN(nn.Module):

  def __init__(self, hidden_size, obs_size, n_actions): #[q1, q2, q3]
    super().__init__()
    self.net = nn.Sequential(
        nn.Linear(obs_size, hidden_size),
        nn.ReLU(),
        nn.Linear(hidden_size, hidden_size),
        nn.ReLU(),
        nn.Linear(hidden_size, n_actions)
    )

  def forward(self, x):
    return self.net(x.float())
