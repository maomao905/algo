def isMatch(text, pattern):
  return isMatchHelper(text, pattern, 0, 0)

# textIndex - the Index the text is checked from
# patIndex - the index the pattern is checked from
def isMatchHelper(text, pattern, textIndex, patIndex):
  # base cased - one of the indexes reached the end of text or pattern
  print('------')
  if textIndex >= len(text):
    if patIndex >= len(pattern):
      return True
    else:
      # the only possibility that the text matches is if the character before the * is matched exactly 0 times
      # '*aaa'
      # pattern index forwarded by two after the * symbol
      if (patIndex+1 < len(pattern)) and (pattern[patIndex+1] == '*'):
        return isMatchHelper(text, pattern, textIndex, patIndex + 2)
      else:
        return False
  # pattern is at the end and text is not at the end
  elif (patIndex >= len(pattern)) and (textIndex < len(text)):
    return False
  # pattern is not at the end and next pattern is *
  elif (patIndex+1 < len(pattern)) and (pattern[patIndex+1] == '*'):    
    if (pattern[patIndex] == '.') or (text[textIndex] == pattern[patIndex]):
      # move to next characteri
      return (isMatchHelper(text, pattern, textIndex, patIndex + 2) or 
             isMatchHelper(text, pattern, textIndex + 1, patIndex))
    else:
       return isMatchHelper(text, pattern, textIndex, patIndex + 2)
  elif (pattern[patIndex] == '.') or (pattern[patIndex] == text[textIndex]):
      return isMatchHelper(text, pattern, textIndex + 1, patIndex + 1)
  else:
      return False
    
# isMatch('bbbbbbbb', '.*.*.*.*a')
isMatch('b', '.*.*.*.*')
# print(cnt)
# 2^4 * len(bbb)
