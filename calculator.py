print("Калькулятор")

while True:

    def calc():
    
        try:

            print(eval(input()))
        
        except Exception as e:
            print("Ошибка!")

    calc()
    
