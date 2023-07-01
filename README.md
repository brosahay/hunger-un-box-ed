# INTRODUCTION

The motivation behind this project was the sh%tty concept of pre-booking food only between the hours 18:00 to 22:30, which might be a peak hour of back to back calls and other activities. Most times people forget to book due to other acitivites of life.
Enough of the rant, lets proceed towards the automation.

So, I wanted to have a headless automated script to book my meals. I started by logging into the application on the browser and analysing the network traffic. I was pleasantly surprised to find REST APIs, which makes this much easier to deal with.

I am capturing the findings below:

## FETCHING THE ACCESS TOKEN USING OAUTH
ENDPOINT
```powershell
POST: /api/oauth/access_token
```
BODY (REQUEST)
```json
{
    "username": "",
    "password": "",
    "grant_type": "password",
    "client_id": "",
    "client_secret": "",
    "company_id":
}
```

BODY (RESPONSE)
```json
{
    "access_token": "",
    "expires_in": ,
    "token_type": "Bearer",
    "scope": "",
    "refresh_token": ""
}
```

This `access_token` can now be used to get around to other APIs, the `refresh_token` can be used to get a new `access_token` without using the user credentials.

## GET EMPLOYEE DETAILS
ENDPOINT
```powershell
GET: /api/users/getEmployeeDetails
```

BODY (RESPONSE)
```json
{
  "data": {
    "id": 0,
    "user_id": 0,
    "leaving_date": 0,
    "general_notification": 0,
    "created_at": 0,
    "updated_at": 0,
    "department": 0,
    "cost_center": 0,
    "on_travel": 0,
    "employee_image": "",
    "app_notification": 0,
    "sms_notification": 0,
    "email_notification": 0,
    "chat_head": 0,
    "feedback_popup": 0,
    "free_card_issued": 0,
    "simpl_eligibility": null,
    "lazypay_eligibility": null,
    "desk_reference": null,
    "email": "",
    "email_verification_token": null,
    "is_email_verified": 0,
    "has_due_bills": 0,
    "external_identifier": null,
    "external_access_token": null,
    "juspay_paylater_eligibility": "",
    "covid_declaration_submitted": 0,
    "gender": null,
    "is_mobile_verified": 0,
    "temporary_mobile_number": null,
    "subscription_enabled": 0,
    "external_json_data": null,
    "subscription_status": "none",
    "last_notification_read": null,
    "delete_response": null
  }
}
```

## FETCH RECENT ORDERS
ENDPOINT
```powershell
GET: /api/recent_orders
```

BODY (RESPONSE)
```json
{
  "data": {
    "lastClosedOrders": {
      "data": []
    },
    "lastOpenOrders": {
      "data": []
    }
  }
}
```

## FETCH BOOKMARKS
ENDPOINT
```powershell
GET: /api/menu/user/bookmarks/fetch/
```

HEADER (REQUEST)
```powershell
locationId=<0000>
occasionId=<0000>
```

RESPONSE (BODY)
```json
{
  "data": {
    "show_images": true,
    "tags": {},
    "UserBookmarks": {
      "data": []
    },
    "TrendingMenu": {
      "data": []
    }
  }
}
```

## GET ALL VENDORS
ENDPOINT
```powershell
GET: /api/listVendors/
```

HEADER (REQUEST)
```powershell
locationId=<0000>
occasionId=<0000>
```

RESPONSE
```json
{
  "data": [
    {
      "occasion_id": 0000,
      "name": "<occasion_name>",
      "label": "",
      "active": 1,
      "display_start_time": "00:00:00",
      "start_time": "00:00:00",
      "end_time": "00:00:00",
      "pre_order": false,
      "code": "",
      "preorder_day": "<day>",
      "preorder_only": 1,
      "current_timestamp": 0000000000,
      "pre_order_enable": false,
      "schedule_start_time": null,
      "schedule_end_time": null,
      "vendor": {
        "data": [
          {
            "vendor_id": 000000,
            "name": "VENDOR NAME",
            "display": "VENDOR NAME",
            "logo": "",
            "type": "default",
            "type_display": "Default",
            "is_buffet": 0,
            "active": 1,
            "vendor_code": "VENDOR",
            "code": "VENDOR",
            "location_id": null,
            "description": null,
            "search_keywords": null,
            "company_id": 000,
            "delivery_expected_time": 0,
            "schedules": [],
            "activeSchedules": [],
            "formattedActiveSchedules": [],
            "start_time": "00:00:00",
            "end_time": "00:00:00",
            "locations": null,
            "companies": null,
            "days_of_week": null,
            "menu_option": null,
            "min_order_amount": 0,
            "delivery_charges": 0,
            "service_tax": "0.00",
            "vat": "0.00",
            "telephone": null,
            "ordering_enabled": true,
            "sort_order": 0,
            "timings": null,
            "deliver_in_lunch": 0,
            "couch_locations": [],
            "vendor_ordering_enabled": 0,
            "sgst": 0,
            "cgst": 0,
            "queued_order": 0,
            "total_gst": null,
            "take_away_available": 0,
            "customer_gst": 0,
            "image": ".jpeg",
            "rating": "0.00",
            "drafts_count": null,
            "disable": false,
            "is_food_festival": 0,
            "new_design_image": ".jpeg",
            "sdk_type": null,
            "next_available_at": null,
            "next_availability_text": null,
            "desk_ordering_enabled": 0,
            "badge_type": "none",
            "is_kitchen_system_enabled": 0,
            "is_slot_booking_vendor": 0,
            "company_name": null,
            "banner_image": ".jpeg",
            "lookup_type": "",
            "enable_hsn": null,
            "gst_details": null,
            "fssai_lic_no": null,
            "hb_gst_details": null,
            "hb_fssai_lic_no": null,
            "tags": null,
            "newMenuManagementEnabled": null,
            "hidden_menus": null
          }
        ]
      }
    }
  ]
}
```

