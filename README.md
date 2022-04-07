# portfolio-project-one
Portfolio project as a byproduct of my CS 161/162 computer science studies at Oregon State University.
This project file, HasamiShogiGame.py, contains a class named HasamiShogiGame that includes the attributes and methods necessary to play
the abstract boardgame hasami shogi, specifically for "Variant 1" on [the Wikipedia page](https://en.wikipedia.org/wiki/Hasami_shogi).

Here's an example of how the class could be used:
```
game = HasamiShogiGame()
moveResult = game.make_move('e5', 'f9')
print(game.get_active_player())
print(game.get_square_occupant('i9'))
print(game.get_game_state())
