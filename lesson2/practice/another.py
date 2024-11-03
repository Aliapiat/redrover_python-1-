from faker import Faker
import random
import string

fake = Faker(['ru_RU'])
Faker.seed()  # фиксируем seed для воспроизводимости результатов


def generate_phone_number():
    # Генерируем валидный номер мобильного телефона с международным кодом
    country_code = random.choice(['+375', '+7'])
    if country_code == '+375':
        operator_code = random.choice(['29', '33', '44', '25'])
        subscriber_number = ''.join(random.choices(string.digits, k=7))
        return f"{country_code} ({operator_code}) {subscriber_number[:3]} {subscriber_number[3:5]} {subscriber_number[5:]}"
    elif country_code == '+7':
        operator_code = random.choice(['900', '901', '902', '903', '904', '905', '906', '909'])
        subscriber_number = ''.join(random.choices(string.digits, k=7))
        return f"{country_code} ({operator_code}) {subscriber_number[:3]} {subscriber_number[3:5]} {subscriber_number[5:]}"



def generate_email():
    # random_suffix = random.randint(100, 999)  # Рандомное число от 100 до 999
    random_suffix = ''.join(random.choices(string.digits, k=3))
    return f'alexeypet5+{random_suffix}@gmail.com'



def generate_password():
    # Генерируем случайные буквы и цифры для пароля
    uppercase_letter = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    other_characters = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    # Собираем пароль и перемешиваем символы
    password = list(uppercase_letter + digit + other_characters)
    random.shuffle(password)

    return ''.join(password)

# Генерация имени и фамилии
first_name = fake.first_name_male()
last_name = fake.last_name()
email = generate_email()
phone_number = generate_phone_number()
password = generate_password()
male_first_name = fake.first_name_male()
company_website = fake.domain_name()




# Вывод сгенерированных данных
print(f'Имя: {first_name}')
print(f'Фамилия: {last_name}')
print(f'Номер телефона: {phone_number}')
print(f'Email: {email}')
print(f"Пароль: {password}")
print(f'--------------- step 2 ---------------')
print(f'{last_name} {first_name} {male_first_name}')
print(f'Сайт компании: https://{company_website}')



