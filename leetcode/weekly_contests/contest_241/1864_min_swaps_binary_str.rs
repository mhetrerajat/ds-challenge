// 1864. Minimum Number of Swaps to Make the Binary String Alternating
// https://leetcode.com/contest/weekly-contest-241/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/
//

use std::cmp::Ordering;

impl Solution {
    fn swap_counter(s: &String, result_first_char: char) -> u32 {
        let mut counter: u32 = 0;
        let mut marker: u8 = result_first_char as u8;

        for c in s.chars() {
            if c != marker as char {
                counter += 1;
            }

            marker ^= 1;
        }

        counter / 2
    }

    pub fn min_swaps(s: String) -> i32 {
        // 1. s can be already alternated
        // 2. each element of s can have either 0 or 1
        // 3. its possible that string cannot be alternated , return -1
        // 4. can have un-even number of 1s and 0s in s

        // count number of chars
        let mut ones: u32 = 0;
        let mut zeros: u32 = 0;

        for c in s.chars() {
            if c == '1' {
                ones += 1;
            } else {
                zeros += 1;
            }
        }

        // impossible to do swaps and find alternating string
        // if diff between ones and zero is more than 1
        if ((ones - zeros) as i32).abs() > 1 {
            return -1i32;
        }

        let result: u32 = match ones.cmp(&zeros) {
            Ordering::Less => Solution::swap_counter(&s, '0'),
            Ordering::Greater => Solution::swap_counter(&s, '1'),
            Ordering::Equal => std::cmp::min(
                Solution::swap_counter(&s, '1'),
                Solution::swap_counter(&s, '0'),
            ),
        };
        result as i32
    }
}
