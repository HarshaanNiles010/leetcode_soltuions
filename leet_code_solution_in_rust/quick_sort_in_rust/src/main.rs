struct NewVector<T>{
    x: Vec<T>
}

fn main(){
    let mut nums: Vec<i32> = vec![1,2,3,4,5,6,7,8,9,10];
    println!("The nums is: {:?}", nums);
    let is_it_sorted: bool = is_sorted(&mut nums);
    match is_it_sorted{
        true => println!("The temp vector is sorted"),
        false => println!("The temp vector is unsorted")
    };
    let temp_new_vector = NewVector{
        x: vec![6,5,4,3,2,1]
    };
    println!("The vector is: {:?}", temp_new_vector.x.clone());
    let mut is_vector_sorted = is_sorted(&mut temp_new_vector.x.clone());
    match is_vector_sorted{
        true => println!("The vector temp_new_vector is sorted "),
        false => println!("The vector temp_new_vector is unsorted ")
    };
    quicksort(&mut temp_new_vector.x.clone(), 1, temp_new_vector.x.clone().len() - 1);
    is_vector_sorted = is_sorted(&mut temp_new_vector.x.clone());
    match is_vector_sorted{
        true => println!("The vector temp_new_vector is sorted "),
        false => println!("The vector temp_new_vector is unsorted ")
    };
}


fn is_sorted<T: std::cmp::PartialOrd + Copy>(vector: &mut Vec<T>) -> bool{
    for i in 1..vector.len(){
        if vector[i - 1] > vector[i]{
            return false;
        }
    }
    true
}

fn quicksort<T: Eq + PartialEq + Clone + PartialOrd>(arr: &mut Vec<T>, low: usize, high: usize) {
    if low < high {
        let p = partition(arr, low, high, &|a, b| {a <= b});
        quicksort(arr, low, p-1);
        quicksort(arr, p+1, high);
    }
}
fn partition<T: Clone, F: Fn(&T, &T) -> bool>(arr: &mut Vec<T>, low: usize, high: usize, f: &F) -> usize {
    let pivot = match arr.get(high) {
        Some(v) => {v.clone()}
        _ => {panic!("Array index {:?} out of bounds", high)}
    };
    let mut i = low;
    for j in low..high-1 {
        match arr.to_vec().get(j) {
            Some(v) => {
                if f(v, &pivot) {
                    let _ = &arr.swap(i, j);
                    i += 1;
                }
            }
            _ => {panic!("Array index {:?} for j out of bounds", j)}
        }
    }
    let _ = &arr.swap(i, high);
    i
}