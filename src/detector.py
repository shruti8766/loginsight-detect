from src.database import DatabaseManager

class AnomalyDetector:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def detect_anomalies(self, record):
        machine_id = record.get('machine_id')
        timstamp = record.get('timstamp')
        units_produced = record.get('units_produced')
        temperature = record.get('temperature')
        error_flag = record.get('error_flag')
        anomalies_found = []

        if not timstamp:
            print(f"Warning: Record missing 'timstamp': {record}")
            return anomalies_found

        if units_produced is not None and units_produced < 50:
            anomalies_found.append({
                "machine_id": machine_id,
                "timstamp": timstamp,
                "anomaly_type": "low_production",
                "value": units_produced,
                "description": f"Units produced ({units_produced}) below threshold (50)."
            })

        if temperature is not None and temperature > 75:
            anomalies_found.append({
                "machine_id": machine_id,
                "timstamp": timstamp,
                "anomaly_type": "high_temperature",
                "value": temperature,
                "description": f"Temperature ({temperature}) above 75 degrees."
            })

        if error_flag == 1:
            anomalies_found.append({
                "machine_id": machine_id,
                "timstamp": timstamp,
                "anomaly_type": "error_flag_raised",
                "value": error_flag,
                "description": "Error flag raised."
            })

        return anomalies_found
