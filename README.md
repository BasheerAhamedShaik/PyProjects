# Snake-Water-Gun Game

This is a Python implementation of the classic Snake-Water-Gun game, similar to Rock-Paper-Scissors. In this game, you can play against the computer, where each choice has a specific win/lose interaction.

## How to Play

1. **Snake (`s`)** beats Water (`w`) but loses to Gun (`g`).
2. **Water (`w`)** beats Gun (`g`) but loses to Snake (`s`).
3. **Gun (`g`)** beats Snake (`s`) but loses to Water (`w`).

### Game Rules:

- **Draw:** If both you and the computer choose the same item.
- **Win:** You win if your choice beats the computer's choice.
- **Lose:** You lose if your choice is beaten by the computer's choice.

## Running the Game

To play the game, simply run the Python script in your terminal:

```bash
python snake_water_gun.py
