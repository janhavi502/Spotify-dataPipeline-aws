# Spotify-DataPipeline-aws
## End-to-End Data Engineering Pipeline: Spotify + AWS

### 📖 Overview
This project builds a scalable data engineering pipeline using Spotify API & AWS Cloud. It extracts music streaming data, processes it, stores structured data in a warehouse, and visualizes insights via dashboards.<br>

### 🚀 Tech Stack
AWS Services: S3, Lambda, Glue, Redshift, Athena, QuickSight<br>
Programming: Python (ETL scripts)<br>
Database: Amazon Redshift / PostgreSQL<br>
Visualization: AWS QuickSight / Tableau<br>
API Used: Spotify API<br>

### 🛠️ Features<br>
✔️ Automated Data Ingestion from Spotify API<br>
✔️ Cloud Storage & Processing with AWS S3 & Glue<br>
✔️ Data Warehousing using Redshift / RDS<br>
✔️ Dashboard & Insights for user analytics<br>

### 📂 Project Structure<br>

spotify-data-pipeline/
├── data_ingestion/          # Extracts data from Spotify API<br>
├── data_processing/         # Cleans & transforms raw data<br>
├── database/                # SQL scripts for data warehousing<br>
├── visualization/           # AWS QuickSight / Tableau dashboards<br>
├── README.md                # Project documentation<br>
├── requirements.txt         # Python dependencies<br>
├── .gitignore               # Ignore sensitive files<br>
└── LICENSE                  # Open-source license<br>

### 📈 Data Flow<br>
1️⃣ Extract → Fetch data from Spotify API<br>
2️⃣ Store → Save raw data in AWS S3<br>
3️⃣ Transform → Clean & process using AWS Glue<Br>
4️⃣ Load → Store in Redshift / RDS<Br>
5️⃣ Visualize → Create dashboards in AWS QuickSight<Br>

### 📊 Results & Insights<br>
Top Artists & Songs based on user streaming behavior<br>
Listening Patterns across different timeframes<br>
Genre Popularity Trends<Br>

### 📜 License<br>
This project is open-source under the MIT License.<br>

### Dataset Link<br>
https://www.kaggle.com/datasets/tonygordonjr/spotify-dataset-2023
