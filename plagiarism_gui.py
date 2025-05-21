import difflib
import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
import os

def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        messagebox.showerror("File Error", str(e))
        return None

def compare_files():
    file1_path = filedialog.askopenfilename(title="Select First File")
    if not file1_path:
        return
    file2_path = filedialog.askopenfilename(title="Select Second File")
    if not file2_path:
        return

    text1 = read_file(file1_path)
    text2 = read_file(file2_path)

    if text1 is None or text2 is None:
        return

    # Calculate similarity
    matcher = difflib.SequenceMatcher(None, text1, text2)
    similarity = round(matcher.ratio() * 100, 2)

    # Verdict logic
    if similarity >= 90:
        verdict = "🚨 Highly Likely Plagiarized"
    elif similarity >= 70:
        verdict = "⚠️ Possibly Plagiarized"
    elif similarity >= 50:
        verdict = "🧐 Needs Review"
    else:
        verdict = "✅ Original Content"

    # Show result in popup
    messagebox.showinfo("Plagiarism Result", f"Similarity: {similarity}%\nVerdict: {verdict}")

    # Generate HTML diff
    diff = difflib.HtmlDiff().make_file(
        text1.splitlines(), text2.splitlines(),
        fromdesc=os.path.basename(file1_path),
        todesc=os.path.basename(file2_path)
    )

    # Save and open HTML diff
    with open("diff_report.html", "w", encoding='utf-8') as f:
        f.write(diff)

    webbrowser.open("diff_report.html")

# GUI Setup
root = tk.Tk()
root.title("Plagiarism Detector")
root.geometry("400x200")

label = tk.Label(root, text="Plagiarism Detector", font=("Arial", 16))
label.pack(pady=20)

btn = tk.Button(root, text="Select Files and Compare", command=compare_files, font=("Arial", 12))
btn.pack(pady=10)

root.mainloop()
