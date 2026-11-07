# Poker Hands Evaluator

This project evaluates a five-card poker hand built from a combination of cards belonging to the player and the table.

## Objective

The goal is to determine the best possible poker hand from the five cards available:

- 3 cards from the player
- 2 cards from the table

A valid evaluation must consider both the card rank and the card suit independently, since the final hand depends on the combination of values and suits.

## Rules of the game

Each card is composed of:

- a suit: hearts, diamonds, clubs or spades
- a rank: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K or A

The evaluator should:

1. identify the best possible hand among the 5 cards
2. distinguish between player cards and table cards
3. compare the final hand against the standard poker ranking order
4. return the highest-ranking combination found

## Important implementation notes

The first step is to analyze the best possible hand. The evaluation should not look only at the player's own 3 cards; it must also consider the 2 table cards together, because the final hand is always made from the five cards in play.

The logic must therefore:

- separate suit and rank
- count repeated ranks
- detect ordered sequences for straights
- detect flushes by suit
- identify full houses, pairs, trips, quads and straight flushes
- determine the highest-ranking valid combination

## Poker hand ranking

From highest to lowest, the standard hand order is:

1. Royal Flush
2. Straight Flush
3. Four of a Kind
4. Full House
5. Flush
6. Straight
7. Three of a Kind
8. Two Pair
9. One Pair
10. High Card

### Hand descriptions

#### 1. Royal Flush
Five consecutive cards of the same suit, from 10 to Ace.

Example: A♠ K♠ Q♠ J♠ 10♠

#### 2. Straight Flush
Five consecutive cards of the same suit.

Example: 9♥ 8♥ 7♥ 6♥ 5♥

#### 3. Four of a Kind
Four cards with the same rank.

Example: K♣ K♦ K♥ K♠ 3♦

#### 4. Full House
Three cards of one rank and two cards of another rank.

Example: Q♣ Q♦ Q♠ 7♥ 7♣

#### 5. Flush
Five cards of the same suit, not in sequence.

Example: A♠ J♠ 8♠ 5♠ 2♠

#### 6. Straight
Five consecutive ranks not all of the same suit.

Example: 6♦ 5♣ 4♥ 3♠ 2♦

#### 7. Three of a Kind
Three cards with the same rank.

Example: 8♣ 8♦ 8♥ J♠ 2♦

#### 8. Two Pair
Two cards of one rank and two cards of another rank.

Example: 9♣ 9♦ 4♠ 4♥ K♣

#### 9. One Pair
Two cards with the same rank.

Example: A♥ A♣ 10♦ 7♣ 3♠

#### 10. High Card
No pair or better. The highest rank in the hand decides.

Example: A♣ J♦ 9♠ 5♥ 2♣

## Evaluation workflow

A recommended implementation order is:

1. parse each card into rank and suit
2. identify the strongest possible 5-card combination
3. check for flush and straight patterns
4. count repeated ranks to identify pairs, triples and quads
5. determine the best hand among all possible combinations
6. return the final result with the hand category and highest card values

## Example

A hand with:

- player: A♠ 9♣ 7♦
- table: K♠ 10♠

This creates the final hand: A♠ K♠ 10♠ 9♣ 7♦

This is a flush only if all five cards share the same suit, which here they do not. The evaluator should therefore calculate the real strongest possible hand using all five cards together.

## Project purpose

This project is intended to practice:

- data modeling
- conditional logic
- sequence detection
- rank counting
- problem decomposition
- poker rules interpretation

## Summary

The main challenge is to evaluate a five-card poker hand correctly by combining player and table cards, distinguishing suit from rank, and applying the standard poker ranking rules in the proper order.

This project is a good exercise in building a decision-based evaluator that must prioritize the strongest valid hand in a given set of cards.
