# 📈 IPO Time-to-Return Analysis (NSE)

## Why this project exists

IPO investments are often driven by hype, but there is very little structured analysis on a simple question:

**How long does it actually take for an IPO to generate meaningful returns?**

This project answers that using raw market data from the National Stock Exchange (NSE).


---

## What this project does

This project builds a complete data pipeline to:

* Track IPO-listed stocks after listing
* Measure how many days they take to reach return milestones
* Identify how many IPOs never reach those returns

It focuses on **time-to-return**, not just returns.

---

## Key Question

> How many days does it take for IPO stocks to reach 10%–100% returns from their issue price?

---

## Data Sources

### 1. NSE Daily Bhavcopy Data

Raw daily trading data downloaded from NSE archives (2020–2024)

* SYMBOL
* OPEN, HIGH, LOW, CLOSE prices
* Volume and trade data

👉 No third-party APIs used

Link: https://archives.nseindia.com/products/content/sec_bhavdata_full_29122023.csv
Just change the date at the end of the URL. Make sure it is not a holiday.

Use this file and the sheets in it. Refreshing the script in Excel would yield results based on the added dates.
/data/NSE Stock Data 2024 - Github.xlsx

---

### 2. IPO Dataset

Extracted from NSE IPO portal:

* Company Name
* Symbol
* Issue Price
* Date of Listing
* Price Band

Link: https://www.nseindia.com/market-data/all-upcoming-issues-ipo

---

## Project Pipeline

### Step 1: Company Universe Extraction

* Scraped all NSE-listed company symbols
* Stored in `Company Codes.xlsx`

Link: https://money.rediff.com/companies/nseall/

Or use /scripts/0.NSE_Company code.py

---

### Step 2: Trading Day URL Generation

* Generated valid NSE bhavcopy URLs
* Excluded holidays (non-trading days)

---

### Step 3: Data Download

* Downloaded daily CSV files for 2020–2024
* Structured into yearly Excel datasets

---

### Step 4: Data Consolidation & Optimization

* Merged multiple Excel files
* Converted into a single dataset
* Stored as `.pkl` file for faster processing

```id="dataflow"
nse_2020_21_22_23_24.pkl
```

---

### Step 5: IPO Data Integration

* Mapped IPO dataset with market data using `SYMBOL`
* Filtered data from listing date onwards

---

### Step 6: Time-to-Return Calculation

For each IPO:

* Track daily prices after listing
* Use **intraday HIGH price** to detect return achievement
* Calculate number of days to reach:

| Return Level | Definition        |
| ------------ | ----------------- |
| 10%          | 1.1 × Issue Price |
| 50%          | 1.5 × Issue Price |
| 100%         | 2.0 × Issue Price |

---

## Output

Final dataset contains:

* IPO details
* Listing performance
* Highest & lowest price lifecycle
* Days to reach return milestones (10% → 100%)

Each row = **1 IPO**

---

## Key Design Choices

### 1. Issue Price as Baseline

Used to measure returns relative to IPO valuation

> Note: Listing price may better reflect market entry and can be explored in future iterations

---

### 2. HIGH Price (not Close Price)

Used to detect the **first opportunity** to achieve returns

> This captures peak potential but may overstate sustained performance

---

## Sample Insights (Illustrative)

* Not all IPOs reach 50% returns
* Many IPOs achieve peak returns early (first few weeks)
* A subset never recovers after listing

---

## Tech Stack

* Python
* Pandas
* Excel
* Requests

---

## Project Structure

```id="structure"
ipo-time-to-return-nse/
│
├── data/
│   ├── NSE_IPO_Extract.xlsx
│
├── input/
│   ├── Company Codes.xlsx
│
├── output/
│   ├── output.xlsx
│
├── scripts/
│   ├── 0. NSE_Company codes.py
│   ├── 1. Read Stock data to pickle.py
│   ├── 2. Days to reach certain percent.py
│
└── README.md
```

---

## What I learned

* Building a multi-year financial dataset from raw exchange data
* Handling large-scale time-series efficiently
* Designing metrics that translate data into decision-making
* Understanding trade-offs in financial analysis (issue vs listing price, high vs close price)

---

## Limitations

* Uses intraday highs (may overstate returns)
* Does not account for holding period or exit feasibility
* Based on issue price, not listing price

---

## Future Scope

* Compare issue price vs listing price returns
* Sector-wise IPO performance
* Risk-adjusted return metrics
* Interactive dashboard for IPO analytics

---

## Disclaimer

This project is for analytical and educational purposes only and should not be considered financial advice.
