fn main(){
    let mut nums: Vec<i32> = Vec::new();
    for i in 0..10{
        nums.push(i + 1);
    }
    for i in nums.iter(){
        match i{
            i if (i % 3) == 0 => println!("Fizz"),
            i if (i % 5) == 0 => println!("Buzz"),
            i if (i % 5) == 0 && (i % 3) == 0 => println!("FizzBuzz"),
            _ => println!("__")
        }
    }
}