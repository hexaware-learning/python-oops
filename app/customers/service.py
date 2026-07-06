from .customer import Customer, CustomerRepository
from httpx import AsyncClient


class CustomerService:
    def __init__(self, repository: CustomerRepository, http_client: AsyncClient):
        self.repository = repository
        self.http_client = http_client

    async def get_customer_orders(self, customer_id: int):
        response = await self.http_client.get(
            f"https://api.example.com/customers/{customer_id}/orders",
            timeout=10.0
        )
        await self.http_client.aclose()
        return response.json()

    async def add_customer(self, id: int, name: str, email: str):
        order_data = await self.get_customer_orders(id)
        customer = Customer(id=id, name=name, email=email)
        self.repository.add_customer(customer)
    
    def get_all_customers(self):
        return self.repository.get_all_customers()


httpx   = AsyncClient()
service = CustomerService(CustomerRepository(), httpx)


async def add_customer_async() -> list[Customer]:
    customers = [
        (1, "John Doe", "john.doe@example.com"),
        (2, "Jane Smith", "jane.smith@example.com"),
        (3, "Alice Johnson", "alice.johnson@example.com"),
        (4, "Bob Brown", "bob.brown@example.com"),
        (5, "Charlie Davis", "charlie.davis@example.com"),
        (1, "Duplicate John", "duplicate.john@example.com")
    ]
    for id, name, email in customers:
        await service.add_customer(id, name, email)

    return service.get_all_customers()


async def process_customers_async(customers: list[Customer]) -> dict:
    if not customers:
        print("No customers to process.")
        return {
            "count": 0,
            "customers": []
        }
    
    seen_ids = set()
    valid_customers = []

    for customer in customers:
        if customer.id in seen_ids:
            print(f"Duplicate customer ID found: {customer.id} {customer.name}. Skipping.")
            continue
        seen_ids.add(customer.id)
        valid_customers.append(customer)
    
    valid_customers.sort(key=lambda c: c.name)
    
    return {
        "count": len(valid_customers),
        "customers": valid_customers
    }


async def main() -> None:
    customer_info = await add_customer_async()
    result = await process_customers_async(customers=customer_info)
    print(result)
