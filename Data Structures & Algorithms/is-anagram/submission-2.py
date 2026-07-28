class Solution:
    def frequencyCounter(self, word):
        frequency = {}
        for letter in word:
            frequency[letter] = frequency.get(letter, 0) + 1

        return frequency

    def isAnagram(self, s: str, t: str) -> bool:
        return self.frequencyCounter(s) == self.frequencyCounter(t)
    