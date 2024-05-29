from datetime import datetime

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Lenguage Uzbek>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

user_info = {
    "first_name": "Muslima", "last_name": "Nematova",
    "card_password": 1234 , "card_balance": 2000000,
    "card_number":"8600963096308520",
    "phone_number": "", "status": False}
data_atm = {"balance": 5000000}

def uzbek_balance_display():
    a = input(f"""
    Sizning balansingiz {user_info["card_balance"]} so'm
    Boshqa xizmatdan foydalanishni istaysizmi?
        1. Ha
        2. Yo'q
            >>> """)

    if a == "1":
        return uzbek_services()

    elif a == "2":
        return main()

    else:
        print("Error")
        return uzbek_balance_display()

def uzbek_balance_check():
    print("Bizni tanlaganiz uchun tashakkur")
    check = f"""
                CHECK
        Balance: {user_info["card_balance"]}
        Card: {12 * "*" + user_info["card_number"][-4::]}
        Time: {datetime.now()}
    """
    print(check)
    return main()

def uzbek_service_balance():
    print("<<<<<<<<<Balance>>>>>>>>")
    services = input("""
        1. Ekranda ko'rish
        2. Chekda ko'rish
            >>> """)
    if services == "1":
        return uzbek_balance_display()

    elif services == "2":
        return uzbek_balance_check()

def check_balance(money):
    m = money * 1.01
    if user_info["card_balance"] > m and data_atm["balance"] >= money:
        tasdiq = input(f"""
                        Kartadan yechiladigan summa {m}
                            1. Davom etish
                            2. Bekor qilish
                                >>> """)
        if tasdiq == "1":
            user_info["card_balance"] -= m
            data_atm["balance"] -= money
            print("Amaliyot muvaffaqiyatli yakunlandi")
            return uzbek_services()

        elif tasdiq == "2":
            print("Xizmat bekor qilindi")
            return uzbek_services()

        else:
            print("Error")
            return uzbek_service_money()

    else:
        print("Xatolik!!!")
        return main()

def uzbek_service_money():
    money = input("""
        Summani tanlang:
            1. 50.000
            2. 100.000
            3. 200.000
            4. 300.000
            5. 400.000
            6. Boshqa summa
            0. Orqaga
                >>> """)

    if money == "1":
        return check_balance(50000)

    elif money == "2":
        return check_balance(100000)

    elif money == "3":
        return check_balance(300000)

    elif money == "4":
        return check_balance(400000)

    elif money == "6":
        money = input("""Summani kiriting: """)
        return check_balance(int(money))

    elif money == "0":
        return uzbek_services()

    else:
        print("Error")
        return uzbek_service_money

def uz_sms_on():
    if user_info["status"] == False:
        phone_number = input("""
            Telefon raqamingizni kiriting: 
                +998 _ >>> """)

        if len(phone_number) == 9:
            user_info["phone_number"] = phone_number
            user_info["status"] = True
            print("Successful")
            return uzbek_services()

        else:
            print('Xatolik')
            return uz_sms_on()

    else:
        print("Bu raqamga allaqachon sms xabarnoma ulangan")
        return uzbek_services()

def uz_sms_off():
    if user_info["status"] == True:
        print("Successfull")
        user_info["status"] = False
        user_info["phone_number"] = ""
        return uzbek_services()

    else:
        print("Bu raqamga allaqachon sms xabarnoma ulanmagan")
        return uzbek_services()

def uzbek_service_sms():
    print("SMS")
    print(f"""
        Status: {user_info["status"]}
        Phone Number {user_info["phone_number"]}
        """)
    service = input("""
        1. SMS Xabarnomani ulash
        2. SMS Xabarnomani o'chirish
            >>> """)

    if service == "1":
        return uz_sms_on()

    elif service == "2":
        return uz_sms_off()

def uzbek_service_add_money():
    print("ADD")
    money = input("Summani kiriting: ")

    if money.isdigit():
        user_info["card_balance"] += int(money)
        data_atm["balance"] += int(money)
        print("Successfull")
        return uzbek_services()

    else:
        print("Error")
        return uzbek_service_money()

