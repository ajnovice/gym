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
	# cart observation have below attributes to describe the current statu of the evironment
	cart_position,cart_velocity,cart_poll_angle,cart_angular_velocity = observation
	"""
	the angle is measured off a straight vertical line from the cart which means if it starts to lean
	towards the right and getting a positive angle and it starts to lean towards the left off that vertical	
	line I get a negative angle.
	So if the pull angle is greater than zero then we know it's starting to lean towards the right.
	So if the pulls lean towards the right.Let's go ahead and move the cart towards the right.
	In an attempt to try to fix that.So we're going to say action is equal to 1	
	But if angle is less than zero, Well in that case we know that the angle is going to be negative meaning the pole is falling to the
	left.So we can try to move to the left.so we will say action is an equal to zero.
	"""
	if cart_poll_angle  > 0:
		action = 1
	else:
		action = 0
	# step return four variable which can be used to optimize the model
	observation,reward,don,info=env.step(action)


"""
What this is going to do is going to randomly sample from action space and then provide that step into the environment.
So we shouldn't actually see the pull balance we should eventually just see some sort of random sliding.
"""


