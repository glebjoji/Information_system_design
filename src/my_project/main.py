from .student import Student
import json

if __name__ == "__main__":
    try:
        student1 = Student(1, "Иванов", "Иван", "Иванович", "г. Москва, ул. Ленина, д. 10", "+79123456789")
        print(f"Объект создан: {student1}")
        print(f"Полное представление: {repr(student1)}")
        
        # Исправленная строка без запятых в адресе
        student_from_str = Student.from_string("2,Петров,Петр,Петрович,г. Санкт-Петербург ул. Невская д. 5,+79876543210")
        print(f"Объект из строки: {student_from_str}")

        json_data = '{"student_id": 3, "last_name": "Сидоров", "first_name": "Сергей", "middle_name": "Алексеевич", "address": "г. Казань, ул. Пушкина, д. 3", "phone": "+79501234567"}'
        json_dict = json.loads(json_data)
        student_from_json = Student.from_json(json_dict)
        print(f"Объект из JSON: {student_from_json}")

        student_equal = Student(1, "Иванов", "Иван", "Иванович", "г. Москва, ул. Ленина, д. 10", "+79123456789")
        print(f"Сравнение объектов (student1 == student_equal): {student1 == student_equal}")

    except ValueError as e:
        print(f"Ошибка при создании объекта: {e}")