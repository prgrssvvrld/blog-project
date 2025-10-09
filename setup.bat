@echo off
echo Установка зависимостей и запуск миграций...

REM Клонирование проекта (если нужно)
echo Проверка наличия проекта...
if not exist manage.py (
    echo Проект не найден. Клонируем из репозитория...
    git clone https://github.com/prgrssvvrld/blog-project.git .
) else (
    echo Проект уже существует
)

REM Проверяем наличие req.txt
if not exist req.txt (
    echo Ошибка: Файл req.txt не найден!
    echo Убедитесь, что вы находитесь в корневой папке проекта
    pause
    exit /b 1
)

REM Остальной код без изменений...
if not exist venv (
    echo Создание виртуального окружения...
    python -m venv venv
) else (
    echo Виртуальное окружение уже существует
)

echo Установка зависимостей...
call venv\Scripts\activate
pip install -r req.txt

echo Применение миграций...
python manage.py migrate

echo Запуск тестов...
python manage.py test

if %ERRORLEVEL% EQU 0 (
    echo Все тесты прошли успешно!
) else (
    echo Некоторые тесты не прошли!
)

echo Готово!
pause