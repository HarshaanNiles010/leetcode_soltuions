use std::vec;
struct NewVector<T>{
    x: Vec<T>
}

fn main(){
    // This is for integers
    let mut nums: Vec<i32> = vec![1,2,3,4,5];
    let largest = find_largest(&mut nums);
    let smallest = find_smallest(&mut nums);
    println!("The largest element in: {:?} is {}", nums, largest);
    println!("The smallest element in: {:?} is {}", nums, smallest);
    // This is for the float
    let mut floating_nums: Vec<f64> = vec![1.,2.,3.,4.,5.,6.];
    let largest_floating_num = find_largest(&mut floating_nums);
    let smallest_floating_num = find_smallest(&mut floating_nums);
    println!("The largest element in: {:?} is {}", floating_nums, largest_floating_num);
    println!("The smallest element in: {:?} is {}", floating_nums, smallest_floating_num);
    // This is for the vector of integer
    let mut new_vector = NewVector{
        x: vec![6,5,4,3,2,1]
    };
    let largest_in_vector = find_largest(&mut new_vector.x);
    println!("The largest element in: {:?} is {}",new_vector.x, largest_in_vector);
    let mut sorted = is_sorted(&mut new_vector.x);
    println!("The vector is: {:?}", new_vector.x);
    match sorted{
        true => println!("The vector is sorted"),
        false => println!("The vector is unsorted")
    };
    new_vector.x = sort_the_vetor(&mut new_vector.x);
    println!("The vector is: {:?}", new_vector.x);
    sorted = is_sorted(&mut new_vector.x);
    match sorted{
        true => println!("The vector is sorted"),
        false => println!("The vector is unsorted")
    };
}



fn sort_the_vetor<T: std::cmp::PartialOrd + Copy>(vector: &mut Vec<T>) -> Vec<T>{
    for i in 0..vector.len(){
        for j in 0..vector.len() - i - 1{
            if vector[j] > vector[j + 1]{
                vector.swap(j, j + 1);
            }
        }
    }
    vector.to_vec()
}

fn is_sorted<T: std::cmp::PartialOrd + Copy>(vector: &mut Vec<T>) -> bool{
    for i in 1..vector.len(){
        if vector[i - 1] > vector[i]{
            return false;
        }
    }
    true
}


fn find_largest<T: std::cmp::PartialOrd + Copy>(vector: &mut Vec<T>) -> T{
    let mut temp = &vector[0];
    for i in 1..vector.len(){
        if vector[i] >= *temp{
            temp = &vector[i];
        }
    }
    *temp
}

fn find_smallest<T: std::cmp::PartialOrd + Copy>(vector: &mut Vec<T>) -> T{
    let mut temp = &vector[0];
    for i in 1..vector.len(){
        if vector[i] <= *temp{
            temp = &vector[i];
        }
    }
    *temp
}