# E-commerce Marketing Data Aggregator

Python project that aggregates e-commerce order data and email marketing campaign data into a simple business performance report.

## Features

- Loads order data from CSV
- Loads email campaign data from CSV
- Calculates total revenue and total orders
- Finds the top-selling product
- Calculates email open rate and click rate
- Exports a summary report to a text file

## Tech Stack

- Python
- Pandas
- CSV data processing
- Business reporting

## Project Structure

```text
ecommerce-marketing-data-aggregator/
├── data/
│   ├── orders.csv
│   └── email_campaigns.csv
├── output/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```


## Input Data
### orders.csv

Expected columns:
- order_id 
- order_date 
- customer_name 
- product_name 
- quantity 
- total_amount 
- status

### email_campaigns.csv

Expected columns:
- campaign_date 
- campaign_name 
- emails_sent 
- opens 
- clicks 
- unsubscribed

## Installation
```text
pip install -r requirements.txt
```

## Example Output
====== E-commerce and Marketing Summary Report ======

### Orders summary

--------------
- Total orders: 535
- Total revenue: 5 527 871 Ft
- Total items sold: 540
- Top product: Python Alapok - Összegző Munkafüzet
- Average order value: 10 332 Ft

### Email campaign summary

----------------------
- Campaigns sent: 79
- Emails sent: 221928
- Total opens: 60973
- Total clicks: 3144
- Total unsubscribed: 1178

### Calculated metrics

------------------
- Open rate: 27.47%
- Click rate: 1.42%
- Sales performance / click: 17.02%
- Average clicks per order: 5.88%

### Best campaign

-------------
- 1. Sales Email - Python Start 2025.06.11 - VIP
- Open rate: 91.51%
- Click rate: 57.55%
- Emails sent: 106

### Top performing campaigns by open rate

-------------------------------------

- 1. Sales Email - Python Start 2025.06.11 - VIP -> 91.51% open rate
- Copy of Már 83 VIP előjelentkező + Video -> 82.80% open rate
- VIP értesítés 2025-06-05 -> 78.30% open rate
- 2. Sales Email - Python Start 2025.06.13 - VIP -> 73.74% open rate
- Python Start Videovisszajelzés kérése - 2025.12.01. -> 72.92% open rate

### Top performing campaigns by click rate

--------------------------------------

- 1. Sales Email - Python Start 2025.06.11 - VIP -> 57.55% click rate

- 7. Sales Email - Python Start 2025.06.25 - VIP -> 23.60% click rate
- Copy of Már 83 VIP előjelentkező + Video -> 21.51% click rate
- XMAS-2025-12-24 kampány - PYTHON START- REGGEL - Email #1 -> 16.82% click rate
- 4. Sales Email - Python Start 2025.06.18 - VIP -> 16.49% click rate




## Use Case 

This project demonstrates how Python can combine e-commerce and marketing data into a simple business summary report.

It is useful for:
- e-commerce reporting 
- marketing performance tracking 
- business data aggregation 
- automation portfolio projects
