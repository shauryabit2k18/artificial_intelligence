# Game Playing Agent: ISOLATION



The purpose of this project is to design and implement a game playing agent to play a game using adversarial search methods. The goal is to create a game playing agent that defeats our opponent at a game of isolation consistently. For this project I’ve designed three heuristics to create an effective edge for the game playing agent. 

## MinMax:

In the case of the game isolation, there are two players competing against each other. We are under the assumption that the AI player and human player are both playing two win. While back-propagating through the search tree, our algorithm must maximize the outcome (choose the optimal move) for when it’s the AI’s turn and minimize the outcome (choose the least optimal move for us) when it’s the human player’s turn.
