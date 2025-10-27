from pydantic import BaseModel


class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = True  # Значение по умолчанию

user1 = User(
    id=1, 
    name="Alice", 
    email="alice@example.com",
    address=Address(city="New York", zip_code="10001")
)
print(user1)

user2 = User(
    id="123", 
    name="Alice", 
    email="alice@example.com", 
    address={"city": "New York", "zip_code": "10001"}
)
print(user2.id)  # 123 (автоматически преобразован в int)
print(user2.model_dump_json())  # Выводит JSON-строку