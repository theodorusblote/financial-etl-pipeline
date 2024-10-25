# ETL Pipeline for Financial Data

This project implements an automated ETL (Extract, Transform, Load) pipeline for extracting stock data using `yfinance`, transforms the data by adding technical indicators such as moving averages, RSI, etc., and loads the data into a PostgreSQL database. The pipeline can be set up to run daily for continually updated data.

## Table of Contents

- [Features](#features)
- [Installation and setup](#installation-and-setup)
- [Project structure](#project-structure)
- [Scheduling the pipeline](#scheduling-the-pipeline)
- [License](#license)

## Features

- **Data extraction:** Retrieves historical stock data using `yfinance`
- **Feature engineering:** Enhances the data with technical indicators such as:
  - 50-Day SMA
  - 200-Day SMA
  - RSI
  - Lagged features for Open Price, Volume, and Daily Return
- **Data loading:** Stores transformed data into a PostgreSQL database for further analysis
- **Automation:** Configurable to run automatically at a specified time daily using cron jobs

## Installation and setup

1. **Clone the repository:**
```bash
git clone https://github.com/theodorusblote/financial-etl-pipeline.git
cd financial-etl-pipeline
```
2. **Create and activate virtual environment:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. **Install required packages:**
```bash
pip install -r requirements.txt
```
4. **Set up environment variables:** Create a .env file in the project root and add your database credentials
```env
DB_USERNAME=your_db_username
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
DB_NAME=your_db_name
```
5. **Run script manually:**
```bash
python financial_etl_pipeline.py
```

## Project structure

```plaintext
financial-etl-pipeline/
│
├── financial_etl_pipeline.py  # Main ETL pipeline script
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (should be excluded from version control)
├── .gitignore                 # Git ignore file
├── LICENSE                    # MIT License
└── README.md                  # Project documentation
```

## Scheduling the piepline

To automate the ETL pipeline to run daily at a specified time, you can set up a cron job (macOS).

1. **Open crontab editor:**
```bash
crontab -e
```
2. **Add cron job:** Replace path/to/your/project with the actual path to your project directory
```cron
0 23 * * * /path/to/your/project/.venv/bin/python /path/to/your/project/financial_etl_pipeline.py
```

Explanation:
- `0 23 * * *`: Runs the job every day at 23:00 (11 pm).

## License

This project is licensed under the [MIT License](LICENSE).
