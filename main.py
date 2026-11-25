import os

LINE = "I didn't drop at the climax, I walked out — he was about to get the girl, and I've carried this house since 2019 without one thank-you."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
