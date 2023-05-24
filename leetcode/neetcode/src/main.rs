mod arrays_n_hashmap {

    use std::collections::HashSet;

    // https://leetcode.com/problems/contains-duplicate/description/
    // Problem 217
    pub fn contains_dups(nums: Vec<usize>) -> bool {
        let mut hset = HashSet::new();
        for n in nums {
            if hset.contains(&n) {
                return true;
            } else {
                hset.insert(n);
            }
        }
        false
    }

    #[test]
    fn test_contains_dups() {
        struct TestCase {
            nums: Vec<usize>,
            expected: bool,
        }

        let testcases = [
            TestCase {
                nums: [1, 2, 3, 4, 5, 1].to_vec(),
                expected: true,
            },
            TestCase {
                nums: [1, 2, 3, 4].to_vec(),
                expected: false,
            },
            TestCase {
                nums: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2].to_vec(),
                expected: true,
            },
        ];

        for tc in testcases {
            assert_eq!(contains_dups(tc.nums), tc.expected);
        }
    }
}

fn main() {
    let nums = [1, 2, 3, 4, 1].to_vec();
    assert!(arrays_n_hashmap::contains_dups(nums));
}
