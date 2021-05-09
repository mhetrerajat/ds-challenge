// 7. Reverse Integer
// https://leetcode.com/problems/reverse-integer/

impl Solution {
    pub fn reverse(x: i32) -> i32 {
                
        let radix = 10;
        let mut reversed : i32 = 0;
        let mut n : i32 = x;
        let mut pop: i32 = 0;

        while n != 0 {
            // Pop
            pop = n % radix;
            n /= radix;
            
            // check for overflow in case of max
            if reversed > (std::i32::MAX / 10) || (reversed == std::i32::MAX / 10 && pop > 7){
                return 0;
            }
            
            // check for overflow in case of min
            if reversed < (std::i32::MIN / 10) || (reversed == std::i32::MIN / 10 && pop < -8) {
                return 0;
            }
            
             // Push
            reversed = reversed * radix + pop;
        }

        reversed
    }
}
