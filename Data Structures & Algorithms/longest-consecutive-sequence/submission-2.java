class Solution {
    public static int longestConsecutive(int[] nums) {

        // sort array
        ArrayList<Integer> sorted = new ArrayList<>();
        for (int i : nums) {
            sorted.add(i);
        }

        if (sorted.size() == 0) {
            return 0;
        }

        Collections.sort(sorted);
        System.out.println(sorted);

        // check for longest consecutive sequence
        int longest = 1;
        int curr_no = sorted.get(0);
        int curr_seq = 1;

        for (int i = 1; i < sorted.size(); i++) {
            if (sorted.get(i) == curr_no + 1) {
                curr_seq++;
                longest = Math.max(longest, curr_seq);

            } else if (sorted.get(i) != curr_no) {
                longest = Math.max(longest, curr_seq);
                curr_seq = 1;
            }

            curr_no = sorted.get(i);
        }
        
        return longest;
    }

    public static void main(String[] args) {
        int[] nums = {0,1,1,2};

        System.out.println(longestConsecutive(nums));
    }
}