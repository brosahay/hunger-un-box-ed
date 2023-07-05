from src.interfaces.Interfaces import ResponseInterface


class Wallet(ResponseInterface):
    id: int
    company_wallet_id: int
    amount: int
    display_name: str
    priority: int
    default: int
    employee_can_recharge: int
    convenience_fee: int
    hidden_wallet: int
    wallet_source: str
    show_reverse: int
    starting_amount: int
    preferred: str
    logo: str
    otp_regex: str
    alert_message: str
    next_expiry_timestamp: int
    payment_group: str
    disabled: bool
    disabled_message: str
    wallet_display_type: str
