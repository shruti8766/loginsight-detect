import pandas as pd
from detector import AnomalyDetector
from database import DatabaseManager

def run_anomaly_detection(csv_file_path):
    db_manager = DatabaseManager()
    if db_manager.connection:
        detector = AnomalyDetector(db_manager)

        try:
            df = pd.read_csv(csv_file_path)

            # Optional: Inspect for debugging
            print("CSV Columns:", df.columns)
            print(df.head())

            all_anomalies = []

            for _, row in df.iterrows():
                record = {
                    'machine_id': row.get('machine_id'),
                    'timstamp': row.get('timstamp'),
                    'units_produced': row.get('units_produced'),
                    'temperature': row.get('temperature'),
                    'error_flag': row.get('error_flag')
                }
                anomalies = detector.detect_anomalies(record)
                for anomaly in anomalies:
                    print(anomaly)
                    db_manager.insert_anomaly(
                        anomaly["machine_id"],
                        anomaly["timstamp"],
                        anomaly["anomaly_type"],
                        anomaly["value"],
                        anomaly["description"]
                    )
                all_anomalies.extend(anomalies)

            print(f"\nTotal anomalies detected: {len(all_anomalies)}")

        except Exception as e:
            print(f"Error during anomaly detection: {e}")
        finally:
            db_manager.close()
    else:
        print("Database connection failed.")

if __name__ == "__main__":
    csv_file_path = 'manufacturing_logs.csv'
    run_anomaly_detection(csv_file_path)


