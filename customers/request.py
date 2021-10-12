CUSTOMERS = [
    {
      "id": 1,
      "name": "Wade",
      "locationId": 1
    },
    {
      "id": 2,
      "name": "Travis",
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Alicia",
      "locationId": 1
    }
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    return requested_customer 