fn main(){
    let vec_length: i32 = 10;
    let mut nums: Vec<i32> = vec![0];
    nums = populate(&mut nums, vec_length);
    println!("The current vector is: {:?}", nums);
    nums = bubble_sort(&mut nums);
    println!("The sorted vector is: {:?}", nums);
}

fn populate(nums: &mut Vec<i32>, length: i32) -> Vec<i32>{
    nums.pop();
    for i in 0..length{
        nums.push(length - i);
    }
    nums.to_vec()
}

fn bubble_sort(nums: &mut Vec<i32>) -> Vec<i32>{
    let mut temp: i32;
    for i in 0..nums.len(){
        for j in 0..nums.len(){
            if nums[i] < nums[j]{
                temp = nums[j];
                nums[j] = nums[i];
                nums[i] = temp;
            }
        }
    }
    nums.to_vec()
}