def pin_code():
    print(f"Kartangizni codi => ", user_info['card_password'])
    pincode = input("Kartaga yangi cod kiriting: ")
    user_info['card_password'] = pincode
    print(f"Kartangizni yangi codi => ", user_info['card_password'])
    man = input("""
        Amaliyot muvaffaqiyatli bajarildi \n
            Hurmatli mijoz boshqa xizmatlardan foydalanasizmi?
            1. Ha
            2. Yoq
        >>>>>> """)
    if man == '1':
        return uzbek_services()
    elif man == '2':
         print('amaliyot muvaffaqiyatli bajarildi')
    else:
        print('xatolik iltimos qaytadan urining!')
        return pin_code()


def uzbek_services_pin():
    mus = input("""
        kartangiz pin kodesini o'zgartirmoqchimisiz?
            1.Ha
            2.Yo'q
            >>>>>>  """)

    if mus == '1':
        return pin_code()

    elif mus == '2':
        return uzbek_services()
    else:
        print("xatolik iltimos qaytadan urining !")
        return uzbek_services_pin()


def uzbek_services():
    print("Service Page")
    services = input("""
        Xizmat turini tanglang:
            1. Balanceni ko'rish
            2. Naqt pul yechish
            3. SMS Xabarnoma
            4. Kartani to'ldirish
            5. Pin kodeni o'zgartirish'
            0. Back
                >>> """)

    if services == "1":
        return uzbek_service_balance()

    elif services == "2":
        return uzbek_service_money()

    elif services == "3":
        return uzbek_service_sms()

    elif services == "4":
        return uzbek_service_add_money()

    elif services == "5":
        return uzbek_services_pin()

    elif services == "0":
        print("Bizni tanlaganiz uchun tashakkur!")
        return main()

    else:
        print("Bunday xizmat turi mavjud emas")
        return uzbek_services()

def uzbek():
    print("<<<<<<<<<<<<<<Uzbek Lenguage>>>>>>>>>>>>>>>>")
    password = input("Pin codeni kiriting: ")
    n = 2
    while user_info["card_password"] != password and n != 0:
        print("Error")
        password = int(input("Pin codeni kiriting: "))
        n -= 1

    if user_info["card_password"] == password:
        return uzbek_services()

    print("Sizning Kartangiz bloklandi")
    return main()

#>>>>>>>>>>>>>>>>>>>>>>> english rengual >>>>>>>>>>>>>>>>>>

def english_balance_display():
    a = input(f"""
    your balance {user_info["card_balance"]} sum
    Do you want to use other service?
        1. Yes
        2. No
            >>> """)

    if a == "1":
        return english_services()

    elif a == "2":
        return main()

    else:
        print("Error")
        return english_balance_display()
def english_balance_chek():
    print("Thank you for choosing us!")
    check = f"""
                CHECK
        Balance: {user_info["card_balance"]}
        Card: {12 * "*" + user_info["card_number"][-4::]}
        Time: {datetime.now()}
    """
    print(check)
    return main()
def english_check_balance(money):
    m = money * 1.01
    if user_info["card_balance"] > m and data_atm["balance"] >= money:
        confirmation = input(f"""
                       amount debited from the card {m}
                            1. Continue
                            2. cancellation
                                >>> """)
        if confirmation == "1":
            user_info["card_balance"] -= m
            data_atm["balance"] -= money
            print("The operation was successfully completed")
            return english_services()

        elif confirmation == "2":
            print("service canceled")
            return english_services()

        else:
            print("Error")
            return english_service_money()

    else:
        print("Error!!!")
        return main()

def english_service_balance():
    print("<<<<<<<<<Balance>>>>>>>>")
    services = input("""
        1. View on screen
        2. See on check
            >>> """)
    if services == "1":
        return english_balance_display()

    elif services == "2":
        return english_balance_chek()

def english_service_money():
    money = input("""
        Select an amount:
            1. 50.000
            2. 100.000
            3. 200.000
            4. 300.000
            5. 400.000
            6. ather amount
            0. Orqaga
                >>> """)

    if money == "1":
        return english_check_balance(50000)

    elif money == "2":
        return english_check_balance(100000)

    elif money == "3":
        return english_check_balance(300000)

    elif money == "4":
        return english_check_balance(400000)

    elif money == "6":
        money = input("""Enter the amount: """)
        return english_check_balance(int(money))

    elif money == "0":
        return english_services()

    else:
        print("Error")
        return english_service_money

