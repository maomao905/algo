"""
time: O(2^N)
space: O(N*2^N)
"""
def find_letter_case_string_permutations(str):
    
  permutations = [str]
  for i in range(len(str)):
    s = str[i]
    if s.isalpha():
        for j in range(len(permutations)):
            char_array = list(permutations[j])
            char_array[i] = char_array[i].swapcase()
            permutations.append(''.join(char_array))
  return permutations

# def find_letter_case_string_permutations(str):
#   permutations = [""]
#   for i in range(len(str)):
#     s = str[i]
#     if s.isnumeric():
#         for j in range(len(permutations)):
#             permutations[j] += s
#     else:
#         for j in range(len(permutations)):
#             permutations.append(permutations[j] + s.upper())
#             permutations[j] += s
# 
#   return permutations


def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()
