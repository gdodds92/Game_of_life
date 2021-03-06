'''
Created on 28.10.2013

@author: Michael and Geoff

This module contains the logic and functionality for the Game of Life.
It works as the complete engine for the game.
'''

from game_of_life.data_structures import grid
from game_of_life.engine import calculator


class GameOfLife(object):
    '''
    This class represents the Game of Life with a defined, persistent
    rule set.
    '''

    def __init__(self, rule_set, initial_input):
        '''
        Ctor - Initialises the Game of Life with a rule set and an initial
        pattern, both defined by the user. Also initialises a calculator.
        '''
        # Initialise the rule set
        self._rule_set = rule_set

        # Initialise the grid objects to be used by the engine
        self._current_generation = initial_input

        # Give the game engine a calculator to use.
        self._calculator = calculator.Calculator(rule_set)

    def _set_current_generation(self, new_cur_gen):
        '''
        Stores the current generation of cells for use later on.
        '''
        self._current_generation = new_cur_gen

    def get_current_generation(self):
        '''
        Returns the current generation of cells from storage.
        '''
        return self._current_generation

    def _set_next_generation(self, new_nex_gen):
        '''
        Stores the next generation of cells calculated by the
        calculator for use later on.
        '''
        self._next_generation = new_nex_gen

    def get_next_generation(self):
        '''
        Returns the next generation of cells from storage for
        further use.
        '''
        return self._next_generation

    def _calculate_next_generation(self, cur_gen):
        '''
        Calculates the next generations of cells depending on the
        collection of cells given to it.
        '''
        new_generation = self._calculator.calculate_generation(cur_gen)
        gr = grid.Grid(cell_pattern=new_generation)
        return gr

    def next_turn(self):
        '''
        Runs the next turn in the Game of life.
        '''
        # Takes the current generation and passes to calculator
        cur_gen = self.get_current_generation()
        nex_gen_cells = self._calculate_next_generation(cur_gen)

        # Stores next generation in self._next_generation
        self._set_next_generation(nex_gen_cells)

        # Passes current generation back to Game Control to be shown on
        # the GUI.
        pass

        # The state in of the next generation is stored as the current
        # generation
        self._current_generation = self.get_next_generation()
