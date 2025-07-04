import pandas as pd
from src.database import DatabaseManager
from src.main import run_anomaly_detection

def show_menu():
    print("\n==== Anomaly Detector CLI ====")
    print("1. View all anomalies")
    print("2. Search anomalies by machine")
    print("3. Export anomalies to CSV")
    print("4. Clear all anomalies")
    print("5. Run anomaly detection on a new file")
    print("0. Exit")

def main():
    db = DatabaseManager()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            anomalies = db.fetch_all_anomalies()
            for i in anomalies:
                print(i)
        elif choice == "2":
            machine = input("Enter machine ID: ").strip()
            db.cursor.execute("SELECT * FROM anomaly WHERE machine_id=%s", (machine,))
            for i in db.cursor.fetchall():
                print(i)
        elif choice == "3":
            anomalies = db.fetch_all_anomalies()
            df = pd.DataFrame(anomalies, columns=["machine_id", "timstamp", "anomaly_type", "value", "description"])
            df.to_csv("anomalies_export.csv", index=False)
            print("Exported to anomalies_export.csv")
        elif choice == "4":
            db.cursor.execute("DELETE FROM anomaly")
            db.connection.commit()
            print("All anomalies cleared.")
        elif choice == "5":
            file_path = input("Enter path to new CSV log file: ").strip()
            run_anomaly_detection(file_path)
        elif choice == "0":
            db.close()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

