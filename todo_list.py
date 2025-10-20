
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

import csv

class Task:
    def __init__(self, title, priority="متوسط"):
        self.title = title
        self.priority = priority

    def __str__(self):
        return f"عنوان: {self.title} | اولویت: {self.priority}"


class ToDoList:
    def __init__(self, filename="tasks.csv"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, priority="متوسط"):
        task = Task(title, priority)
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ کار '{title}' با اولویت '{priority}' اضافه شد.")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"🗑️ کار '{title}' حذف شد.")
                return
        print("⚠️ کاری با این عنوان پیدا نشد.")

    def view_tasks(self):
        if not self.tasks:
            print("📭 هیچ کاری در لیست وجود ندارد.")
        else:
            print("\n📋 لیست کارها:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def save_tasks(self):
        with open(self.filename, mode="w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Priority"])
            for task in self.tasks:
                writer.writerow([task.title, task.priority])

    def load_tasks(self):
        try:
            with open(self.filename, mode="r", encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    title = row["Title"]
                    priority = row["Priority"]
                    self.tasks.append(Task(title, priority))
        except FileNotFoundError:
            # اگر فایل وجود نداشت، چیزی لود نمی‌کنیم
            pass


def main():
    todo = ToDoList()

    while True:
        print("\n--- منوی مدیریت لیست کارها ---")
        print("1. اضافه کردن کار جدید")
        print("2. حذف کار")
        print("3. مشاهده لیست کارها")
        print("4. خروج")

        choice = input("لطفاً شماره گزینه را وارد کنید: ")

        if choice == "1":
            title = input("عنوان کار: ")
            priority = input("اولویت (بالا/متوسط/پایین): ")
            todo.add_task(title, priority)
        elif choice == "2":
            title = input("عنوان کاری که می‌خواهید حذف کنید: ")
            todo.remove_task(title)
        elif choice == "3":
            todo.view_tasks()
        elif choice == "4":
            print("👋 خداحافظ! لیست ذخیره شد.")
            break
        else:
            print("❌ گزینه نامعتبر است، دوباره تلاش کنید.")


if __name__ == "__main__":
    main()
