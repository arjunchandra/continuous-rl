"""Define abstractions."""
from typing import Union
from abc import ABC, abstractmethod
import numpy as np
from envs.vecenv import SubprocVecEnv

Arrayable = Union[list, float, np.ndarray]

class Policy(ABC):
    @abstractmethod
    def step(self, obs: Arrayable):
        pass

    @abstractmethod
    def observe(self,
                next_obs: Arrayable,
                reward: Arrayable,
                done: Arrayable):
        pass

    @abstractmethod
    def learn(self):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def eval(self):
        pass

class ParametricFunction(ABC):
    """Wrap around a torch module."""
    @abstractmethod
    def __call__(self, obs: Arrayable):
        pass

    @abstractmethod
    def parameters(self):
        pass

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def eval(self):
        pass

    @abstractmethod
    def to(self, device):
        pass

class Env(ABC):
    @abstractmethod
    def step(self, action: Arrayable):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def render(self, mode='human'):
        pass

    @abstractmethod
    def close(self):
        pass


Env.register(SubprocVecEnv)

class Noise(ABC):
    @abstractmethod
    def step(self):
        pass

    @abstractmethod
    def perturb_output(
            self,
            inputs: Arrayable,
            a_function: ParametricFunction):
        pass
