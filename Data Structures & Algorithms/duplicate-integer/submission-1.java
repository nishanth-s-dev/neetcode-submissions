class Solution {

    // O(n) | O(n)
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        
        for (int i : nums) {
            if (set.contains(i)) return true;
            set.add(i);
        }

        return false;
    }
}