use std::vec;
struct NewVector<T>{
    x: Vec<T>
}

fn main(){
    // This is for integer
    let mut temp_vector = NewVector{
        x: vec![9,8,7,6,5,4,3,2,1]
    };
    let sorted_vector = sort(&mut temp_vector.x);
    println!("The vector is: {:?}", sorted_vector);
    println!("The vector is: {:?}", temp_vector.x);
    let sorted_list = is_sorted(&mut temp_vector.x.clone());
    match sorted_list{
        true => println!("The vector is sorted"),
        false => println!("The vector is unsorted")
    };
}

fn sort<T: std::cmp::PartialOrd + Copy>(vector: &mut Vec<T>) -> (){
    let middle = vector.len()/2;
    if vector.len() < 2{
        return;
    }
    let mut sorted = vector.to_vec();
    sort(&mut vector[..middle].to_vec());
    sort(&mut vector[middle..].to_vec());
    merge(&mut vector[..middle].to_vec(), &mut vector[middle..].to_vec(), &mut sorted);
    vector.copy_from_slice(&sorted);
}

fn merge<T: std::cmp::PartialOrd + Copy>(l_vector: &mut Vec<T>, r_vector: &mut Vec<T>, sorted: &mut Vec<T>) -> (){
    let (mut left, mut right, mut i) = (0,0,0);
    while left < l_vector.len() && right < r_vector.len(){
        if l_vector[left] <= r_vector[right]{
            sorted[i] = l_vector[left];
            i += 1;
            left += 1;
        }
        else{
            sorted[i] = r_vector[right];
            i += 1;
            right += 1;
        }
    }

    if left < l_vector.len(){
        sorted[i..].copy_from_slice(&l_vector[left..]);
    }

    if right < r_vector.len(){
        sorted[i..].copy_from_slice(&r_vector[right..]);
    }
}


fn is_sorted<T: std::cmp::PartialOrd + Copy>(vector: &mut Vec<T>) -> bool{
    for i in 1..vector.len(){
        if vector[i - 1] > vector[i]{
            return false;
        }
    }
    true
}