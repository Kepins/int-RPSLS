# Rock Paper Scissors (Lizard Spock)

## Rock Paper Scissors

Rock, Paper, Scissors is a hand game usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. These shapes are "rock", "paper" and "scissors". It's a [zero-sum game](https://en.wikipedia.org/wiki/Zero-sum_game) - that means that in case there is no tie, there are only two possible outcomes: one of the two players wins and the other player loses.



| <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Rock-paper-scissors.svg/460px-Rock-paper-scissors.svg.png" alt="RPS" style="width: 500px;"/> |
|:--:|
| Scissors cuts Paper |
| Paper covers Rock |
| Rock crushes Scissors |

## Rock Paper Scissors Lizard Spock

Rock, Paper, Scissors, Lizard, Spock is an expansion to RPS. The picture below depicts its rules.

| <img src="https://data2.cupsell.pl/upload/generator/10029/640x420/35503_print-trimmed-1.png" alt="RPSLS" style="width: 500px;"/> |
|:--:| 
| Scissors cuts Paper |
| Paper covers Rock |
| Rock crushes Lizard |
| Lizard poisons Spock |
| Spock smashes Scissors |
| Scissors decapitates Lizard |
| Lizard eats Paper |
| Paper disproves Spock |
| Spock vaporizes Rock |
| (and as it always has) Rock crushes Scissors |


## Task

### Flow
Your task is to implement both variants of the game with the following flow:
1. user chooses if he wants the extended version,
2. user chooses figure he wants to use,
3. computer chooses random figure,
4. user gets the result of the combat between those figures,
5. user chooses whether he wants to play again: if so, go back to `1.`, else end program.

### Requirements:
- the code should be written in Python 3.5+
- whole game should be designed according to OOP paradigm,
- enums are widely appreciated,
- functions should be covered with unit tests (preferably with `pytest` framework),
- whole program ought to be consistent with PEP8 (adding `pylint` would be great for this purpose).

## How to run


1. Create virtual environment from requirements.txt: python3 -m venv .venv
2. Activate virtual environment: source .venv/bin/activate
3. Run main.py: python main.py
