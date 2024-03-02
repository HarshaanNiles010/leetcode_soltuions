use cars::Vehicle;
pub mod cars;
fn main(){
    let _first_car = Vehicle::make_new_vehicle();
    let _second_car = Vehicle::make_specific_vehicle(
        "Kachaoow".to_string(), 
        cars::VehicleCompany::Ferrari, 
        cars::VehicleColor::Indigo, 
        cars::VehicleFuelType::Electric, 
        cars::VehicleType::Sedan, 
        2022, 
        13579
    );
    println!("The car is: {:#?}", _first_car);
    println!("The car is: {:#?}", _second_car);
}