## GET CURRENT USER DETAILS
ENDPOINT
```powershell
GET: /api/current_user/
```

HEADER (REQUEST)
```powershell
locationId=<0000>
occasionId=<0000>
```

BODY (RESPONSE)
```json
{
  "data": {
    "id": 0000000,
    "email": "email@domain.com",
    "username": "email@domain.com",
    "emp_id": "email@domain.com",
    "name": "email@domain.com",
    "wallet": 000,
    "company_id": 000,
    "vendor_id": null,
    "type": "<>",
    "default_location_id": 0000,
    "card_code": null,
    "card_hash": "",
    "employee_type_id": 0000,
    "department_id": null,
    "employee_type": null,
    "card_no": null,
    "mobile_no": "0000000000",
    "reset_required": 0,
    "allowed_in_group_order": false,
    "card_check": 1,
    "active": 1,
    "card_type": null,
    "default_location_name": "<cafeteria-name>",
    "default_location_capacity": 0,
    "desk_ordering_enabled": 0,
    "desk_reference": null,
    "has_due_bills": 0,
    "registration_type": "",
    "required_email_verification": false,
    "is_email_verified": false,
    "is_mobile_verified": 1,
    "updated_email": "email@domain.com",
    "forced_redirect_url": null,
    "master_vendor_name": null,
    "master_vendor_pan": null,
    "subscription_enabled": 0,
    "locations": null,
    "current_wallets": {
      "data": [
        {
          "id": 00000000,
          "company_wallet_id": 0000,
          "amount": 000,
          "display_name": "<wallet-name>",
          "priority": 1,
          "default": 1,
          "employee_can_recharge": 0,
          "convenience_fee": 0,
          "hidden_wallet": 0,
          "wallet_source": "",
          "show_reverse": 0,
          "starting_amount": 000,
          "preferred": null,
          "logo": null,
          "otp_regex": null,
          "alert_message": null,
          "next_expiry_timestamp": 0000000000,
          "payment_group": null,
          "disabled": false,
          "disabled_message": null,
          "wallet_display_type": ""
        }
      ]
    },
    "default_location": {
      "data": {
        "id": 0000,
        "name": "<cafeteria-name>",
        "company_id": 000,
        "label": "<cafeteria-name>",
        "building_name": "<cafeteria-name>",
        "address1": "",
        "active": 1,
        "gstin": null,
        "city_id": null,
        "city_name": null,
        "capacity": 0,
        "latitude": "",
        "longitude": "",
        "total_capacity": 000,
        "start_time": "00:00:00",
        "end_time": "00:00:00",
        "enforce_capacity": 1,
        "enforce_physical_distancing": 0,
        "desk_ordering_enabled": 0,
        "type": "cafe",
        "address_id": 0000,
        "address_line_1": null,
        "address_line_2": null,
        "state_name": null,
        "pincode": null,
        "state_code": null,
        "partner_company_id": null,
        "state_id": null,
        "multi_vendor_ordering_enabled": 0
      }
    }
  },
  "meta": {
    "scopes": {
      "employee": ""
    }
  }
}
```

## GET LIST OF OCCASIONS
ENDPOINT
```powershell
GET: /api/v3/consumer/list-occasions
```
HEADER (REQUEST)
```powershell
locationId=<0000>
```

BODY (RESPONSE)
```json
{
  "data": [
    {
      "id": 0000,
      "name": "<occassion-name>", # All Day, Breakfast, Lunch, Snacks
      "label": "",
      "active": 1,
      "preorder_start_time": "00:00:00",
      "preorder_end_time": "00:00:00",
      "preorder_only": 0,
      "preorder_day": "",
      "occasion_id": 0000,
      "pre_order_days": null,
      "end_time": "00:00:00",
      "start_time": "00:00:00"
    }
  ]
}
```

## REVIEW OF PAST ORDERS
ENDPOINT
```powershell
POST: /api/order/review
```

BODY (REQUEST)
```json
{
  "rating": 0,
  "comment": "",
  "order_id": 0,
  "reference": "order",
  "review_options": []
}
```

# INSTALL

```powershell
python3 -m venv .venv
source ./.venv/bin/activate
pip3 install -r requirements.txt
```
