#[derive(Debug, Clone)]
#[allow(dead_code)]
pub enum VehicleCompany{
    Toyota,
    Bmw,
    Mercedes,
    Subaru,
    Porche,
    Ferrari,
    Dodge,
    Ford,
}

#[derive(Debug, Clone)]
#[allow(dead_code)]
pub enum VehicleColor{
    Violet,
    Indigo,
    Blue,
    Green,
    Yellow,
    Orange,
    Red,
}

#[derive(Debug, Clone)]
#[allow(dead_code)]
pub enum VehicleFuelType{
    Petrol,
    Disel,
    Hydrogen,
    Electric,
}

#[derive(Debug, Clone)]
#[allow(dead_code)]
pub enum VehicleType{
    Suv,
    HatchBack,
    Sports,
    Coupe,
    CrossOver,
    Minivan,
    Sedan,
    Pickup,
    Convertable,
}

#[derive(Debug, Clone)]
#[allow(dead_code)]
pub struct Vehicle{
    vehicle_name: String,
    vehicle_make: VehicleCompany,
    vehicle_color: VehicleColor,
    vehicle_fuel_type: VehicleFuelType,
    vehicle_type: VehicleType,
    vehicle_make_year: u16,
    vehicle_vin: u16,
}

impl Vehicle{
    pub fn make_new_vehicle() -> Vehicle{
    Vehicle{
            vehicle_name: "Default".to_string(),
            vehicle_make: VehicleCompany::Toyota,
            vehicle_color: VehicleColor::Violet,
            vehicle_fuel_type: VehicleFuelType::Electric,
            vehicle_type: VehicleType::Suv,
            vehicle_make_year: 2024,
            vehicle_vin: 12345,
        }
    }
    pub fn make_specific_vehicle(   
        name: String, 
        make: VehicleCompany,  
        color: VehicleColor,
        fuel: VehicleFuelType,
        v_type: VehicleType,
        make_year: u16,
        vin: u16
    ) -> Vehicle{
        Vehicle{
            vehicle_name: name.to_string(),
            vehicle_make: make,
            vehicle_color: color,
            vehicle_fuel_type: fuel,
            vehicle_type:v_type,
            vehicle_make_year: make_year,
            vehicle_vin: vin
        }

    }
}