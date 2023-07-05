from src.interfaces.Interfaces import ResponseInterface


class Location(ResponseInterface):
    id: int
    name: str
    company_id: int
    label: str
    building_name: str
    address1: str
    active: int
    gstin: str
    city_id: str
    city_name: str
    capacity: int
    latitude: str
    longitude: str
    total_capacity: int
    start_time: str
    end_time: str
    enforce_capacity: int
    enforce_physical_distancing: int
    desk_ordering_enabled: int
    type: str
    address_id: int
    address_line_1: str
    address_line_2: str
    state_name: str
    pincode: str
    state_code: str
    partner_company_id: str
    state_id: str
    multi_vendor_ordering_enabled: int
