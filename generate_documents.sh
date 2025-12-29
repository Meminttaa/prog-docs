#!/bin/bash
set -e

echo "▶ Чтение данных из PostgreSQL"
python3 parse_from_postgres.py

echo "▶ Генерация документов"
python3 process_docx_per_student.py

echo "✅ ГОТОВО"
