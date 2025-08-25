Input: "Hello world! Hello again."
Output: "hello"

Input: "Python is great. Python is dynamic. Python is powerful!"
Output: "python"

Input: "Data, data, data! I cannot make bricks without clay."
Output: "data"

import string
from collections import Counter

def most_frequent_word(text: str) -> str:
    """
    Processes a paragraph and returns the most frequently used word.

    Steps:
    - Converts text to lowercase
    - Removes punctuation
    - Counts word frequency

    Examples:
    - Input: "Hello world! Hello again." → Output: "hello"
    - Input: "Python is great. Python is dynamic. Python is powerful!" → Output: "python"
    - Input: "Data, data, data! I cannot make bricks without clay." → Output: "data"
    """
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Split into words
    words = text.split()

    # Count frequency
    freq = Counter(words)

    # Return the most common word
    return freq.most_common(1)[0][0]

paragraph = "AI is amazing. AI is evolving. AI is everywhere!"
print(most_frequent_word(paragraph))  # Output: "ai"