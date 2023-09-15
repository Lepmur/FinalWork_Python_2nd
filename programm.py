import json
import os
import datetime

# Путь к файлу для хранения заметок в формате JSON
NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            notes = json.load(file)
        return notes
    else:
        return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note(title, body):
    notes = load_notes()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": len(notes) + 1, "title": title, "body": body, "created_at": now, "updated_at": now}
    notes.append(note)
    save_notes(notes)
    print("Заметка добавлена успешно!")

def edit_note(note_id, title, body):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["body"] = body
            note["updated_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка отредактирована успешно!")
            return
    print("Заметка с указанным ID не найдена.")

def delete_note(note_id):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка удалена успешно!")
            return
    print("Заметка с указанным ID не найдена.")

def list_notes():
    notes = load_notes()
    if not notes:
        print("Список заметок пуст.")
    else:
        for note in notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата создания: {note['created_at']}")

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Список заметок")
        print("5. Выйти")
        choice = input("Введите номер действия: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            add_note(title, body)
        elif choice == "2":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            edit_note(note_id, title, body)
        elif choice == "3":
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(note_id)
        elif choice == "4":
            list_notes()
        elif choice == "5":
            break
        else:
            print("Неправильный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
