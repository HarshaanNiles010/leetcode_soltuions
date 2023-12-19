#[allow(unused_variables)]

fn main(){
    let length: i32 = 10;
    let target: i32 = 5;
    let mut arr: Vec<i32> = vec![0];
    arr = populate_arr(&mut arr, length);
    let position: usize = find_target(&mut arr, target);
    println!("The position is: {}", position);
}

fn populate_arr(arr: &mut Vec<i32>, length: i32) -> Vec<i32>{
    arr.pop();
    for i in 0..length{
        arr.push(i + 1);
    }
    arr.to_vec()
}

fn find_target(arr: &mut Vec<i32>, target: i32) -> usize{
    let mut left = 0;
    let mut right = arr.len() - 1;
    while left < right{
        let mut mid: usize = left + ((right - left)/2);
        if arr[mid] == target{
            mid
        }
        else if arr[mid] > target{
            right -= 1;
        }
        else if arr[mid] < target{
            left += 1;
        }
    }
    -1
}