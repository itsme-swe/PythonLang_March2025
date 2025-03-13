class Customer:

    def __init__(self, id, name, blStreet, blCity, country):

        self.custId = id
        self.name = name

        self.billingAddress = self.Address(blStreet, blCity, country)

    def __str__(self):
        return f"CustomerID: {self.custId}\n Name: {self.name}\n Street: {self.billingAddress.street}\n Address: {self.billingAddress.city}\n Country: {self.billingAddress.country}"

    class Address:

        def __init__(self, street, city, country):

            self.street = street
            self.city = city
            self.country = country

        def display(self):
            print(self.street)
            print(self.city)
            print(self.country)


cust1 = Customer(101, "John", "Siddharth Nagar", "Jaipur", "India")

print(cust1)
