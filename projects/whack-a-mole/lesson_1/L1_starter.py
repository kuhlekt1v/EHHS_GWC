################################
#                              #
#        -Whack-A-Mole-        #
#        Starter Code L1       #
#                              #
################################

# -*- coding: utf-8 -*-
import os
import sys

# Whack-a-mole game board.
board = (" ╔═══╦═══════╗ ╔═══╦═══════╗ ╔═══╦═══════╗\n" +
         " ║ 7 ║       ║ ║ 8 ║       ║ ║ 9 ║       ║\n" +
         " ╚═══╣       ║ ╚═══╣       ║ ╚═══╣       ║\n" +
         "     ║       ║     ║       ║     ║       ║\n" +
         "     ║       ║     ║       ║     ║       ║\n" +
         "     ╚═══════╝     ╚═══════╝     ╚═══════╝\n" +
         " ╔═══╦═══════╗ ╔═══╦═══════╗ ╔═══╦═══════╗\n" +
         " ║ 4 ║       ║ ║ 5 ║       ║ ║ 6 ║       ║\n" +
         " ╚═══╣       ║ ╚═══╣       ║ ╚═══╣       ║\n" +
         "     ║       ║     ║       ║     ║       ║\n" +
         "     ║       ║     ║       ║     ║       ║\n" +
         "     ╚═══════╝     ╚═══════╝     ╚═══════╝\n" +
         " ╔═══╦═══════╗ ╔═══╦═══════╗ ╔═══╦═══════╗\n" +
         " ║ 1 ║       ║ ║ 2 ║       ║ ║ 3 ║       ║\n" +
         " ╚═══╣       ║ ╚═══╣       ║ ╚═══╣       ║\n" +
         "     ║       ║     ║       ║     ║       ║\n" +
         "     ║       ║     ║       ║     ║       ║\n" +
         "     ╚═══════╝     ╚═══════╝     ╚═══════╝")

# Mole to displayed randomly in a hole.
mole = " ╔══─┐ \n" + " │o-o│ \n" + "┌└───┘┐\n" + "││ J ││\n"

# Empty holes.
empty = "       " + "       " + "       " + "       "

while True:
  # Initial game instructions following outlined in the assignment
  # should be contained within this while loop.