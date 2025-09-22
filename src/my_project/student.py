import phonenumbers
from .student_summary import StudentSummary

class Student(StudentSummary):
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
            if not phonenumbers.is_valid_number_for_region(parsed_phone, "RU"):
                raise ValueError("Некорректный номер телефона для российского региона.")
            return parsed_phone
        except phonenumbers.NumberParseException:
            raise ValueError("Ошибка при разборе номера телефона. Проверьте формат.")

    def __init__(self, student_id, last_name, first_name, middle_name, address, phone_string):
        self._validate_id(student_id)
        self._validate_name(last_name, "Фамилия")
        self._validate_name(first_name, "Имя")
        self._validate_name(middle_name, "Отчество")
        self._validate_address(address)
        
        super().__init__(last_name, first_name, middle_name)
        
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

    def __repr__(self):
        return (f"Student(student_id={self._student_id}, last_name='{self.last_name}', "
                f"first_name='{self.first_name}', middle_name='{self.middle_name}', "
                f"address='{self._address}', phone='{self.phone}')")

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._student_id == other._student_id and self._phone == other._phone

    @classmethod
    def from_string(cls, data_string):
        parts = data_string.split(',')
        if len(parts) != 6:
            raise ValueError("Неверный формат строки. Ожидается 6 полей.")
        student_id, last_name, first_name, middle_name, address, phone_string = parts
        return cls(int(student_id.strip()), last_name.strip(), first_name.strip(), middle_name.strip(), address.strip(), phone_string.strip())

    @classmethod
    def from_json(cls, json_data):
        if not isinstance(json_data, dict):
            raise TypeError("Ожидается словарь JSON.")
        return cls(
            json_data.get('student_id'),
            json_data.get('last_name'),
            json_data.get('first_name'),
            json_data.get('middle_name'),
            json_data.get('address'),
            json_data.get('phone')
        )