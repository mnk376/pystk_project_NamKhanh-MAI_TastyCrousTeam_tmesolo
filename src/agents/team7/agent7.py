import numpy as np
import random

from utils.track_utils import compute_curvature, compute_slope
from agents.kart_agent import KartAgent

class Agent7(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.name = "Nam_Khanh-MAI-T7" # replace with your chosen name
        self.steps_count = 0

    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []

    def endOfTrack(self):
        return self.isEnd

    def path_ajust(self, obs, action):
        """
        Ajuste la direction du kart pour suivre le centre de la piste.
        """
        steer = action["steer"]
        center = obs["paths_end"][2]
        if (center[2] > 20 and abs(obs["center_path_distance"]) < 3) : 
            steer = 0
        elif abs(center[0]) > 0.67 : # variable optimise 
            steer += 0.63 * center[0]
        action["steer"] = np.clip(steer, -1, 1)
        return action

    #def recule(self, obs,action):
     #   return action


    def choose_action(self, obs):
        self.steps_count += 1

          
        acceleration = random.random()
        steering = random.random()
        action = {
            "acceleration": acceleration,
            "steer":  steering,
            "brake": False, # bool(random.getrandbits(1)),
            "drift": False, #bool(random.getrandbits(1)),
            "nitro": False, #bool(random.getrandbits(1)),
            "rescue":False, #bool(random.getrandbits(1)),
            "fire": False, #bool(random.getrandbits(1)),
        }



        if self.steps_count >= 200:  #si le pas passe de 200
            action["acceleration"] = -1.0
            action["brake"] = False
            return action

        #action = self.recule(obs, action)
        action = self.path_ajust(obs, action)
        return action


