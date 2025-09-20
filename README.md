# Тема: "Распределение учебной нагрузки"
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
    def _validate_last_name(last_name):
        if not isinstance(last_name, str) or not last_name.isalpha() or not last_name.istitle():
            raise ValueError("Фамилия должна быть непустой строкой, состоящей только из букв, и начинаться с заглавной буквы.")

    @staticmethod
    def _validate_first_name(first_name):
        if not isinstance(first_name, str) or not first_name.isalpha() or not first_name.istitle():
            raise ValueError("Имя должно быть непустой строкой, состоящей только из букв, и начинаться с заглавной буквы.")

    @staticmethod
    def _validate_middle_name(middle_name):
        if not isinstance(middle_name, str) or not middle_name.isalpha() or not middle_name.istitle():
            raise ValueError("Отчество должно быть непустой строкой, состоящей только из букв, и начинаться с заглавной буквы.")

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

6. Обеспечить перегрузку конcтруктора для нетривиальных примеров (строка, JSON и тд).
```
@classmethod
    def from_string(cls, data_string):
        parts = data_string.split(',')
        if len(parts) != 6:
            raise ValueError("Неверный формат строки. Ожидается 6 полей.")
        
        student_id, last_name, first_name, middle_name, address, phone_string = parts
        
        # Вызываем основной конструктор, передавая преобразованные данные
        return cls(int(student_id), last_name, first_name, middle_name, address, phone_string)

    @classmethod
    def from_json(cls, json_data):
        if not isinstance(json_data, dict):
            raise TypeError("Ожидается словарь JSON.")
            
        # Получаем данные из словаря и вызываем основной конструктор
        return cls(
            json_data.get('student_id'),
            json_data.get('last_name'),
            json_data.get('first_name'),
            json_data.get('middle_name'),
            json_data.get('address'),
            json_data.get('phone')
        )
```

7. Обеспечить вывод на экран полной версии объекта и краткой версии объекта. Обеспечить сравнение объектов на равенство.

```
def __repr__(self):
        return (f"Student(student_id={self._student_id}, last_name='{self.last_name}', "
                f"first_name='{self.first_name}', middle_name='{self.middle_name}', "
                f"address='{self._address}', phone='{self.phone}')")

    def __str__(self):
        initials = f"{self.first_name[0]}.{self.middle_name[0]}."
        return f"{self.last_name} {initials}"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._student_id == other._student_id and self._phone == other._phone
```

8. Создать класс, содержащий краткую версию данных исходного класса (например Фамилия Инициалы, только один контакт, ИНН ОГРН без адреса, без контактных лиц и тд).

```
# Часть: Краткая версия данных
class StudentSummary:
    def __init__(self, last_name, first_name, middle_name):
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def first_name(self):
        return self._first_name

    @property
    def middle_name(self):
        return self._middle_name
    
    def get_initials(self):
        """Возвращает инициалы ФИО."""
        return f"{self._first_name[0]}.{self._middle_name[0]}."

# Целое: Полная версия данных, содержащая краткую
class Student:
    def __init__(self, student_id, last_name, first_name, middle_name, address, phone_string):
        # Композиция: Создаем объект StudentSummary внутри Student
        self._summary = StudentSummary(last_name, first_name, middle_name)
        
        self._student_id = student_id
        self._address = address
        self._phone = phonenumbers.parse(phone_string, "RU")

    @property
    def last_name(self):
        return self._summary.last_name
    
    @property
    def first_name(self):
        return self._summary.first_name
        
    def __str__(self):
        """Краткая версия через композицию."""
        return f"{self._summary.last_name} {self._summary.get_initials()}"
```
9. Собрать два класса в одну иерархию наследования, обеспечить ОТСУТСТВИЕ повтора кода.
```
# 1. Родительский класс
class StudentSummary:
    def __init__(self, last_name, first_name, middle_name):
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def first_name(self):
        return self._first_name

    @property
    def middle_name(self):
        return self._middle_name
    
    def __str__(self):
        initials = f"{self._first_name[0]}.{self._middle_name[0]}."
        return f"{self._last_name} {initials}"

# 2. Дочерний класс
class Student(StudentSummary):
    @staticmethod
    def _validate_phone(phone_string):
        try:
            parsed_phone = phonenumbers.parse(phone_string, "RU")
            if not phonenumbers.is_valid_number_for_region(parsed_phone, "RU"):
                raise ValueError("Некорректный номер телефона для российского региона.")
            return parsed_phone
        except phonenumbers.NumberParseException:
            raise ValueError("Ошибка при разборе номера телефона. Проверьте формат.")

    def __init__(self, student_id, last_name, first_name, middle_name, address, phone_string):
        # Вызов конструктора родительского класса с помощью super()
        super().__init__(last_name, first_name, middle_name)
        
        # Инициализация дополнительных полей с валидацией
        self._student_id = student_id
        self._address = address
        self._phone = self._validate_phone(phone_string)

    @property
    def student_id(self):
        return self._student_id
    
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    
    @property
    def phone(self):
        return phonenumbers.format_number(self._phone, phonenumbers.PhoneNumberFormat.E164)

```
10. Нарисовать полную диаграмму классов. - БЕЗ диаграммы классов работа не принимается.
   ![Untitled diagram _ Mermaid Chart-2025-09-20-190934](https://github.com/user-attachments/assets/5b344fa2-bf2d-464b-a0a4-3eaf27ed490f)
<svg id="export-svg" width="100%" xmlns="http://www.w3.org/2000/svg" class="classDiagram" style="max-width: 398.9624938964844px;" viewBox="0 0 398.9624938964844 630" role="graphics-document document" aria-roledescription="class">
