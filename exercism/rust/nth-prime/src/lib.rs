#[allow(dead_code)]
fn is_prime(n: u32) -> bool {
    let mut factors = 0;

    for x in 1..n {
        if n % x == 0 {
            factors += 1;
        }
    }

    // the number should have only 1 factor
    // since prime number is divisible by only 2 numbers, 1 and that number itself
    // since we are checking from 2, there should be only 1 factor
    if factors == 1 {
        return true;
    }

    false
}

#[allow(dead_code)]
fn naive_approach(n: u32) -> u32 {
    // Does not works with large numbers

    let mut counter = 0;
    let mut number = 1;

    loop {
        if is_prime(number) {
            counter += 1;
        }

        // since 0th is the 1st element
        if n + 1 == counter {
            // found the nth number
            break;
        }

        // increment number by 1 after each iteration
        number += 1;
    }

    number
}

pub fn nth(n: u32) -> u32 {
    // Initialize with true
    const MAX_LIMIT: usize = 1_000_000;
    let mut map: [u8; MAX_LIMIT] = [1; MAX_LIMIT];

    let mut pointer = 2;

    while pointer * pointer <= MAX_LIMIT {
        if map[pointer] == 1 {
            for x in pointer * pointer..MAX_LIMIT {
                if x % pointer == 0 {
                    map[x] = 0;
                }
            }
        }

        pointer += 1;
    }

    let mut counter = 0;
    for (idx, is_prime) in map.iter().enumerate() {
        if idx == 0 || idx == 1 {
            continue;
        }

        if n - counter == 0 && is_prime == &1 {
            return idx as u32;
        }

        if is_prime == &1 {
            counter += 1;
        }
    }

    0
}
