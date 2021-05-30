pub fn build_proverb(list: &[&str]) -> String {
    let mut result = String::new();
    let length = if list.len() != 0 { list.len() - 1 } else { 0 };

    for idx in 0..length {
        result.push_str(
            format!(
                "For want of a {} the {} was lost.\n",
                list[idx],
                list[idx + 1]
            )
            .as_str(),
        );
    }

    if list.len() >= 1 {
        result.push_str(format!("And all for the want of a {}.", list[0]).as_str());
    }

    result
}
