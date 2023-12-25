fn main(){
    let mut height: Vec<i32> = vec![1,8,6,2,5,4,8,3,7];
    let max_area: i32 = area_max(&mut height);
    println!("The max area is: {}", max_area);
}

fn area_max(height: &mut Vec<i32>) -> i32{
    let mut max_area: i32 = 0;
    let mut left: usize = 0;
    let mut right: usize = height.len() - 1;

    while left < right{
        let area = ((right - left) as i32) * height[left].min(height[right]);
        max_area = area.max(max_area);
        if height[left] > height[right]{
            right -= 1;
        }
        else{
            left += 1;
        }
    }
    max_area
}