def eng_sms_on():
    if user_info["status"] == False:
        phone_number = input("""
            enter your phone number: 
                +998 _ >>> """)
        if len(phone_number) == 9:
            user_info["phone_number"] = phone_number
            user_info["status"] = True
            print("Successful")
            return english_services()
        else:
            print('Xatolik')
            return eng_sms_on()
    else:
        print("SMS notification is already connected to this number")
        return english_services()
def eng_sms_off():
    if user_info["status"] == True:
        print("Successfull")
        user_info["status"] = False
        user_info["phone_number"] = ""
        return english_services()

    else:
        print("no sms notification is connected to this number")
        return english_services()

def english_service_sms():
    print("SMS")
    print(f"""
        Status: {user_info["status"]}
        Phone Number {user_info["phone_number"]}
        """)
    service = input("""
        1. Connect sms notification
        2. Delete sms notification
            >>> """)
    if service == "1":
        return eng_sms_on()

    elif service == "2":
        return eng_sms_off()

def english_service_add_money():
    print("ADD")
    money = input("enter the amount: ")
    if money.isdigit():
        user_info["card_balance"] += int(money)
        data_atm["balance"] += int(money)
        print("Successfull")
        return english_services()
    else:
        print("Error")
        return english_service_money()


def english_services():
    print("Service Page")
    services = input("""
        select the type of service:
            1. View balance
            2. cash withdrawal
            3. sms notification
            4. fill out the card
            5. edit pin code
            0. Back
                >>> """)

    if services == "1":
        return english_service_balance()

    elif services == "2":
        return english_service_money()

    elif services == "3":
        return english_service_sms()

    elif services == "4":
        return english_service_add_money()

    elif services == "5":
        return eng_services_pin()


    elif services == "0":
        print("Thank you for choosing us!")
        return main()

    else:
        print("This type of service does not exist")
        return english_services()

def eng_pin_code():
    print(f"your card code => ", user_info['card_password'])
    pincode = input("your new card code: ")
    user_info['card_password'] = pincode
    print(f"your new card code => ", user_info['card_password'])
    man = input("""
        Operation was completed successfully \n
            dear customer, do you use other services?
            1. yes
            2. no
        >>>>>> """)
    if man == '1':
        return english_services()
    elif man == '2':
         print('Operation was completed successfully')
    else:
        print('error!')
        return eng_pin_code()


def eng_services_pin():
    mus = input("""
        do you want to change your card pin code?
            1. yes
            2. no
            >>>>>>  """)

    if mus == '1':
        return eng_pin_code()

    elif mus == '2':
        return english_services()
    else:
        print("ERROR!")
        return eng_services_pin()


def english():
    print(">>>>>>>>>>>>English Lenguage>>>>>>>>>>>>>>>>")
    password = int(input("enter pin code: "))
    n = 2
    while user_info["card_password"] != password and n != 0:
        print("Error")
        password = int(input("enter pin code: "))
        n -= 1

    if user_info["card_password"] == password:
        return english_services()
    print("you card has been blocked")
    return main()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>Russian language>>>>>>>>>>>>>>>>>>>>>>>>>>>

def rus_balanc_display():
    a = input(f"""
    ваш баланс {user_info["card_balance"]} сум
    хочешь ли ты воспользоваться другими услугами??
        1. да
        2. нет
            >>> """)

    if a == "1":
        return rus_services()

    elif a == "2":
        return main()

    else:
        print("Error")
        return rus_balance_display()


def rus_balance_check():
    print("Спасибо, что выбрали нас")
    check = f"""
                CHECK
        баланс: {user_info["card_balance"]}
        карта: {12 * "*" + user_info["card_number"][-4::]}
        время: {datetime.now()}
    """
    print(check)
    return main()

def rus_service_balance():
    print("<<<<<<<<<Balance>>>>>>>>")
    services = input("""
        1. просмотреть на экране
        2. смотри на чеке
            >>> """)
    if services == "1":
        return rus_balanc_display()

    elif services == "2":
        return rus_balance_check()


def rus_check_balance(money):
    m = money * 1.01
    if user_info["card_balance"] > m and data_atm["balance"] >= money:
        tasdiq = input(f"""
                        сумма списанная с карты {m}
                            1. продолжать
                            2. отмена
                                >>> """)
        if tasdiq == "1":
            user_info["card_balance"] -= m
            data_atm["balance"] -= money
            print("операция успешно завершена")
            return rus_services()

        elif tasdiq == "2":
            print("отмена услуги")
            return rus_services()

        else:
            print("Error")
            return rus_service_money()

    else:
        print("Error!!!")
        return main()

