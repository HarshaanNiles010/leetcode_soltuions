#[warn(non_snake_case)]
fn main(){
    let length: i32 = 10;
    let mut arr: Vec<i32> = vec![0];
    arr = populate_arr(& mut arr, length);
    println!("The current array is: {:?}", arr);
}

fn populate_arr(nums: &mut Vec<i32>, length: i32) -> Vec<i32>{
    nums.pop();
    for i in 0..length{
        nums.push(i + 1);
    }
    nums.to_vec()
}