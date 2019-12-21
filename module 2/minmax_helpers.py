#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def _get_blank_spaces(self):
    return[(x , y) for y in range(ylim) for x in range(xlim) if self._board[x][y] == 0]
    
def terminal_test(gameState):
    return not bool(gameState.get_legal_moves())
def min_value(gameState):
    if terminal_test(gameState):
        return 1
    v = float("inf")
    for m in gameState.get_legal_moves():
        v = min(v , max_value(gameState.forecast_move(m)))
    return v
def max_value(gameState):
    if terminal_test(gameState):
        return -1
    v = float("-inf")
    for m in gameState.get_legal_moves():
        v = max(v , min_value(gameState.forecast_move(m)))
    return v

