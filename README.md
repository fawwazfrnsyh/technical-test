# Technical Test
Technical Test Avows Technologies (Placement Mandiri Sekuritas) <br>
Mohammad Fawwaz Ferriansyah <br>
fawwaz.ferriansyah@gmail.com

---

# TASK 1
Import the CRM events and CRM call center logs tables into a PostgreSQL database. Use SQL to join the tables and summarize the average time to resolve complaints across a number of different dimensions.

## Prerequisites

- Docker desktop installed on your system
- Docker images for PostgreSQL install on Docker Desktop
- CSV file CRM events and call center logs data
- SQL Client (DBeaver, etc)

## Setup Instructions

### 1. PostgreSQL Database Setup

Start a PostgreSQL Docker container with the following configuration:

```bash
docker run --name consolidatedash -e POSTGRES_USER=cons_dash -e POSTGRES_PASSWORD=consdash2023 -p 5432:5432 -d postgres
```

### 2. Database Schema Creation

Connect to your PostgreSQL instance and create the required schema and tables:

```sql
-- Create schema
CREATE SCHEMA IF NOT EXISTS crm;

-- Create CRM events table
CREATE TABLE crm.events(
    Date_received DATE,
    Product VARCHAR(200),
    Sub_product VARCHAR(200),
    Issue VARCHAR(200),
    Sub_issue VARCHAR(200),
    Consumer_complaint_narrative VARCHAR(5000),
    Tags VARCHAR(200),
    Consumer_consent_provided VARCHAR(200),
    Submitted_via VARCHAR(200),
    Date_sent_to_company DATE,
    Company_response_to_consumer VARCHAR(200),
    Timely_response VARCHAR(200),
    Consumer_disputed VARCHAR(200),
    Complaint_ID VARCHAR(200),
    Client_ID VARCHAR(200)
);

-- Create call center logs table
CREATE TABLE crm.call_center_logs(
    Date_received DATE,
    Complaint_ID VARCHAR(200),
    rand_client VARCHAR(200),
    phonefinal VARCHAR(200),
    vru_line VARCHAR(200),
    call_id VARCHAR(200),
    priority VARCHAR(200),
    type VARCHAR(200),
    outcome VARCHAR(200),
    server VARCHAR(200),
    ser_start VARCHAR(200),
    ser_exit VARCHAR(200),
    ser_time TIME
);
```

## Data Import Process

1. **Prepare your data files**: Ensure CRM events and call center logs are in CSV format
2. **Import data**: Use DBaver features to import CSV file to table. Ensure that the column names in the file match those in the table.
3. **Validate data**: Run basic counts and checks to ensure data integrity
4. **Execute analysis**: Run the provided queries to generate insights

## Analysis Queries

### 1. Average Resolution Time by Product

Analyzes resolution times for different product categories (Banking, Credit Card):

```sql
SELECT 
    e.product, 
    AVG(ccl.ser_time) 
FROM crm.events e
JOIN crm.call_center_logs ccl ON e.complaint_id = ccl.complaint_id 
WHERE e.complaint_id IS NOT NULL
GROUP BY e.product 
ORDER BY e.product;
```

### 2. Average Resolution Time by Issue Type
Breaks down resolution times by issue categories:

```sql
SELECT 
    e.issue, 
    AVG(ccl.ser_time) 
FROM crm.events e
JOIN crm.call_center_logs ccl ON e.complaint_id = ccl.complaint_id 
WHERE e.complaint_id IS NOT NULL
GROUP BY e.issue 
ORDER BY e.issue;
```

### 3. Average Resolution Time by Month

Shows trends in complaint resolution:

```sql
SELECT 
    TO_CHAR(e.date_received, 'YYYY-MM') as month, 
    AVG(ccl.ser_time) 
FROM crm.events e
JOIN crm.call_center_logs ccl ON e.complaint_id = ccl.complaint_id 
WHERE e.complaint_id IS NOT NULL
GROUP BY TO_CHAR(e.date_received, 'YYYY-MM')
ORDER BY month;
```

------

# Task 2
Import the Luxury Loan Portfolio into pandas dataframes and use Plotly dash to create a web app that displays 3 charts of different types that show interesting business metrics.

## Loan Luxury Portfolio Dash

