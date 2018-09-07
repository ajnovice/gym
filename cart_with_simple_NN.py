import tensorflow as tf 
import gym
import numpy as np 

num_inputs = 4
num_hidden = 4
num_outputes = 1

initializer = tf.contrib.layers.variance_scaling_initializer()
X = tf.placeholder(tf.float32,shape=[None,num_inputs])
hiddeen_layer_one = tf.layers.dense(X,num_hidden,activation=tf.nn.relu,kernel_initializer=initializer)
hiddeen_layer_two = tf.layers.dense(hiddeen_layer_one,num_hidden,activation=tf.nn.relu,kernel_initializer=initializer)
output_layer = tf.layers.dense(hiddeen_layer_two,num_outputes,activation=tf.nn.sigmoid,kernel_initializer=initializer)
probabilities = tf.concat(axis=1,values=[output_layer,1-output_layer])
action = tf.multinomial(probabilities,num_samples=1)
init = tf.global_variables_initializer()

episode = 50
step_limit = 100
env = gym.make('CartPole-v0')
avg_steps = list()
with tf.Session() as sess:
	init.run()
	for _ in range(episode):
		obs = env.reset()
		for step in range(step_limit):
			action_value = action.eval(feed_dict={X:obs.reshape(1,num_inputs)})
			obs,reward,done,infor=env.step(action_value[0][0])

			if done:
				avg_steps.append(step)
				print("Cart Pole fell after {} steps".format(step))
				break
print("After {} episodes, average steps per game are {}".format(episode,np.mean(avg_steps)))

