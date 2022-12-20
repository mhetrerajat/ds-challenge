// 1. Two Sum
// https://leetcode.com/problems/two-sum/

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        
        let mut map = std::collections::HashMap::new();
        
        for (idx, &num) in nums.iter().enumerate() {
                        
            // Return the indexes if element already exists
            if map.contains_key(&num){
                let another_idx: &i32 = map.get(&num).unwrap();
                return vec![*another_idx, idx as i32];
            }
            
            map.entry((target-num) as i32).or_insert(idx as i32);
        }
        
        return vec![];
    }
}
