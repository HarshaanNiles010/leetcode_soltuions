use std::collections::BTreeMap;

fn main() {
    let mut nums: Vec<i32> = Vec::new();
    for i in 0..10 {
        nums.push(i + 1);
    }
    nums.push(10);
    nums.push(9);
    nums.push(8);
    let mut freq: BTreeMap<i32, i32> = freq_distro(&mut nums);
    println!("The freq distro is: ");
    println!("{:#?}", freq);
    let mut keys: Vec<i32> = get_keys(&mut freq).into_iter().rev().collect();
    println!("The keys are: {:#?}", keys);
    let mut values: Vec<i32> = get_values(&mut freq).into_iter().rev().collect();
    println!("The values are: {:#?}", values);
    let new_freq: BTreeMap<i32, i32> = convert_to_btree_map(&mut keys, &mut values);
    println!("{:#?}", new_freq);
}

fn freq_distro(nums: &mut Vec<i32>) -> BTreeMap<i32, i32> {
    let mut temp_freq: BTreeMap<i32, i32> = BTreeMap::new();
    for i in 0..nums.len() {
        if temp_freq.contains_key(&nums[i]) {
            *temp_freq.get_mut(&nums[i]).unwrap() += 1;
        } else {
            temp_freq.insert(nums[i], 1);
        }
    }
    temp_freq
}

fn get_keys(distro: &mut BTreeMap<i32, i32>) -> Vec<i32> {
    let temp: Vec<i32> = distro.keys().cloned().collect();
    temp.to_vec()
}

fn get_values(distro: &mut BTreeMap<i32, i32>) -> Vec<i32> {
    let temp: Vec<i32> = distro.values().cloned().collect();
    temp.to_vec()
}

fn convert_to_btree_map(keys: &mut Vec<i32>, values: &mut Vec<i32>) -> BTreeMap<i32, i32> {
    let mut temp: BTreeMap<i32, i32> = BTreeMap::new();
    for i in 0..keys.len() {
        temp.insert(keys[i], values[i]);
    }
    temp
}
