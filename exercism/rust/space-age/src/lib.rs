// The code below is a stub. Just enough to satisfy the compiler.
// In order to pass the tests you can add-to or change any of this code.

#[derive(Debug)]
pub struct Duration {
    years_on_earth: f64,
}

impl From<u64> for Duration {
    fn from(s: u64) -> Self {
        Duration {
            years_on_earth: s as f64 / (365.25 * 24.0 * 60.0 * 60.0),
        }
    }
}

pub trait Planet {
    fn years_during(d: &Duration) -> f64 {
        d.years_on_earth / Self::period_factor()
    }

    fn period_factor() -> f64;
}

macro_rules! planet {
    ($planet_name:ident, $factor:expr) => {
        pub struct $planet_name;
        impl Planet for $planet_name {
            fn period_factor() -> f64 {
                $factor
            }
        }
    };
}

planet!(Mercury, 0.2408467);
planet!(Venus, 0.61519726);
planet!(Earth, 1.0);
planet!(Mars, 1.8808158);
planet!(Jupiter, 11.862615);
planet!(Saturn, 29.447498);
planet!(Uranus, 84.016846);
planet!(Neptune, 164.79132);
