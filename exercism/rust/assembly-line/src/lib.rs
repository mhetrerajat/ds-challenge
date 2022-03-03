// This stub file contains items that aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.

pub fn production_rate_per_hour(speed: u8) -> f64 {
    // unimplemented!("calculate hourly production rate at speed: {}", speed)

    const CARS_PER_HOUR: f64 = 221.0;

    let success_factor = match speed {
        0 => 0.0,
        1..=4 => 1.0,
        5..=8 => 0.9,
        9..=10 => 0.77,
        _ => panic!("overflow"),
    };

    CARS_PER_HOUR * success_factor * speed as f64
}

pub fn working_items_per_minute(speed: u8) -> u32 {
    // unimplemented!("calculate the amount of working items at speed: {}", speed)
    production_rate_per_hour(speed) as u32 / 60
}
