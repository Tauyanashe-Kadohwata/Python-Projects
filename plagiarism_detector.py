import difflib
from difflib import SequenceMatcher
import sys
import os

def read_file(filepath):
    """Reads content from a file and handles file not found errors."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"❌ Error: File '{filepath}' not found.")
        sys.exit(1)

def analyze_similarity(text1, text2):
    """Returns similarity ratio and matching blocks."""
    matcher = SequenceMatcher(None, text1, text2)
    similarity = round(matcher.ratio() * 100, 2)
    matching_blocks = matcher.get_matching_blocks()
    return similarity, matching_blocks

def give_verdict(similarity):
    """Returns a verdict based on similarity percentage."""
    if similarity >= 90:
        return "🚨 Highly Likely Plagiarized"
    elif similarity >= 70:
        return "⚠️  Possibly Plagiarized"
    elif similarity >= 50:
        return "🧐 Needs Review"
    else:
        return "✅ Original Content"

def show_differences(text1, text2):
    """Prints line-by-line difference summary."""
    diff = difflib.unified_diff(
        text1.splitlines(),
        text2.splitlines(),
        fromfile='demo1.txt',
        tofile='demo2.txt',
        lineterm=''
    )
    print("\n--- Differences Preview ---")
    for line in diff:
        print(line)

def main(file1, file2):
    text1 = read_file(file1)
    text2 = read_file(file2)

    similarity, blocks = analyze_similarity(text1, text2)
    verdict = give_verdict(similarity)

    print(f"\n🔎 Similarity: {similarity}%")
    print(f"📝 Verdict: {verdict}")

    if similarity < 100:
        show_differences(text1, text2)
        
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python plagiarism_detector.py <file1> <file2>")
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        main(file1, file2)
 