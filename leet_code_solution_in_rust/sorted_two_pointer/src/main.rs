use std::cmp::Ordering::{Equal, Greater, Less};
fn main(){
    let length: i32 = 10;
    let target: i32 = 14;
    let mut nums: Vec<i32> = vec![];
    nums = populate_nums(&mut nums, length);
    let index_arr: [i32; 2] = sorted_two_pointers(&mut nums, target);
    println!("The target indexes are: {:?}",index_arr);
    let new_index: Vec<i32> = new_sorted_two_pointers(&mut nums, target).to_vec();
    println!("The target indexes are: {:?}", new_index);
}

fn populate_nums(nums: &mut Vec<i32>, length: i32) -> Vec<i32>{
    for i in 0..length{
        nums.push(i + 1);
    }
    nums.to_vec()
}

fn sorted_two_pointers(nums: &mut Vec<i32>, target: i32) -> [i32;2]{
    let mut left: usize = 0;
    let mut right: usize = nums.len() - 1;
    let mut target_sum: i32;
    let mut target_idx: [i32; 2] = [-1,-1];
    while left < right{
        target_sum = nums[left] + nums[right];
        if target_sum == target{
            target_idx[0] = left as i32;
            target_idx[1] = right as i32;
            return target_idx;
        }
        else if target_sum < target{
            left += 1;
        }
        else if target_sum > target{
            right -= 1;
        }
    }
    return target_idx;
}

// Sorted two pointers but more rusty way

fn new_sorted_two_pointers(nums: &mut Vec<i32>, target: i32) -> Vec<i32>{
    let (mut l, mut r) = (0, nums.len() - 1);
    while l < r{
        match(nums[l] + nums[r]).cmp(&target){
            Less => l += 1,
            Greater => r -= 1,
            Equal => return vec![l as i32 + 1, r as i32 + 1]
        }
    }
    unreachable!("Test did not follow the constraints!")
}