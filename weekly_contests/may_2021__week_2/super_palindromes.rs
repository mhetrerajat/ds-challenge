// Super Palindromes
// https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3736/
//

impl Solution {
    fn is_palindrome(number: i64) -> bool {
        let radix: i64 = 10;
        let mut rev: i64 = 0;
        let mut n: i64 = number.abs();
        let mut pop: i64 = 0;

        while n != 0 {
            pop = n % radix;
            n /= radix;

            if rev > (std::i64::MAX / radix) || (rev == std::i64::MAX / radix && pop > 7) {
                return false;
            }

            rev = rev * radix + pop;
        }

        rev == number
    }

    fn is_super_palindrome(number: i64) -> bool {
        if Solution::is_palindrome(number) {
            let sqrt_num = (number as f64).sqrt();
            if sqrt_num.fract() == 0.0 {
                return Solution::is_palindrome(sqrt_num as i64);
            }
        }

        return false;
    }

    pub fn superpalindromes_in_range(left: String, right: String) -> i32 {
        let left: i64 = left.parse().unwrap();
        let right: i64 = right.parse().unwrap();

        let mut counter: i32 = 0;

        for num in (left..right) {
            if Solution::is_super_palindrome(num) {
                counter += 1;
            }
        }

        counter
    }
}
