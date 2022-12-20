// 20. Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/
//

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = Vec::new();

        let mut prev_char: char = '\0';

        for c in s.chars() {
            prev_char = stack.pop().or(Some('\0')).unwrap();

            // we don't have to add if any of these conditions matches

            if (prev_char == '(' && c == ')')
                || (prev_char == '{' && c == '}')
                || (prev_char == '[' && c == ']')
            {
            } else {
                if prev_char != '\0' {
                    stack.push(prev_char);
                }
                stack.push(c);
            }
        }

        stack.len() == 0
    }
}
