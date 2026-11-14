"""4. Strings"""

text = "Python is fun"

text[0]          # 'P'
text[-1]         # 'n'
text[0:6]        # 'Python'
text[::2]        # every second character
text[::-1]       # reversed string

len(text)
text.lower()
text.upper()
text.title()
text.strip()
text.replace("fun", "powerful")
text.split()                 # list of words
"-".join(["2026", "11", "14"])
text.startswith("Py")
text.endswith("fun")
