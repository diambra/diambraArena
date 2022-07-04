import diambra.arena
from diambra.arena.utils.gym_utils import show_wrap_obs

# Gym wrappers settings
wrappers_settings = {}

# Number of no-Op actions to be executed
# at the beginning of the episode (0 by default)
wrappers_settings["no_op_max"] = 0

# Number of steps for which the same action should be sent (1 by default)
wrappers_settings["sticky_actions"] = 1

# Frame resize operation spec (deactivated by default)
# WARNING: for speedup, avoid frame warping wrappers,
#          use environment's native frame wrapping through
#          "frameShape" setting (see documentation for details).
wrappers_settings["hwc_obs_resize"] = [128, 128, 1]

# Wrapper option for reward normalization
# When activated, the reward normalization factor can be set (default = 0.5)
# The normalization is performed by dividing the reward value
# by the product of the factor times the value of the full health bar
# reward = reward / (C * fullHealthBarValue)
wrappers_settings["reward_normalization"] = True
wrappers_settings["reward_normalization_factor"] = 0.5

# If to clip rewards (False by default)
wrappers_settings["clip_rewards"] = False

# Number of frames to be stacked together (1 by default)
wrappers_settings["frame_stack"] = 4

# Frames interval when stacking (1 by default)
wrappers_settings["dilation"] = 1

# How many past actions to stack together (1 by default)
wrappers_settings["actions_stack"] = 12

# If to scale observation numerical values (deactivated by default)
wrappers_settings["scale"] = True

# Scaling interval (0 = [0.0, 1.0], 1 = [-1.0, 1.0])
wrappers_settings["scale_mod"] = 0

env = diambra.arena.make("doapp", {}, wrappers_settings)

observation = env.reset()
show_wrap_obs(observation, env.n_actions_stack, env.char_names)

while True:

    actions = env.action_space.sample()

    observation, reward, done, info = env.step(actions)
    show_wrap_obs(observation, env.n_actions_stack, env.char_names)
    print("Reward: {}".format(reward))
    print("Done: {}".format(done))
    print("Info: {}".format(info))

    if done:
        observation = env.reset()
        show_wrap_obs(observation, env.n_actions_stack, env.char_names)
        break

env.close()