# Memory Match Game

This is a simple Memory Match Game built using Python's **Streamlit** framework. It allows users to play a card-matching game with options for one or two players. The game features a shuffled deck of cards where players take turns flipping two cards, attempting to match pairs. A match increases the score, and in the two-player mode, players alternate turns.

## Features

- **One Player Mode**: Play solo and try to match all pairs of cards.
- **Two Players Mode**: Two players take turns matching pairs, with scores tracked for each player.
- **Customizable Cards**: Card images are loaded from the provided folder.
- **Responsive Design**: The game adjusts to fit within the available browser window size.
- **Interactive Gameplay**: Cards can be flipped by clicking on buttons, and matches are dynamically tracked.

## Prerequisites

To run this project, you need to have the following installed:

- **Python 3.7 or higher**
- **Streamlit**:  
  ```bash
  pip install streamlit
  ```
- **Pillow (PIL)**:  
  ```bash
  pip install Pillow
  ```

## How to Run

1. Clone this repository or download the project files:
   
   ```bash
   git clone https://github.com/yourusername/memory-match-game.git
   cd memory-match-game
   ```

2. Install the required dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```

   (Ensure that the `requirements.txt` file includes `streamlit` and `Pillow`.)

3. Place your card images in the `card_images` folder. The game currently supports `.png` images of playing cards, but this can be customized.

4. Run the game using Streamlit:

   ```bash
   streamlit run main.py
   ```

5. Open the link provided by Streamlit in your web browser to start playing.

## Game Instructions

- **One Player Mode**: Click on "One Player" to start a solo game. The objective is to match all pairs of cards in the deck.
- **Two Players Mode**: Click on "Two Players" to start a multiplayer game. Players take turns flipping two cards, and the player with the most matched pairs at the end wins.
- The game ends when all card pairs are matched.

## Customization

- **Card Images**: You can customize the card images by replacing or adding files to the `card_images` folder. The filenames should follow the same structure used in the `card_filenames` list.
- **Grid Size**: The board layout currently uses 15 columns, but you can adjust this in the `display_board` function if needed.

## How it Works

1. **Deck Initialization**: A shuffled deck of cards is created, consisting of pairs of each card.
2. **Flipping Cards**: When a card is clicked, it's revealed. If two cards are flipped, the game checks if they match.
3. **Score Tracking**: The game keeps track of matched cards and scores in both one and two-player modes.
4. **Turn Switching**: In two-player mode, turns alternate after every card flip.
