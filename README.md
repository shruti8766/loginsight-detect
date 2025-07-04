## LogInsight Detect
-- LogInsight Detect is a robust Python application designed to deliver actionable insights by detecting anomalies in manufacturing machine logs. Leveraging advanced data analysis and seamless database integration, it empowers organizations to maintain operational excellence and minimize downtime.

---

## Project Overview

LogInsight Detect streamlines the identification of critical production anomalies—such as low output, high temperature, and error flags—directly from manufacturing logs.
Key features include:

-- Automated, rule-based anomaly detection for rapid, reliable insights

--Persistent MySQL database storage for all detected events

--Intuitive command-line interface (CLI) for detection, search, export, and maintenance

--Seamless integration with real-world manufacturing data pipelines

--Modular, extensible architecture ready for enterprise deployment

---

## Technologies Used
--Python 3.x — Core application logic

--pandas — High-performance data processing

--MySQL — Scalable, reliable database backend

--mysql-connector-python — Secure database connectivity

---


## Quick Start
1] Clone the repository:
        git clone https://github.com/shruti8766/loginsight-detect.git
        cd loginsight-detect

2] Install dependencies:
        pip install -r requirements.txt

3] Configure the MySQL database:
  --Create a database named project in your MySQL server. 
        CREATE DATABASE project;

  --Update credentials in src/database.py as needed for your environment.
        self.connection = mysql.connector.connect(
        host="localhost",
        database="project",
        user="youruser",        # <-- replace with your MySQL username
        password="yourpassword" # <-- replace with your MySQL password
        )
4] Place your manufacturing log CSV files in the data/ directory.


---


## Usage
1] Launch the interactive CLI:
        python -m src.cli
    -View, search, export, or clear anomalies
    -Run anomaly detection on new log files

2] Run batch anomaly detection:
        python -m src.main

3]Execute automated tests:
        python -m test.test_detector


---

## Project Structure
PythonProject1/
├── data/
│ ├── manufacturing.py          # Data generation 
│ └── manufacturing_logs.csv    # Sample input data
├── src/
│ ├── cli.py                    # Command-line interface logic
│ ├── database.py               # Database connection and management
│ ├── detector.py               # Anomaly detection engine
│ └── main.py                   # Batch detection runner
├── test/
│ └── test_detector.py          # Automated test suite
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
└── LICENSE                     # Project license (MIT)


---

## Testing & Quality Assurance
-All detection logic is validated with sample scenarios in test/test_detector.py.
-To ensure reliability, run:
        python -m test.test_detector


---

## Why LogInsight Detect?
--Enterprise-ready: Designed for scalability and integration with existing manufacturing systems.

--Actionable analytics: Delivers immediate, meaningful insights to reduce downtime and improve productivity.

--Extensible: Built with modularity in mind—customize detection rules or integrate with dashboards and alerting systems.


---


## License
This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.
---


## About the Author
Data-driven Python developer with a passion for building resilient, production-grade analytics tools for industry. Experienced in end-to-end solutions from data ingestion to actionable reporting.

For business inquiries or collaboration opportunities, please contact: shrutigaikwad8766@gmail.com
