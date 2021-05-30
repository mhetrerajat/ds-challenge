use std::cmp::min;
#[derive(Debug)]
pub struct HighScores<'s> {
    scores: &'s [u32],
}

impl<'s> HighScores<'s> {
    pub fn new(scores: &'s [u32]) -> Self {
        // unimplemented!(
        //     "Construct a HighScores struct, given the scores: {:?}",
        //     scores
        // )

        Self { scores }
    }

    pub fn scores(&self) -> &[u32] {
        // unimplemented!("Return all the scores as a slice")
        self.scores
    }

    pub fn latest(&self) -> Option<u32> {
        // unimplemented!("Return the latest (last) score")
        // Some(self.scores[self.scores.len()])
        self.scores.last().cloned()
    }

    pub fn personal_best(&self) -> Option<u32> {
        // unimplemented!("Return the highest score")
        self.scores
            .iter()
            .reduce(|a, b| -> &u32 {
                if a >= b {
                    a
                } else {
                    b
                }
            })
            .cloned()
    }

    pub fn personal_top_three(&self) -> Vec<u32> {
        // unimplemented!("Return 3 highest scores")
        // (vec![]).copy_from_slice(self.scores.clone().sort()[..3])

        // let mut r = vec![];

        // for a in self.scores() {
        //     let mut max_item = *a;
        //     for b in self.scores {
        //         if max_item < *b {
        //             max_item = *b;
        //         }
        //     }
        //     r.push(max_item);

        //     if r.len() == 3 {
        //         break;
        //     }
        // }

        let mut a = self.scores.to_vec();
        a.sort_unstable();
        a.reverse();
        let length = min(a.len(), 3);
        a[..length].to_vec()
    }
}
