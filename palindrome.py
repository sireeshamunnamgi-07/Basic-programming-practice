import re
def is_palindrome(text: str) -> bool:
    cleaned = re.sub(r'[^A-Za-z0-9]', '', text).lower()
    return cleaned == cleaned[::-1]
if __name__ == "__main__":
    test_cases = [
        "madam",
        "Racecar",
        "hello",
        "A man, a plan, a canal: Panama",
        "No lemon, no melon"
    ]
for s in test_cases:
        result = is_palindrome(s)
        print(f'"{s}" → {result}')
