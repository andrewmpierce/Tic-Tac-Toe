# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:47:13 2015

@author: Drew
"""

#This will be the board class in Tic Tac Toe

class Board(object):
    
    def _init_(self, board):
        self.board = board
    

    def display(self, board):
        board_line1 = "---"
        board_line2 = "---"
        board_line3 = "---"        
        
        print board_line1
        print board_line2 
        print board_line3
        
        
Board.display()
