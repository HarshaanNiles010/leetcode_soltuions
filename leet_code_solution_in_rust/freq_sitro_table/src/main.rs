use std::collections::HashMap;
fn main(){
    let mut nums: Vec<i32> = Vec::new();
    for i in 0..10{
        nums.push(i + 1);
    }
    let freq: HashMap<i32, i32> = freq_distro(&mut nums);
    println!("The freq distribution is:");
    println!("{:?}",freq);
}

fn freq_distro(nums: &mut Vec<i32>) -> HashMap<i32, i32>{
    let mut freq: HashMap<i32, i32> = HashMap::new();
    for i in 0..nums.len(){
        if freq.contains_key(&nums[i]){
            *freq.get_mut(&nums[i]).unwrap() += 1;
        }
        else{
            freq.insert(nums[i], 1);
        }
    } 
    freq 
}