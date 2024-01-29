# Blackjack_opp_game

Welcam in Blackjack terminal game which was made in Python using object oriented programming. 
This project consists of several modules that together implement a simple Blackjack game.


1. [ Rules. ](#rules)
2. [ Gameplay. ](#gameplay)
3. [Modules](#modules)
  - [`game.py`](#gamepy)
  - [`deck.py`](#deckpy)
  - [`card.py`](#cardpy)
  - [`user.py`](#userpy)
4. [ Prerequisites and installation. ](#installation)
5. [ Demo. ](#demo)
6. [ Running the tests. ](#running_and_tests)


<a name="rules"></a>
## Rules

- The goal is to connect as many points as possible, but not more than 21.
- The highest hand is Blackjack, which includes 10 and face cards.
- Cards 2 to 10 have values equal to their numbers.
- Jack, Queen, and King are worth 10 points each.
- An Ace has a value of 1 or 11, depending on the game stage.
  
<a name="gameplay"></a>
## Gameplay

1. The player receives two cards.
2. The player can choose to draw a card (next) or not draw cards (pass).
3. If a player has more than 21 points after drawing cards, they lose.
4. If a player has exactly 21 points, they win.
5. If a player has fewer than 21 points, the dealer draws two cards.
6. The dealer aims to beat the player's score.
7. The winner is the one whose sum of points is closer to or equal to 21
 
<a name="installation"></a>

<a name="modules"></a>
## Modules
<a name="gamepy"></a>
### 1. Game
Classes:
Game: Represents the main game logic and flow.
Dependencies:
Deck class from the deck module.
User class from the user module.
Description:
The game.py module contains the main game logic. It orchestrates the flow of the Blackjack game, managing the interaction between the player, the deck of cards, and the computer-controlled croupier.

<a name="deckpy"></a>
### 2. Deck
Classes:
Deck: Manages the creation, shuffling, and distribution of a deck of cards.
External Dependencies:
Card class from the card module.
Description:
The deck.py module handles the functionality related to the deck of cards. It includes methods for creating a deck, shuffling it, and distributing cards to players. It relies on the Card class from the card module to represent individual playing cards.

<a name="cardpy"></a>
### 3. Card
Classes:
Card: Represents a playing card.
Description:
The card.py module defines the Card class, representing individual playing cards in the game. Each card has a value, a string representation for numbers, and a color.

<a name="userpy"></a>
### 4.User
Classes:
User: Represents a participant in a Blackjack game.
Description:
The user.py module defines the User class, representing both the player and the croupier in the game. It keeps track of each participant's cards and score. The User class is used by the Game class to manage player and croupier interactions.

## Prerequisites and installation. 

There is no need for any installation of extra modules.

The main.py file contains the main function to start the Blackjack game. It creates an instance of the Game class and initiates the player's opening move.

```
python main.py
```

## Demo

[Link to Video Demo](https://www.youtube.com/watch?v=i7axmKqd-w0)

<a name="running_and_tests"></a>
## Running the tests

Each module has its test file. 
To run the test install pytest module:

```
pip install pytest
```
Then type:
```
python -m pytest <module_neme.py>
```
