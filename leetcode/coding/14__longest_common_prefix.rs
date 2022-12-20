// 14. Longest Common Prefix
// https://leetcode.com/problems/longest-common-prefix/
//

impl Solution {
    fn naive(strs: Vec<String>) -> String {
        let strs_length = strs.len();

        let mut result = String::new();
        let mut prev_char = "";
        let mut counter = 0;

        for idx in (0..strs_length + 2) {
            for (sidx, s) in strs.iter().enumerate() {
                let c_option = s.get(idx..idx + 1);

                // Break computation once the smallest string is processed
                if c_option.is_none() {
                    break;
                }

                let c = c_option.unwrap();

                // set prev_char for first string in strs
                if sidx == 0 {
                    prev_char = c;

                    if prev_char != c {
                        prev_char = "";
                        break;
                    }
                    counter += 1;
                }

                if counter == strs_length {
                    result.push_str(prev_char);
                } else {
                    // we don't have to check further
                    // found char which is not matching across strings
                    // return whatever we have in previous iteration
                    break;
                }

                // Reset counter
                counter = 0;
            }

            result
        }

        pub fn longest_common_prefix(strs: Vec<String>) -> String {
            // 1. strs can only have lowercase english letters
            // 2. each string cannot be greater than 200
            Solution::naive(strs)
        }
    }
}
