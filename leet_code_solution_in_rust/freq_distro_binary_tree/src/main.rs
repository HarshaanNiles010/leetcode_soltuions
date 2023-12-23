use std::collections::BTreeMap;


fn main(){
    let mut nums: Vec<i32> = Vec::new();
    for i in 0..10{
        nums.push(i + 1);
    }
    let freq: BTreeMap<i32, i32> = freq_distro(&mut nums);
    println!("The freq distro is: ");
    println!("{:?}", freq);
}

fn freq_distro(nums: &mut Vec<i32>) -> BTreeMap<i32, i32>{
    let mut temp_freq: BTreeMap<i32,i32> = BTreeMap::new();
    for i in 0..nums.len(){
        if temp_freq.contains_key(&nums[i]){
            *temp_freq.get_mut(&nums[i]).unwrap() += 1;
        }
        else{
            temp_freq.insert(nums[i], 1);
        }
    }
    temp_freq
}