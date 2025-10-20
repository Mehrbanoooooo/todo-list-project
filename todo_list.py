
# -*- coding: utf-8 -*-
import csv
import sys
sys.stdout.reconfigure(encoding='utf-8')


class Task:
    def __init__(self, title, priority="Medium"):
        self.title = title
        self.priority = priority

    def __str__(self):
        return f"Title: {self.title} | Priority: {self.priority}"


class ToDoList:
    def __init__(self, filename="tasks.csv"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, priority="Medium"):
        task = Task(title, priority)
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Do '{title}' With priority  '{priority}' Added. ")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"🗑️ Do '{title}' Deleted.")
                return
        print("⚠️ No work Do this title was found.")

    def view_tasks(self):
        if not self.tasks:
            print("📭 There are no tasks on the list.")
        else:
            print("\n📋 To-do list:")
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
            # If the file doesn't exist, we don't load anything.
            pass


def main():
    todo = ToDoList()

    while True:
        print("\n--- To-do list management menu ---")
        print("1. Add new task")
        print("2. Delete Do")
        print("3. View task list")
        print("4. Exit")

        choice = input("Please enter the option number: ")

        if choice == "1":
            title = input("Do Title: ")
            priority = input("Priority (High/Medium/Low): ")
            todo.add_task(title, priority)
        elif choice == "2":
            title = input("Do title you want to delete: ")
            todo.remove_task(title)
        elif choice == "3":
            todo.view_tasks()
        elif choice == "4":
            print("👋 Goodbye! List saved.")
            break
        else:
            print("❌ Invalid option, try again.")


if __name__ == "__main__":
    main()
