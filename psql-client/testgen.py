from faker import Faker

fake = Faker()

with open("testname.csv", "w") as f:
    f.write("\n".join(fake.name() for _ in range(100)))