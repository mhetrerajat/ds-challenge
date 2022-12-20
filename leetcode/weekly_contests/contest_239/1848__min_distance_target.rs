// 1848. Minimum Distance to the Target Element My SubmissionsBack to Contest
// https://leetcode.com/contest/weekly-contest-239/problems/minimum-distance-to-the-target-element/
//

impl Solution {
    pub fn get_min_distance(nums: Vec<i32>, target: i32, start: i32) -> i32 {
        let mut min_idx: i32 = std::i32::MAX;

        for (i, n) in nums.iter().enumerate() {
            if n == &target {
                min_idx = std::cmp::min(min_idx, (i as i32 - start).abs());
            }
        }

        min_idx
    }
}
