pub fn verse(n: u32) -> String {
    match n {
        0 => "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n".to_string(),
        1 => "1 bottle of beer on the wall, 1 bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall.\n".to_string(),
        _ => format!("{current} {fmt_bottles} of beer on the wall, {current} {fmt_bottles} of beer.\nTake one down and pass it around, {left} {left_fmt_bottles} of beer on the wall.\n", current=n, left=n-1, fmt_bottles=format_bottles(n), left_fmt_bottles=format_bottles(n-1))
    }
}

fn format_bottles(n: u32) -> String {
    match n {
        1 => "bottle".to_string(),
        _ => "bottles".to_string(),
    }
}

pub fn sing(end: u32, start: u32) -> String {
    let song: Vec<String> = (start..=end).rev().map(verse).collect();
    song.join("\n")
}
