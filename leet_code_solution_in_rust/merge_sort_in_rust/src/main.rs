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
    let mut sorted_list = is_sorted(&mut temp_vector.x.clone());
    match sorted_list{
        true => println!("The vector in struct is sorted"),
        false => println!("The vector in struct is unsorted")
    };
    temp_vector.x = sorted_vector;
    sorted_list = is_sorted(&mut temp_vector.x.clone());
    match sorted_list{
        true => println!("The vector is sorted"),
        false => println!("The vector is unsorted")
    };
}

fn sort<T: std::cmp::PartialOrd + Copy>(vector: &mut Vec<T>) -> Vec<T>{
    if vector.len() < 2{
        vector.to_vec()
    }
    else{
        let size = vector.len() / 2;
        let mut left = sort(&mut vector[0..size].to_vec());
        let mut right = sort(&mut vector[size..].to_vec());
        let merged = merge(&mut left, &mut right);
        merged
    }
}

fn merge<T: std::cmp::PartialOrd + Copy>(l_vector: &mut Vec<T>,r_vector: &mut Vec<T>) -> Vec<T>{
    let mut i = 0;
    let mut j = 0;
    let mut merged = Vec::new();

    while i < l_vector.len() && j < r_vector.len(){
        if l_vector[i] < r_vector[j]{
            merged.push(l_vector[i]);
            i = i + 1;
        }
        else{
            merged.push(r_vector[j]);
            j = j + 1;
        }
    }

    if i < l_vector.len(){
        while i < l_vector.len(){
            merged.push(l_vector[i]);
            i = i + 1;
        }
    }

    if j < r_vector.len(){
        while j < r_vector.len(){
            merged.push(r_vector[j]);
            j = j + 1;
        }
    }
    merged 
}


fn is_sorted<T: std::cmp::PartialOrd + Copy>(vector: &mut Vec<T>) -> bool{
    for i in 1..vector.len(){
        if vector[i - 1] > vector[i]{
            return false;
        }
    }
    true
}