def rm_char(word, c):
    return word.replace(c, "")

print(rm_char("CSx Sevenx", "x"))

def rm_char2(word, c):
  word_without_char = []
  for char in word:
    if char != c.lower() and char != c.upper():
      word_without_char.append(char)
  return "".join(word_without_char)

print(rm_char2("CSx SevXenx", "x"))
