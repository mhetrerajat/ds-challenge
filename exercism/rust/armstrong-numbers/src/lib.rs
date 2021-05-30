pub fn is_armstrong_number(num: u32) -> bool {
    const RADIX: u32 = 10;
    let mut number = num;
    let mut num_chars = 1;

    loop {
        if number < RADIX {
            break;
        }

        number = number / RADIX;

        num_chars += 1;
    }

    let mut number = num;
    let mut result = 0;
    for _ in 0..num_chars {
        result += (number % RADIX).pow(num_chars);
        number = number / RADIX;
    }

    result == num
}
