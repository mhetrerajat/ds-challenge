use std::fmt::{Display, Formatter, Result};
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Clock {
    hours: i32,
    minutes: i32,
}

impl Display for Clock {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        write!(f, "{:0>2}:{:0>2}", self.hours, self.minutes)
    }
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {
        let (h, m) = Clock::normalize(hours, minutes);
        Self {
            hours: h,
            minutes: m,
        }
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        Clock::new(self.hours, self.minutes + minutes)
    }

    fn normalize(mut hours: i32, mut minutes: i32) -> (i32, i32) {
        while minutes < 0 {
            minutes += 60;
            hours -= 1;
        }

        while hours < 0 {
            hours += 24;
        }

        hours += minutes / 60;

        (hours % 24, minutes % 60)
    }
}
