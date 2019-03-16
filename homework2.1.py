name = str(input("Как вас зовут? "))
gender = str(input("М|Ж? "))
age = float(input("Сколько вам лет? "))
height = float(input("Какой у вас рост (см)? "))
weight = float(input("Какой у вас вес (кг)? "))

print("Вычисляем BMI")

bmi = round(((weight / height ** 2) * 10000), 2)
print("Ваш BMI: ", bmi)

if gender == "м" or "m":
    finish = "ый"
else:
    finish = "ая"
print("Уважаем" + "{} ".format(finish) + name + ". " + "Ваш возраст: " + str(age) + ". " + "Ваш рост: " \
      + str(height) + ". " + "Ваш вес: " + str(weight) + ". " + "Ваш BMI: " + str(bmi) + ".")
print("Классификация: ", end="")
if bmi <= 16:
    print("Выраженный дефицит массы тела.")
    print("Рекомендуется повышение веса, лечение анорексии.")
elif 16 < bmi <= 18.5:
    print("Недостаточная масса тела.")
    print("Рекомендуется повышение веса.")
elif 18.5 < bmi <= 25:
    print("Нормальная масса тела.")
    print("Похудение не требуется.")
elif 25 < bmi <= 30:
    print("Избыточная масса тела (предожирение).")
    print("Рекомендуется похудение.")
elif 30 < bmi <= 35:
    print("ожирение 1-ой степени.")
    print("Рекомендуется снижение массы тела.")
elif 35 < bmi <= 40:
    print("Ожирение 2-ой степени.")
    print("Настоятельно рекомендуется снижение массы тела.")
elif bmi > 40:
    print("Ожирение 3-ой степени.")
    print("Необходимо немедленное снижение массы тела.")

print("График BMI")
finish = int(bmi - 11)
characters = int(79 - bmi)
print("10" + "#" * finish + str(bmi) + "*" * characters + "80")
