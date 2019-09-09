import math 
import cellular_automaton as ca
import pygame
import random

ALIVE = [1.0]
DEAD = [0]

dim = int(input())
initial_set = [(dim//2,dim//2)]
neighborhood = ca.VonNeumannNeighborhood(ca.EdgeRule.IGNORE_EDGE_CELLS)

class SimpleProcess(ca.Rule):
    def init_state(self,cell_coordinate):
        init = 1.0 if cell_coordinate in initial_set else 0.0
        return [init]

    def evolve_cell(self,last_cell_state,neighbors_last_states):
        alive_neighbors = self.__count_alive_neighbors(neighbors_last_states)
        if last_cell_state==ALIVE:
            new_cell_state = ALIVE
        elif alive_neighbors == 1:
            new_cell_state = ALIVE 
        else:
            new_cell_state = DEAD
        return new_cell_state
    
    @staticmethod
    def __count_alive_neighbors(neighbors):
        an = 0
        for n in neighbors:
            if n == ALIVE:
                an += 1
        return an

    def get_state_draw_color(self, current_state):
        return [255 if current_state[0] else 0, 0, 0]

process = ca.CAFactory.make_multi_process_cellular_automaton(
    dimension=[dim,dim],
    neighborhood=neighborhood,
    rule=SimpleProcess,
    processes=1)

ca_window = ca.CAWindow(cellular_automaton=process, evolution_steps_per_draw=1)