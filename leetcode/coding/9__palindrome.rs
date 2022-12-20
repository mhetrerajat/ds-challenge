// 9. Palindrome Number
// https://leetcode.com/problems/palindrome-number/

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        
        // Checks
        // 1. make sure x and rev both in i32 range
        // 2. negative numbers are not really a palindrome here, so consider absolute values
        // 3. Since numbers cannot be negative we don't need to worry about i32 range below zero
        
        let radix: i32 = 10;
        let mut rev: i32 = 0;
        let mut n: i32 = x.abs();
        let mut pop: i32 = 0;
        
        while n != 0 {
            pop = n % radix;
            n /= radix;
            
            if rev > (std::i32::MAX / radix)  || (rev == std::i32::MAX / radix && pop > 7){
                return false;
            }
            
            rev = rev * radix + pop;
        }
        
        x == rev
    }
}
