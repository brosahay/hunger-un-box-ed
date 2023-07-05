from src.interfaces.Interfaces import ResponseInterface


class Occassion(ResponseInterface):
    id: int
    name: str  # All Day, Breakfast, Lunch, Snacks
    label: str
    active: int
    preorder_start_time: str
    preorder_end_time: str
    preorder_only: int
    preorder_day: str
    occasion_id: int
    pre_order_days: str
    end_time: str
    start_time: str
