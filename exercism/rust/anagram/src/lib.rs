use std::collections::{HashMap, HashSet};

pub fn anagrams_for<'a>(word: &str, possible_anagrams: &[&'a str]) -> HashSet<&'a str> {
    // unimplemented!(
    //     "For the '{}' word find anagrams among the following words: {:?}",
    //     word,
    //     possible_anagrams
    // );

    let lower_word = word.to_lowercase();
    let word_frequency = letter_counter(&lower_word);

    possible_anagrams
        .iter()
        .cloned()
        .filter(|candidate| {
            let lower_candidate = candidate.to_lowercase();
            println!(
                "{:?} -> {:?}",
                letter_counter(&lower_candidate),
                word_frequency
            );
            lower_candidate != lower_word && letter_counter(&lower_candidate) == word_frequency
        })
        .collect()
}

fn letter_counter(word: &str) -> HashMap<char, usize> {
    word.chars().fold(HashMap::new(), |mut counter, ch| {
        *counter.entry(ch).or_insert(0) += 1;
        counter
    })
}
