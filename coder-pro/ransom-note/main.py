# Time complexity is O(n)+O(m), whete n is the size of the magazine and m is the size of the word
# Space is dependent on the letters that the magazine has, but it has an upper boundary of 26 (the size of english alphabet), so ultimately it'd be O(1)
class Solution(object):
  def canSpell(self, magazine, word):
    result = True
    mag_dict = {}

    for letter in magazine:
        mag_dict[letter] = mag_dict.get(letter, 0) + 1

    for l in word:
        if not l in mag_dict:
            result=False
            break
        else:
            mag_dict[l] -= 1
            # print(l,mag_dict[l])
            if mag_dict[l]==0:
                del mag_dict[l]

    return result


magazine = ['A', 'B', 'C', 'D', 'E', 'F']
wordOne = "BED"
wordTwo = "CAT"
wordThree = "BBE"

print(Solution().canSpell(magazine, wordOne))
print(Solution().canSpell(magazine, wordTwo))
print(Solution().canSpell(magazine, wordThree))