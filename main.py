from ocr import extract_text
from parser import parse_expense
from db import init_db, save_expense
from analytics import show_summary

def main():
    init_db()
    while True:
        print("\n1. Upload Receipt\n2. View Summary\n3. Exit")
        choice = input("Select option: ")

        if choice == "1":
            path = input("Enter image path (e.g., receipts/sample1.jpg): ").strip()
            try:
                text = extract_text(path)
                print("\nExtracted Text:\n", text)
                expense = parse_expense(text)
                save_expense(expense)
                print("Saved Expense:", expense)
            except Exception as e:
                print("Error processing receipt:", e)

        elif choice == "2":
            show_summary()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
