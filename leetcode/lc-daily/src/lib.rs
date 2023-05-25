use std::{cmp::Reverse, collections::BinaryHeap};

pub fn add(left: usize, right: usize) -> usize {
    left + right
}

// https://leetcode.com/problems/maximum-subsequence-score/
// May 24, 2023
// 2542. Maximum Subsequence Score
fn max_score(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
    let _n: usize = nums1.len(); // both nums1 and nums2 are of same length

    // sort nums2, nums1 pair in descending order as per nums2
    let mut srtnums = nums2.into_iter().zip(nums1.into_iter()).collect::<Vec<_>>();
    srtnums.sort_unstable_by(|a, b| b.cmp(a));

    // use minheap to keep track of smallest numbers
    let mut sum = 0;
    let mut answer = 0;
    let mut pq = BinaryHeap::new();

    for (n2, n1) in &srtnums {
        pq.push(Reverse(n1));
        sum += n1;

        if pq.len() > k as usize {
            if let Some(Reverse(pitem)) = pq.pop() {
                sum -= pitem;
            }
        }

        if pq.len() == k as usize {
            // get the max answer
            answer = answer.max(sum * n2);
        }
    }
    answer as i64
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }

    #[test]
    fn test_max_score() {
        let result = max_score(vec![1, 3, 3, 2], vec![2, 1, 3, 4], 3);
        assert_eq!(result, 12);
        assert_eq!(max_score(vec![4, 2, 3, 1, 1], vec![7, 5, 10, 9, 6], 1), 30);
    }
}
