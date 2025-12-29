import os
import json
from docx_generator import create_docx_for_student


def safe_name(text):
    return text.replace(" ", "_").replace("/", "_")


with open("all_students_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

students = data["students"]

output_dir = "output_docs"
os.makedirs(output_dir, exist_ok=True)

for student in students:
    fio = student.get("ФИО_обучающегося", "Без_ФИО")
    fio_dir_name = safe_name(fio)

    student_dir = os.path.join(output_dir, fio_dir_name)
    os.makedirs(student_dir, exist_ok=True)

    create_docx_for_student(
        "Аттестационный лист производственная.docx",
        os.path.join(student_dir, f"Аттестационный_лист_пп_{fio_dir_name}.docx"),
        student
    )

    create_docx_for_student(
        "Аттестационный лист учебная.docx",
        os.path.join(student_dir, f"Аттестационный_лист_уп_{fio_dir_name}.docx"),
        student
    )

    create_docx_for_student(
        "Отчёт производственная.docx",
        os.path.join(student_dir, f"Отчёт_пп_{fio_dir_name}.docx"),
        student
    )

    create_docx_for_student(
        "Отчёт учебная.docx",
        os.path.join(student_dir, f"Отчёт_уп_{fio_dir_name}.docx"),
        student
    )

