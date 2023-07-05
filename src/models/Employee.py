import src.interfaces.Interfaces as Interfaces


class Employee(Interfaces.ResponseInterface):
    id: int
    user_id: int
    leaving_date: int
    general_notification: int
    created_at: int
    updated_at: int
    department: int
    cost_center: int
    on_travel: int
    employee_image: str
    app_notification: int
    sms_notification: int
    email_notification: int
    chat_head: int
    feedback_popup: int
    free_card_issued: int
    simpl_eligibility: int
    lazypay_eligibility: int
    desk_reference: int
    email: str
    email_verification_token: int
    is_email_verified: int
    has_due_bills: int
    external_identifier: int
    external_access_token: int
    juspay_paylater_eligibility: str
    covid_declaration_submitted: int
    gender: int
    is_mobile_verified: int
    temporary_mobile_number: int
    subscription_enabled: int
    external_json_data: int
    subscription_status: str
    last_notification_read: int
    delete_response: int

    def deserialize(self, json_str: str) -> object:
      temp = Interfaces.ResponseInterface.deserialize
      return temp.data
