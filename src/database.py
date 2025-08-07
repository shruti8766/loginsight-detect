import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self._connect()
        if self.connection and self.connection.is_connected():
            self._create_anomaly_table()
        print("Database Manager initialized!")

    def _connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                database="project",
                user="root",
                password="123456"
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("Successfully connected to MySQL!!")
            else:
                print("Failed to establish connection between MySQL and Python!")
                self.connection = None
        except mysql.connector.Error as err:
            print(f"Error connecting to MySQL: {err}")
            self.connection = None
            self.cursor = None

    def _create_anomaly_table(self):
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS anomaly (
            machine_id VARCHAR(50) NOT NULL,
            timstamp VARCHAR(100) NOT NULL,
            anomaly_type VARCHAR(100) NOT NULL,
            value VARCHAR(255),
            description TEXT,
            PRIMARY KEY (machine_id, timstamp, anomaly_type) 
        )
        """
        try:
            self.cursor.execute(create_table_sql)
            self.connection.commit()
            print("Anomaly table checked/created successfully.")
        except mysql.connector.Error as err:
            print(f"Error creating anomaly table: {err}")

    def insert_anomaly(self, machine, timstamp, anomaly_type, values, description):
        if not self.connection or not self.connection.is_connected():
            print("Database not connected for insert. Attempting to reconnect...")
            self._connect()
            if not self.connection or not self.connection.is_connected():
                print("Failed to reconnect, cannot insert anomaly.")
                return False

        insert_sql = """
        INSERT INTO anomaly (machine_id, timstamp, anomaly_type, value, description)
        VALUES (%s, %s, %s, %s, %s)
        """
        try:
            self.cursor.execute(insert_sql, (machine, timstamp, anomaly_type, str(values), description))
            self.connection.commit()
            print(f"Anomaly inserted: {anomaly_type} for {machine} at {timstamp}")
            return True
        except mysql.connector.Error as err:
            print(f"Error inserting anomaly: {err}")
            self.connection.rollback()
            return False

    def fetch_all_anomalies(self):
        if not self.connection or not self.connection.is_connected():
            print("Database not connected for fetching. Attempting to reconnect...")
            self._connect()
            if not self.connection or not self.connection.is_connected():
                print("Failed to reconnect, cannot fetch anomalies.")
                return []

        try:
            self.cursor.execute("SELECT machine_id, timstamp, anomaly_type, value, description FROM anomaly ORDER BY timstamp ASC")
            results = self.cursor.fetchall()
            print(f"Fetched {len(results)} anomalies from the database.")
            return results
        except mysql.connector.Error as err:
            print(f"Error fetching anomalies: {err}")
            return []

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed.")
