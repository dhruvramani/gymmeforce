import numpy as np

from gymmeforce.agents import VanillaPGAgent
from gymmeforce.common.utils import discounted_sum_rewards


class ActorCriticAgent(VanillaPGAgent):
    def __init__(self, env_name, **kwargs):
        super().__init__(env_name, use_baseline=True, **kwargs)

    def _add_advantages_and_vtarget(self, trajectory):
        trajectory['baseline'] = self.model.compute_baseline(self.sess,
                                                             trajectory['states'])
        td_target = trajectory['rewards'] + self.gamma * np.append(
            trajectory['baseline'][1:], 0)
        if self.use_gae:
            td_residual = td_target - trajectory['baseline']
            gae = discounted_sum_rewards(td_residual, self.gamma * self.gae_lambda)
            trajectory['advantages'] = gae
            trajectory['baseline_target'] = gae + trajectory['baseline']
        else:
            trajectory['advantages'] = trajectory['returns'] - trajectory['baseline']
            trajectory['baseline_target'] = td_target

    def train(self, learning_rate, use_gae=True, gae_lambda=0.95, **kwargs):
        self.use_gae = use_gae
        self.gae_lambda = gae_lambda
        super().train(learning_rate, **kwargs)
