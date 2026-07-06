from dataclasses import dataclass

@dataclass(frozen=True)
class Customer:
    id: int
    name: str
    email: str
    
    def get_info(self) -> str:
        return f"Customer ID: {self.id}, Name: {self.name}, Email: {self.email}"


class CustomerRepository:
    def __init__(self) -> None:
        self._customers: list[Customer] = []

    def add_customer(self, customer: Customer):
        self._customers.append(customer)

    def get_all_customers(self) -> list[Customer]:
        return self._customers


