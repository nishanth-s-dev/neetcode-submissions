class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        Map<Character, Integer> mapOne = new HashMap<>();
        Map<Character, Integer> mapTwo = new HashMap<>();

        int pointer = 0;
        
        while (pointer < s.length()) {
            char charOne = s.charAt(pointer);
            char charTwo = t.charAt(pointer);

            if (mapOne.containsKey(charOne)) {
                mapOne.put(charOne, mapOne.get(charOne) + 1);
            } else {
                mapOne.put(charOne, 0);
            }

            if (mapTwo.containsKey(charTwo)) {
                mapTwo.put(charTwo, mapTwo.get(charTwo) + 1);
            } else {
                mapTwo.put(charTwo, 0);
            }

            pointer++;
        }

        Set<Character> keysetOne = mapOne.keySet();
        Set<Character> keysetTwo = mapTwo.keySet();

        if (!keysetOne.equals(keysetTwo)) return false;


        for (Map.Entry<Character, Integer> entry : mapOne.entrySet()) {
            Character key = entry.getKey();
            Integer valueOne = entry.getValue();
            Integer valueTwo = mapTwo.get(key);

            if (valueTwo == null || !valueOne.equals(valueTwo)) {
                return false;
            }
        }

        return true;
    }
}
