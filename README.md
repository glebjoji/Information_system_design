# Тема:"Распределение учебной нагрузки"
Описание предметной области

Вы работаете в высшем учебном заведении и занимаетесь распределением нагрузки между преподавателями кафедры. В вашем распоряжении имеются сведения о преподавателях кафедры, включающие наряду с анкетными данными информацию об их ученой степени, занимаемой административной должности и стаже работы. Преподаватели вашей кафедры должны обеспечить проведение занятий по некоторым предметам. По каждому из них установлено определенное количество часов. В результате распределения нагрузки у вас должна получиться информация следующего рода: «Такой-то преподаватель проводит занятия по такому-то предмету с такой-то группой».

### Задание ЛР1.

1. Выбрать тему, построить ER модель предметной области - 3-4 таблицы в 3НФ.


   <img width="1248" height="439" alt="image" src="https://github.com/user-attachments/assets/5a1e7251-a70c-40c8-8ab7-46bdc4693af5" />


2. Выбрать независимую сущность с наибольшим числом полей (клиент, организация, студент, пользователь и тд) - дальше ЛР1 - ЛР4 работа только с этой сущностью.


    ### Student
   

3. Построить полный класс этой сущности. Обеспечить инкапсуляцию ВСЕХ полей.

```
import phonenumbers

class Student:
    def __init__(self, student_id, last_name, first_name, middle_name, address, phone_string):
        self._student_id = student_id
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name
        self._address = address
        self._phone = phone_string # пока просто строка, валидация будет в следующем пункте
#геттер
    @property
    def student_id(self):
        return self._student_id

#геттер
    @property
    def last_name(self):
        return self._last_name

#сеттер
    @last_name.setter
    def last_name(self, value):
        self._last_name = value

#геттер
    @property
    def first_name(self):
        return self._first_name

#сеттер
    @first_name.setter
    def first_name(self, value):
        self._first_name = value

#геттер
    @property
    def middle_name(self):
        return self._middle_name

#сеттер
    @middle_name.setter
    def middle_name(self, value):
        self._middle_name = value

#геттер
    @property
    def address(self):
        return self._address

#сеттер
    @address.setter
    def address(self, value):
        self._address = value
        
#Геттер для номера телефона. Возвращает форматированный номер.
    @property
    def phone(self):
        """Геттер для номера телефона. Возвращает форматированный номер."""
        return phonenumbers.format_number(self._phone, phonenumbers.PhoneNumberFormat.E164)

#Сеттер для номера телефона с валидацией.
    @phone.setter
    def phone(self, value):
        self._phone = Student._validate_phone(value)
```

        
4. Сделать методы класса (статические) валидации всех необходимых полей. Сделать так, чтобы существование объекта с неразрешёнными полями было невозможно.

```
class Student:
    @staticmethod
    def _validate_id(student_id):
        if not isinstance(student_id, int) or student_id <= 0:
            raise ValueError("ID студента должен быть положительным целым числом.")

    @staticmethod
    def _validate_name(name, field_name):
        if not isinstance(name, str) or not name.isalpha() or not name.istitle():
            raise ValueError(f"{field_name} должен быть непустой строкой, состоящей только из букв, и начинаться с заглавной буквы.")

    @staticmethod
    def _validate_address(address):
        if not isinstance(address, str) or not address.strip():
            raise ValueError("Адрес должен быть непустой строкой.")

    @staticmethod
    def _validate_phone(phone_string):
        try:
            parsed_phone = phonenumbers.parse(phone_string, "RU")

            # is_valid_number_for_region проверяет корректность номера и его длину для России.

            if not phonenumbers.is_valid_number_for_region(parsed_phone, "RU"):
                raise ValueError("Некорректный номер телефона для Российского региона.")
            return parsed_phone
        except phonenumbers.NumberParseException:
            raise ValueError("Ошибка при разборе номера телефона. Проверьте формат.")
```

5. Убрать повтор кода из пункта 4.

6. Обеспечить перегрузку конcтруктора для нетривиальных примеров (строка, JSON и тд).

7. Обеспечить вывод на экран полной версии объекта и краткой версии объекта. Обеспечить сравнение объектов на равенство.

8. Создать класс, содержащий краткую версию данных исходного класса (например Фамилия Инициалы, только один контакт, ИНН ОГРН без адреса, без контактных лиц и тд).

9. Собрать два класса в одну иерархию наследования, обеспечить ОТСУТСТВИЕ повтора кода.

10. Нарисовать полную диаграмму классов. - БЕЗ диаграммы классов работа не принимается.
   
