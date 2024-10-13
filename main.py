import random
import streamlit as st

# Word hints for the game
WORD_HINTS = {
    "سياحة": "استكشاف أماكن جديدة.",
    "سباحة": "الحركة في الماء.",
    "تقاعس": "تأخر أو تهاون عن العمل.",
    "طائرة": "وسيلة نقل.",
    "كهولة": "ما بين الفتوة والشيخوخة.",
    "جهوري": "عالي النبرة قوي ومرتفع."
}

class Game:
    def __init__(self):
        self.attempts = 0  # Track attempts for the current word

    def reset_attempts(self):
        self.attempts = 0  # Reset attempts for the new word

# Function to select a random word
def get_random_word(used_words):
    available_words = list(WORD_HINTS.keys())
    unused_words = [word for word in available_words if word not in used_words]
    if unused_words:
        return random.choice(unused_words)
    return None

# Function to check the guess and provide feedback
def check_guess(guess, answer):
    feedback = ["⬜"] * len(guess)
    answer_list = list(answer)

    # Check for correct letters in the correct place (🟩)
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            feedback[i] = "🟩"
            answer_list[i] = None

    # Check for correct letters in the wrong place (🟨)
    for i in range(len(guess)):
        if feedback[i] == "⬜" and guess[i] in answer_list:
            feedback[i] = "🟨"
            answer_list[answer_list.index(guess[i])] = None

    return feedback

# Initialize game
if 'game' not in st.session_state:
    st.session_state['game'] = Game()
if 'answer' not in st.session_state:
    st.session_state['answer'] = get_random_word([])  # Start with a random word
if 'used_words' not in st.session_state:
    st.session_state['used_words'] = []

# Randomly choose a word for the game
if st.session_state['answer'] is None:
    st.session_state['answer'] = get_random_word(st.session_state['used_words'])
    if st.session_state['answer']:
        st.session_state['used_words'].append(st.session_state['answer'])
    st.session_state['game'].reset_attempts()  # Reset attempts for the new word

# Reset the game
if st.button('إعادة'):
    st.session_state['answer'] = get_random_word(st.session_state['used_words'])
    if st.session_state['answer']:
        st.session_state['used_words'].append(st.session_state['answer'])
    st.session_state['game'].reset_attempts()  # Reset attempts for the new word
    st.session_state['guesses'] = []  # Clear guesses

# Display game title
st.title("خمن الكلمة")

# Initialize guesses
if 'guesses' not in st.session_state:
    st.session_state['guesses'] = []

# Function to change square color based on feedback
def get_square_style(feedback):
    if feedback == "🟩":
        return "background-color: green; color: white;"
    elif feedback == "🟨":
        return "background-color: #f09102; color: white;"
    else:
        return "background-color: gray; color: white;"

# Button for hint
if st.button('💡'):
    if st.session_state.get('answer'):
        hint = WORD_HINTS[st.session_state['answer']]
        st.info(f"تلميح: {hint}")

# Input box for guesses
with st.form(key="wordle_form"):
    guess = st.text_input("ادخل كلمة من 5 حروف:", help="", max_chars=5)
    submit_guess = st.form_submit_button(label="خمن الكلمة")

# Lambda to check if the guess is all letters
is_all_letters = lambda x: x.isalpha() and len(x) == 5

# Check guess if the player submits a word
if submit_guess:
    if is_all_letters(guess):
        if st.session_state['game'].attempts < 5:  # Check if attempts are less than 5
            feedback = check_guess(guess, st.session_state['answer'])
            st.session_state['guesses'].append((guess, feedback))
            st.session_state['game'].attempts += 1  # Increment attempts

            # Check if the user has won
            if guess == st.session_state['answer']:
                st.success("مبروك! خمنت الكلمة الصحيحة")

                # Move to the next word
                st.session_state['answer'] = get_random_word(st.session_state['used_words'])
                if st.session_state['answer']:
                    st.session_state['used_words'].append(st.session_state['answer'])
                st.session_state['game'].reset_attempts()  # Reset attempts for the new word
                st.session_state['guesses'] = []  # Clear guesses for the new word

            elif st.session_state['game'].attempts >= 5:
                st.error(f"يا خسارة! الكلمة الصحيحة كانت: {st.session_state['answer']}")
                # Move to the next word
                st.session_state['answer'] = get_random_word(st.session_state['used_words'])
                if st.session_state['answer']:
                    st.session_state['used_words'].append(st.session_state['answer'])
                st.session_state['game'].reset_attempts()  # Reset attempts for the new word
                st.session_state['guesses'] = []  # Clear guesses for the new word
        else:
            st.warning("لقد استنفدت جميع المحاولات! انتقل إلى الكلمة التالية.")

    else:
        st.error("خطأ, ادخل كلمة مكونة من 5 حروف فقط!")

# Display guesses and feedback using squares
if st.session_state['guesses']:
    for guess, feedback in st.session_state['guesses']:
        cols = st.columns(5)
        for i, letter in enumerate(guess):
            cols[i].markdown(
                f"<div dir='rtl' style='text-align: center; padding: 10px; font-size: 20px; border: 1px solid black; {get_square_style(feedback[i])}'>{guess[i]}</div>",
                unsafe_allow_html=True
            )

# Apply RTL styling
st.markdown("""
<style>
body {
    direction: rtl;
    text-align: right;
}
</style>
""", unsafe_allow_html=True)
