import gym
from gym.wrappers import RecordVideo, RecordEpisodeStatistics, TimeLimit


def create_envrionment(name):
  env = gym.make(name)
  env = TimeLimit(env, max_episode_steps=400) #episode is cut at 400 so needs to do things quicker
  env = RecordVideo(env, video_folder='./videos', episode_trigger=lambda x: x % 50 == 0)
  env = RecordEpisodeStatistics(env) #keep track of the reward
  return env