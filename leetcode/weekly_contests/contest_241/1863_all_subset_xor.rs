// 1863. Sum of All Subset XOR Totals
// https://leetcode.com/contest/weekly-contest-241/problems/sum-of-all-subset-xor-totals/
//
//

impl Solution {
    pub fn subset_xor_sum(nums: Vec<i32>) -> i32 {
        let mut total: i32 = 0;

        for n in nums.iter() {
            total |= n;
        }

        total * 2i32.pow(nums.len() as u32 - 1)
    }
}
