import gym
from gym import wrappers


env = gym.make('My3-v1')
env = wrappers.Monitor(env, '../warker_test/tmp/My3-v1-experiment-1',force=True)
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break