def rus_service_money():
    money = input("""
        выберите сумму:
            1. 50.000
            2. 100.000
            3. 200.000
            4. 300.000
            5. 400.000
            6. другая сумма
            0. назад
                >>> """)

    if money == "1":
        return rus_check_balance(50000)

    elif money == "2":
        return rus_check_balance(100000)

    elif money == "3":
        return rus_check_balance(300000)

    elif money == "4":
        return rus_check_balance(400000)

    elif money == "6":
        money = input("""введите сумму: """)
        return rus_check_balance(int(money))

    elif money == "0":
        return rus_services()

    else:
        print("Error")
        return rus_service_money

def rus_sms_on():
    if user_info["status"] == False:
        phone_number = input("""
            введите свой номер телефона: 
                +998 _ >>> """)
        if len(phone_number) == 9:
            user_info["phone_number"] = phone_number
            user_info["status"] = True
            print("Successful")
            return rus_services()
        else:
            print('error')
            return rus_sms_on()
    else:
        print("СМС-уведомление уже подключено к этому номеру")
        return rus_services()

def rus_sms_off():
    if user_info["status"] == True:
        print("Successfull")
        user_info["status"] = False
        user_info["phone_number"] = ""
        return rus_services()

    else:
        print("на этот номер не подключено смс-уведомление")
        return rus_services()

def rus_service_sms():
    print("SMS")
    print(f"""
        Status: {user_info["status"]}
        Phone Number {user_info["phone_number"]}
        """)
    service = input("""
        1. подключить смс уведомление
        2. удалить смс-уведомление
            >>> """)
    if service == "1":
        return rus_sms_on()

    elif service == "2":
        return rus_sms_off()

def rus_service_add_money():
    print("ADD")
    money = input("введите сумму: ")
    if money.isdigit():
        user_info["card_balance"] += int(money)
        data_atm["balance"] += int(money)
        print("Successfull")
        return rus_services()
    else:
        print("Error")
        return rus_service_money()


def rus_pin_code():
    print(f"код вашей карты => ", user_info['card_password'])
    pincode = input("введите новый код на карте: ")
    user_info['card_password'] = pincode
    print(f"код вашей новой карты => ", user_info['card_password'])
    man = input("""
        операция завершилась успешно \n
            дорогой клиент, пользуешься ли ты другими услугами??
            1. да
            2. Нет
        >>>>>> """)
    if man == '1':
        return rus_services()
    elif man == '2':
         print('операция завершилась успешно')
    else:
        print('ERROR!')
        return rus_pin_code()


def rus_services_pin():
    mus = input("""
        вы хотите изменить пин-код своей карты?
            1. Да
            2. Нет
            >>>>>>  """)

    if mus == '1':
        return rus_pin_code()

    elif mus == '2':
        return rus_services()
    else:
        print("xatolik iltimos qaytadan urining !")
        return rus_services_pin()

def rus_services():
    print("Service Page")
    services = input("""
        выберите тип услуги:
            1. просмотреть баланс
            2. выдача наличных
            3. смс-уведомление
            4. заполнить карту
            5. изменить пин-код
            0. Back
                >>> """)

    if services == "1":
        return rus_service_balance()

    elif services == "2":
        return rus_service_money()

    elif services == "3":
        return rus_service_sms()

    elif services == "4":
        return rus_service_add_money()

    elif services == "5":
        return rus_services_pin()

    elif services == "0":
        print("Спасибо, что выбрали нас!")
        return main()

    else:
        print("такого типа услуг не существует")
        return rus_services()

def rus():
    print("<<<<<<<russian Lenguage>>>>>>>")
    password = int(input("введите пин-код: "))
    n = 2
    while user_info["card_password"] != password and n != 0:
        print("Error")
        password = int(input("введите пин-код: "))
        n -= 1

    if user_info["card_password"] == password:
        return rus_services()

    print("Ваша карта заблокирована")
    return main()
def main():
    lenguage = input("""
        Tilni tanglang:
            1. Uzbek
            2. English
            3. Russian
                >>> """)

    if lenguage == "1":
        return uzbek()

    elif lenguage == "2":
        return english()

    elif lenguage == "3":
        return (rus())

    else:
        print("Bunday til mavjud emas")
        return main()

if __name__ == "__main__":
    main()
