pub fn verse(n: u32) -> String {
    // unimplemented!("emit verse {}", n)

    if n == 0 {
        return "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n".to_string();
    } else if n == 1 {
        return "1 bottle of beer on the wall, 1 bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall.\n".to_string();
    } else if n == 2 {
        return "2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n".to_string();
    }

    format!("{current} bottles of beer on the wall, {current} bottles of beer.\nTake one down and pass it around, {left} bottles of beer on the wall.\n", current=n, left=n-1)
}

pub fn sing(end: u32, start: u32) -> String {
    // unimplemented!("sing verses {} to {}, inclusive", start, end)

    let mut song = String::new();

    for n in (start..=end).rev() {
        song.push_str(&verse(n));
        song.push_str("\n");
    }

    song.pop();

    song
}
