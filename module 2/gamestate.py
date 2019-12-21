#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from copy import deepcopy
# board dimentions constant
xlim , ylim = 2 , 3

class GameState:
    def __init(self):
        self._board = [[0] * ylim for _ in range(xlim)]
        self._board[-1][-1] = 1
        seld._parity = 0
        self.player_locations = [None , None]
    def forecast_move(self , move):
        if move not in self.get_legal_moves():
            raise RuntimeError("attempted forcast of an illeaglemove")
        newBoard = deepcopy(self)
        newBoard._board[move[0]][move[1]] = 1
        newBoard._player_loacations[self._parity] = move
        newBoard._parity ^= 1
        return newBoard
    def get_legal_moves(self):
        loc = self._player_loacations[self._parity]
        if not loc:
            return self._get_blank_spaces()
        moves = []
        rays = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        for dx , dy in rays:
            _x , _y = loc
            while 0 <= _x + dx < xlim and 0 <= _y + dy < ylim:
                _x , _y = _x + dx , _y + dy
                if self._board[_x][_y]:
                    break
                moves.append((_x , _y))
        return moves

