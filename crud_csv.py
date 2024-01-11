'''This program template grew out of a need to test front ends without having to install and set up a database every time.

It aims to mimic a basic database crud interface'''

import csv

# Example models

class Customer:
    Id: int
    GivenName: str
    Surname: str
    Streetaddress: str
    City: str
    Zipcode: str
    Country: str
    CountryCode: str
    NationalId: str
    TelephoneCountryCode: int
    Telephone: str
    EmailAddress: str

class CustomerData:
    id: int
    given_name: str
    surname: str
    streetaddress: str
    city: str
    zipcode: str
    country: str
    country_code: str
    national_id: str
    phone_country_code: int
    telephone: str
    email_address: str

# Example models end

class CRUD_csv:
    def __init__(self) -> None:
        self._customers = 'customers.csv'                   # Enter name of csv file
        self._customers_headers = ['Id',                    # Enter headers of csv file
                                   'GivenName',
                                   'Surname',
                                   'Streetaddress',
                                   'City',
                                   'Zipcode',
                                   'Country',
                                   'CountryCode',
                                   'NationalId',
                                   'TelephoneCountryCode',
                                   'Telephone',
                                   'EmailAddress']

        try:        # Sets up the csv files if they do not already exist
            with open(self._customers, 'x', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self._customers_headers)
                writer.writeheader()
        except FileExistsError:
            pass

    def _get_headers(self, csvfile: str) -> list[str]:
        if csvfile == self._customers:
            return self._customers_headers
        else:   # Should never fire if this method and __init__ has been set up correctly
            raise LookupError

    # CSV methods
    def _csv_read(self, csvfile: str) -> list[dict[str, str]]:
        with open(csvfile, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return_data = []
            for row in reader:
                return_data.append(row)
        return return_data
    
    def _csv_write(self, csvfile: str, data_list: list[dict[str, str]]) -> None:
        headers = self._get_headers(csvfile)
        with open(csvfile, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for row in data_list:
                writer.writerow(row)

    def _csv_append(self, csvfile: str, data_dict: dict[str, str]) -> None:
        headers = self._get_headers(csvfile)
        with open(csvfile, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writerow(data_dict)

    # Model assemblers
    def _assemble_customer(self, data_dict: dict[str, str]) -> Customer:
        customer = Customer()
        customer.Id = int(data_dict['Id'])
        customer.GivenName = data_dict['GivenName']
        customer.Surname = data_dict['Surname']
        customer.Streetaddress = data_dict['Streetaddress']
        customer.City = data_dict['City']
        customer.Zipcode = data_dict['Zipcode']
        customer.Country = data_dict['Country']
        customer.CountryCode = data_dict['CountryCode']
        customer.NationalId = data_dict['NationalId']
        customer.TelephoneCountryCode = int(data_dict['TelephoneCountryCode'])
        customer.Telephone = data_dict['Telephone']
        customer.EmailAddress = data_dict['EmailAddress']
        return customer

    # Customer CRUDs
    def create_customer(self, data: CustomerData) -> None:
        current_customer_count = len(self._csv_read(self._customers))
        data_dict = {'Id': str(current_customer_count + 1),
                     'GivenName': data.given_name,
                     'Surname': data.surname,
                     'Streetaddress': data.streetaddress,
                     'City': data.city,
                     'Zipcode': data.zipcode,
                     'Country': data.country,
                     'CountryCode': data.country_code,
                     'NationalId': data.national_id,
                     'TelephoneCountryCode': data.phone_country_code,
                     'Telephone': data.telephone,
                     'EmailAddress': data.email_address}
        self._csv_append(self._customers, data_dict)

    def read_all_customers(self) -> list[Customer]:
        data = self._csv_read(self._customers)
        all_customers = []
        for row in data:
            customer = self._assemble_customer(row)
            all_customers.append(customer)
        return all_customers
    
    def read_all_customers_by_given_name(self, customer_given_name: str) -> list[Customer]:
        data = self._csv_read(self._customers)
        select_customers = []
        for row in data:
            if row['GivenName'] == customer_given_name:
                customer = self._assemble_customer(row)
                select_customers.append(customer)
        return select_customers
    
    def read_all_customers_by_surname(self, customer_surname: str) -> list[Customer]:
        data = self._csv_read(self._customers)
        select_customers = []
        for row in data:
            if row['Surname'] == customer_surname:
                customer = self._assemble_customer(row)
                select_customers.append(customer)
        return select_customers
    
    def read_all_customers_by_city(self, customer_city: str) -> list[Customer]:
        data = self._csv_read(self._customers)
        select_customers = []
        for row in data:
            if row['City'] == customer_city:
                customer = self._assemble_customer(row)
                select_customers.append(customer)
        return select_customers

    def read_customer_by_id(self, customer_id: int) -> Customer:
        data = self._csv_read(self._customers)
        for row in data:
            if row['Id'] == str(customer_id):
                customer = self._assemble_customer(row)
                return customer

    def update_customer(self, data: CustomerData) -> None:
        data_dict = {'Id': data.id,
                     'GivenName': data.given_name,
                     'Surname': data.surname,
                     'Streetaddress': data.streetaddress,
                     'City': data.city,
                     'Zipcode': data.zipcode,
                     'Country': data.country,
                     'CountryCode': data.country_code,
                     'NationalId': data.national_id,
                     'TelephoneCountryCode': data.phone_country_code,
                     'Telephone': data.telephone,
                     'EmailAddress': data.email_address}

        all_customer_data = self._csv_read(self._customers)
        for row in all_customer_data:
            if row['Id'] == data_dict['Id']:
                index = all_customer_data.index(row)
                all_customer_data[index] = data_dict
                break
        self._csv_write(self._customers, all_customer_data)
