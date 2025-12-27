import argparse
from textblob import TextBlob
import sys

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text using TextBlob.
    Returns the polarity and subjectivity.
    """
    blob = TextBlob(text)
    return blob.sentiment

def print_banner():
    print("=" * 40)
    print("   SENTIMENT SCOPE - AI Analyzer")
    print("=" * 40)

def main():
    print_banner()
    
    parser = argparse.ArgumentParser(description="Analyze the sentiment of a text string.")
    parser.add_argument("text", nargs="?", help="The text to analyze. If omitted, you will be prompted.")
    args = parser.parse_args()

    text = args.text
    if not text:
        try:
            text = input("Enter text to analyze: ")
        except KeyboardInterrupt:
            sys.exit(0)

    if not text.strip():
        print("Error: No text provided.")
        return

    sentiment = analyze_sentiment(text)
    
    print("\n--- Analysis Results ---")
    print(f"Input: \"{text}\"\n")
    
    # Polarity: -1.0 (Negative) to 1.0 (Positive)
    polarity = sentiment.polarity
    print(f"Polarity Score: {polarity:.2f}")
    print("  [-1.0 (Negative) ... 0 (Neutral) ... 1.0 (Positive)]")
    
    # Subjectivity: 0.0 (Objective) to 1.0 (Subjective)
    subjectivity = sentiment.subjectivity
    print(f"Subjectivity Score: {subjectivity:.2f}")
    print("  [0.0 (Fact) ... 1.0 (Opinion)]")

    print("\nVERDICT:")
    if polarity > 0.1:
        print("  \u2705 POSITIVE vibe")
    elif polarity < -0.1:
        print("  \u274C NEGATIVE vibe")
    else:
        print("  \u2796 NEUTRAL vibe")
    print("=" * 40)

if __name__ == "__main__":
    main()