This dashboard was created using Plotly Dash to analyze loan portfolio data.
Visualizations include:
- Bar chart: Total funded amount per purpose.
- Line chart: Monthly transaction trend.
- Pie chart: Distribution of borrower positions.

---

## Prerequisite
Make sure you have:
- Python 3.9 or later
- `pip` (Python package manager)
- CSV data file: `LuxuryLoanPortfolio.csv` (place it according to the path in the script or change the `file` variable)

Python libraries:
- `dash`
- `plotly`
- `pandas`
- `numpy`
---

## How to run
1. **Install library**
```
pip install [__library_name_]
```

2. **Run the application**
```
python luxury_loan_portfolio.py
```

3. **Open a browser** and access:
```
http://127.0.0.1:8050/
```

---

## Dashboard Preview

---

# TASK 3
---

# TASK 4
How would you create a data platform end-to-end system? the data might have internal data or external data, but the end data would be stored into cloud platforms like Google Cloud Platform or Azure Platform or AWS Platform. Please give details step by step, including data preparation, model evaluation, etc.

### 1. Data Preparation
#### Internal Data Sources
- **Company Systems**: Export data from existing enterprise systems
  - Application logs
  - ERP (Enterprise Resource Planning) systems
  - CRM (Customer Relationship Management) systems

#### External Data Sources
- **APIs**: Collect data from external service APIs
- **Public Datasets**: Ingest publicly available data sources

#### Data Format Conversion
Convert incoming data to Hadoop-compatible formats:
- **Parquet** (recommended for analytics)
- **CSV** (for simple tabular data)
- **ORC** (Optimized Row Columnar)

#### Data Ingestion Methods
- **Stream Processing**: Real-time data ingestion
  - Apache Kafka for message queuing
  - Apache Flink for stream processing
- **Batch Processing**: Scheduled data loads
  - Apache NiFi for data flow management

### 2. Data Processing
#### Data Cleansing
- Remove null values and handle missing data
- Standardize data formats across sources
- Identify and fix duplicate records

#### Data Transformation
- **Column Derivation**: Create new calculated fields
- **Reference Table Joins**: Enrich data with lookup tables
- **Data Aggregation**: Summarize data for reporting needs

#### Data Modeling
- **Star Schema**: Implement dimensional modeling approach
  - Fact tables for measurable events
  - Dimension tables for descriptive attributes

#### Processing Tools
- **Apache Hive**: SQL-like queries on Hadoop data
- **Apache Spark**: Distributed data processing engine

### 3. Cloud Process
#### Hadoop to S3 Migration
- **AWS DataSync Agent**: Deploy in on-premises environment
- **Configuration**:
  - Source: HDFS (Hadoop Distributed File System)
  - Destination: Amazon S3 bucket
  - Optional scheduling for automated transfers

#### Metadata Management
- **AWS Glue Crawler**:
  - Points to S3 landing path
  - Extracts metadata from data files
  - Populates AWS Data Catalog automatically

#### ETL Processing
- **Data Cleansing & Transformation**: Prepare data for warehouse loading
- **AWS Glue Jobs**:
  - Read from Data Catalog (S3 source)
  - Optional staging tables for intermediate processing
  - Transform data according to business rules

#### Data Warehousing
- **Staging Area**: Optional intermediate storage for data validation
- **Data Mart**: Load processed data into OLAP tables
- **Amazon Redshift**: Target data warehouse
- **Stored Procedures**: Automated data loading processes

---

# TASK 5

Write a few short paragraphs of no more than 500 words on how you see the future of fintech developing when it comes to investment banking. Feel free to express your opinions and be creative, there is no single correct answer.
### The Future of Fintech in Indonesian Investment Banking
#### Investing Made Easier
In the past, only the wealthy and large corporations could invest in stocks or bonds. Now, emerging fintech apps like Bibit, Ajaib, Pluang, etc., enable ordinary people to invest with small capital. We can buy stocks simply through a smartphone, even with as little as 100,000 rupiah.

#### E-commerce Becomes a Bank
E-commerce platforms are not just places to shop but will also become places where we manage our finances—from loans for small businesses to investments. For example, e-commerce platforms like Shopee and Tokopedia have already begun expanding into the fintech sector, offering cash loans, paylater features, collaborating with banks to issue credit cards, and even allowing users to buy gold. There is a possibility that in the coming years, we will be able to conduct investment transactions using these e-commerce platforms.
