class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequencyOne = {}
        frequencyTwo = {}

        for letter in s:
            frequencyOne[letter] = frequencyOne.get(letter, 0) + 1
        for letter in t:
            frequencyTwo[letter] = frequencyTwo.get(letter, 0) + 1

        return frequencyOne == frequencyTwo