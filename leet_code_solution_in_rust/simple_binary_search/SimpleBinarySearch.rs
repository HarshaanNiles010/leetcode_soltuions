use std::cmp::Ordering;

#[allow(unused_variables)]
#[warn(non_snake_case)]
fn main(){
    let length: i32 = 10;
    let target: i32 = 5;
    let mut arr: Vec<i32> = vec![0];
    arr = populate_arr(&mut arr, length);
    let position: i32 = find_target(&mut arr, target);
    println!("The position is: {}", position);
}
// This is working fine 
fn populate_arr(arr: &mut Vec<i32>, length: i32) -> Vec<i32>{
    arr.pop();
    for i in 0..length{
        arr.push(i + 1);
    }
    arr.to_vec()
}
// This is not working properly
fn find_target(arr: &mut Vec<i32>, target: i32) -> i32{
    let mut left: usize = 0_usize;
    let mut right: usize = arr.len();
    let mut idx: usize;
    while left < right{
        idx = (left + right)/2;
        match arr[idx].cmp(&target){
            Ordering::Less => left = idx + 1,
            Ordering::Greater => right = idx,
            Ordering::Equal => {return idx as i32;}
        }
    }
    -1
}
