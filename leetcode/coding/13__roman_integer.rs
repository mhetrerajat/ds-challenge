// 13. Roman to Integer
// https://leetcode.com/problems/roman-to-integer/

use std::collections::HashMap;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        
        let mut roman_map: HashMap<char, i32> = HashMap::new();
        roman_map.insert('I', 1);
        roman_map.insert('V', 5);
        roman_map.insert('X', 10);
        roman_map.insert('L', 50);
        roman_map.insert('C', 100);
        roman_map.insert('D', 500);
        roman_map.insert('M', 1000);
        
        let mut prev_char: char = '\0';
        let mut num: i32 = 0;
        
        for x in s.chars(){

            if (prev_char == 'I' && (x == 'V' || x == 'X')) || (prev_char == 'X' && (x == 'L' || x == 'C')) || (prev_char == 'C' && (x == 'D' || x == 'M')) {
                num -= 2 * roman_map.get(&prev_char).expect("invalid roman char");
            }
            num += roman_map.get(&x).expect("invalid roman char");
            prev_char = x;
        }
        
        num
    }
}
