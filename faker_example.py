from faker import Faker

fake = Faker('ru_RU')

print(fake.name())
print(fake.address())
print(fake.email())
print(fake.text())

user_data = {
    "name": fake.name(),
    "email": fake.email(),
    "address": fake.address()
}
print(user_data)