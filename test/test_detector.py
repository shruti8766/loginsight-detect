import sys
import os

# Ensure backend/src is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend', 'src')))

from database import DatabaseManager
from detector import AnomalyDetector

def test_detector():
    db_manager = DatabaseManager()
    
    if db_manager.connection and db_manager.connection.is_connected():
        db_manager.cursor.execute("DELETE FROM anomaly")
        db_manager.connection.commit()
        print("Cleared old anomalies from the database before testing.")
    else:
        print("Database connection failed.")
        return

    detector = AnomalyDetector(db_manager)
    test_records = [
        {'machine_id': 'M1', 'timstamp': '03-07-2025 09:00', 'units_produced': 80, 'temperature': 60.0, 'error_flag': 0},
        {'machine_id': 'M2', 'timstamp': '03-07-2025 09:05', 'units_produced': 40, 'temperature': 70.0, 'error_flag': 0},
        {'machine_id': 'M3', 'timstamp': '03-07-2025 09:10', 'units_produced': 90, 'temperature': 85.0, 'error_flag': 0},
        {'machine_id': 'M4', 'timstamp': '03-07-2025 09:15', 'units_produced': 100, 'temperature': 65.0, 'error_flag': 1},
        {'machine_id': 'M5', 'timstamp': '03-07-2025 09:20', 'units_produced': 30, 'temperature': 90.0, 'error_flag': 1},
    ]

    total_anomalies = 0
    try:
        for record in test_records:
            anomalies = detector.detect_anomalies(record)
            print(f"Input: {record}")
            if anomalies:
                print("Detected anomalies:")
                for anomaly in anomalies:
                    print(anomaly)
                total_anomalies += len(anomalies)
            else:
                print("No anomalies detected.")
            print("-" * 40)

        print(f"Total anomalies detected in test: {total_anomalies}")
    finally:
        db_manager.close()

if __name__ == "__main__":
    test_detector()
