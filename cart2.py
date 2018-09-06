#import openai gym library
import gym
# choose an environment from environment available from gym library
env = gym.make('CartPole-v0')
# make the car at zero level(shift the environment at default starting stage)
observation=env.reset()

"""
for some 1000 times steps we're going to do is we're going to render the environment and rendering
the environment basically creates this little pop up that allows you to view the environmentusing available sample space
"""

for _ in range(1000):
	env.render()
	action = env.action_space.sample()
	# step return four variable which can be used to optimize the model
	observation,reward,don,info=env.step(action)


"""
What this is going to do is going to randomly sample from action space and then provide that step into the environment.
So we shouldn't actually see the pull balance we should eventually just see some sort of random sliding.
"""


