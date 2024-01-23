fn main(){
    let mut height: Vec<i32> = vec![0,1,0,2,1,0,1,3,2,1,2,1];
    let max_area: i32 = trap(&mut height);
    println!("max area is: {}", max_area);
}

fn trap(height: &mut Vec<i32>) -> i32{
    if height.is_empty(){
        return 0;
    }
    let mut left: usize = 0;
    let mut right: usize = height.len() - 1;
    let mut max_left: i32 = height[left];
    let mut max_right: i32 = height[right];
    let mut result: i32 = 0;

    while left < right{
        if max_left < max_right{
            left += 1;
            max_left = max_left.max(height[left]);
            result += max_left - height[left];
        }
        else{
            right -= 1;
            max_right = max_right.max(height[right]);
            result += max_right - height[right];
        }
    }
    result
}

