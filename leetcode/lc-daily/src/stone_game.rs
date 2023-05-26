pub mod stone_game {
    use std::collections::HashMap;

    pub fn stone_game_1(piles: Vec<i32>) -> bool {
        let mut dp: HashMap<(usize, usize), i32> = HashMap::new();
        let n = piles.len();

        fn dpf(l: usize, r: usize, dp: &mut HashMap<(usize, usize), i32>, piles: &Vec<i32>) -> i32 {
            if l > r {
                return 0;
            }

            if dp.contains_key(&(l, r)) {
                return dp.get(&(l, r)).unwrap().to_owned();
            }

            let is_even = (r - l) % 2 != 0;
            let left: i32 = if is_even {
                piles.get(l).unwrap().to_owned()
            } else {
                0
            };

            let right = if is_even {
                piles.get(r).unwrap().to_owned()
            } else {
                0
            };

            let v = std::cmp::max(
                dpf(l + 1, r, dp, piles) + left,
                dpf(l, r - 1, dp, piles) + right,
            );

            // let v = (dpf(l + 1, r, dp, piles) + left).max(dpf(l, r - 1, dp, piles) + right);
            dp.insert((l, r), v);

            dp.get(&(l, r)).unwrap().to_owned()
        };

        dpf(0, n - 1, &mut dp, &piles) > 0
    }

    #[test]
    fn test_stone_game_1() {
        assert_eq!(stone_game_1(vec![5, 3, 4, 5]), true);
        assert_eq!(stone_game_1(vec![3, 7, 2, 3]), true);
    }
}
