import pandas as pd
from src.database import DatabaseManager
from src.detector import AnomalyDetector

def run_anomaly_detection(csv_file_path):
    try:
        df = pd.read_csv(csv_file_path)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return

    db_manager = DatabaseManager()
    if db_manager.connection and db_manager.connection.is_connected():
        try:
            db_manager.cursor.execute("DELETE FROM anomaly")
            db_manager.connection.commit()
            print("Cleared old anomalies from the database.")

            detector = AnomalyDetector(db_manager)

            for _, row in df.iterrows():
                record = row.to_dict()
                anomalies = detector.detect_anomalies(record)
                for anomaly in anomalies:
                    db_manager.insert_anomaly(
                        anomaly['machine_id'],
                        anomaly['timstamp'],
                        anomaly['anomaly_type'],
                        anomaly['value'],
                        anomaly['description']
                    )

            print("\nAll anomalies in database:")
            all_anomalies = db_manager.fetch_all_anomalies()
            for anomaly in all_anomalies:
                print(anomaly)
            print(f"\nTotal anomalies detected: {len(all_anomalies)}")

        except Exception as e:
            print(f"Error during anomaly detection: {e}")
        finally:
            db_manager.close()
    else:
        print("Database connection failed.")

if __name__ == "__main__":
    csv_file_path = "C:/Users/shrut/PycharmProjects/pythonProject1/data/manufacturing_logs.csv"
    run_anomaly_detection(csv_file_path)


