# Python-in-21-Days

![Python](https://img.shields.io/badge/Python-21%20Days-3776AB?logo=python&logoColor=white)
![Focus](https://img.shields.io/badge/Focus-Data%20%26%20AI-0A66C2)
![Level](https://img.shields.io/badge/Level-Beginner%20to%20Interview%20Ready-2E8B57)
![Format](https://img.shields.io/badge/Format-Daily%20Practice%20%7C%20Projects%20%7C%20Interview%20Prep-8A2BE2)

## Python for Data & AI: 21-Day Accelerated Blueprint

A practical 21-day Python roadmap built for one hour a day. The goal is to move from fundamentals into real-world scripting, data handling, automation, and interview readiness for Data Science, Data Engineering, and AI Automation.

**Daily format: 20 min theory + 20 min interactive code + 20 min real-world exercise = 1 hour per day**

This repository is organized into three modules:

- **Module 1:** Core Python Engine
- **Module 2:** Advanced Manipulation & Scripting Architecture
- **Module 3:** Specialization & Interview Readiness

## Table of Contents

- [Why this roadmap](#why-this-roadmap)
- [How to use this repository](#how-to-use-this-repository)
- [Learning path](#learning-path)
- [Repository structure](#repository-structure)
- [Daily workflow](#daily-workflow)
- [Expected outcome](#expected-outcome)
- [Next steps](#next-steps)

## Why this roadmap

This blueprint is designed for consistency, not just information overload. Each day combines theory, coding practice, and a real-world exercise so every lesson produces something useful.

The roadmap is intentionally aligned with paths that matter in the real market:

- **Data Analysis:** Python, pandas, cleaning, grouping, and summaries.
- **Data Engineering:** Python fundamentals, files, SQL, ETL thinking, and pipeline logic.
- **AI Automation:** scripting, file handling, APIs, structured data, and workflow logic.

## How to use this repository

1. Read the theory for the day.
2. Type the interactive code manually.
3. Complete the real-world exercise without copying too early.
4. Save your solution inside the matching day folder.
5. Revisit old scripts and improve them as your understanding grows.

A strong rule for this challenge: **build first, optimize later**.

## Learning path

### Module 1: Core Python Engine (Days 1–7)

Focus: mastering syntax, data structures, and foundational logic required to manipulate data pipelines and trigger automations.

#### Day 1: Environment & The Anatomy of Variables
**Theory (20 min):** Setting up a professional environment using VS Code and Jupyter Notebooks. Understanding dynamic typing, memory references, and primitive data types like strings, integers, floats, and booleans.

**Interactive Code (20 min):**
```python
# Type casting and string interpolation
age = 25
hourly_rate = 45.50
is_active = True
profile_summary = f"User Age: {age} | Rate: ${hourly_rate} | Status: {is_active}"
print(profile_summary)
```

**Real-World Exercise (20 min):** Create a script that takes raw API output inputs (simulated via variables: `client_name`, `monthly_ad_spend`, `conversion_rate`) and outputs a formatted performance string calculating total conversions.

#### Day 2: Control Flow & Algorithmic Logic
**Theory (20 min):** Conditional execution, logical operators, and truthy/falsy values. Mastering conditional filtering used in data processing.

**Interactive Code (20 min):**
```python
# Conditional parsing logic
lead_score = 85
if lead_score >= 80:
    status = "High Priority - Route to Sales AI"
elif lead_score >= 50:
    status = "Medium Priority - Nurture"
else:
    status = "Low Priority"
print(status)
```

**Real-World Exercise (20 min):** Build an automated lead-scoring filter that checks a lead's budget and employee count, assigning them to `Enterprise`, `Mid-Market`, or `SMB` automation buckets.

#### Day 3: Looping Mechanisms & Iteration Control
**Theory (20 min):** `for` loops, `while` loops, and loop control statements like `break` and `continue`.

**Interactive Code (20 min):**
```python
# Iterating through data streams with early exit
server_logs = ["INFO", "INFO", "WARNING", "CRITICAL", "INFO"]
for log in server_logs:
    if log == "CRITICAL":
        print("Alert triggered! Halting pipeline.")
        break
    print(f"Processing log: {log}")
```

**Real-World Exercise (20 min):** Write a loop that iterates through a list of 10 transaction amounts. Skip any negative or fraudulent transactions using `continue`, and stop execution if a single transaction exceeds `$10,000`.

#### Day 4: Native Data Structures - Lists & Tuples
**Theory (20 min):** Array-like structures, indexing, slicing, mutability vs immutability, and list methods.

**Interactive Code (20 min):**
```python
# Slicing high-frequency data chunks
historical_metrics =[1][2][3]
recent_metrics = historical_metrics[-3:]
print(f"Recent Trend: {recent_metrics}")
```

**Real-World Exercise (20 min):** Take a list of unorganized user email strings. Clean them by removing whitespace, converting them to lowercase, and saving them into a fresh validated list.

#### Day 5: Key-Value Engines - Dictionaries & Sets
**Theory (20 min):** Working with JSON-like data using Python dictionaries. Keys, values, hashing, lookups, and sets for deduplication.

**Interactive Code (20 min):**
```python
# Simulating a payload structure
webhook_payload = {
    "event": "lead_created",
    "data": {"name": "Alex", "email": "alex@corp.com"}
}
print(webhook_payload.get("data").get("email"))
```

**Real-World Exercise (20 min):** Deduplicate a raw list of transaction IDs using a set, then construct a dictionary containing the transaction count and summary metadata.

#### Day 6: Functional Architecture & Scope
**Theory (20 min):** Writing clean, modular code using functions. Parameters, arguments, default values, return statements, and scope.

**Interactive Code (20 min):**
```python
def calculate_roi(investment: float, return_amount: float) -> float:
    net_profit = return_amount - investment
    return (net_profit / investment) * 100

print(f"Project ROI: {calculate_roi(1000, 2500)}%")
```

**Real-World Exercise (20 min):** Build a robust Python function named `clean_phone_number` that strips country codes, dashes, and spaces from a raw phone string, returning a standardized E.164 format string.

#### Day 7: Error Resilience & File I/O Foundations
**Theory (20 min):** Handling unexpected inputs using `try-except-finally`. Reading and writing text and CSV files using `with open()`.

**Interactive Code (20 min):**
```python
# Secure data handling
try:
    with open("data_stream.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    content = "Fallback: Direct API Stream Activated"
print(content)
```

**Real-World Exercise (20 min):** Attempt to open a configuration file. If the file is missing, catch the exception, write a default JSON configuration to a new file, and log a custom warning string.

### Module 2: Advanced Manipulation & Scripting Architecture (Days 8–14)

Focus: moving into intermediate concepts required to efficiently process data packages and interface with enterprise APIs.

#### Day 8: Py-Expressions (List Comprehensions & Lambdas)
**Theory (20 min):** Writing readable, high-performance, single-line data transformations.

**Interactive Code (20 min):**
```python
# Elegant batch data filtering
raw_salaries = 
high_earners = [salary for salary in raw_salaries if salary > 80000]
print(high_earners)
```

**Real-World Exercise (20 min):** Strip dollar signs from price tags, cast them to floats, and apply a 10% tax using a single list comprehension.

#### Day 9: Object-Oriented Python for Production (OOP)
**Theory (20 min):** Classes, objects, `__init__`, attributes, and methods.

**Interactive Code (20 min):**
```python
class APIConnector:
    def __init__(self, endpoint: str, token: str):
        self.endpoint = endpoint
        self.token = token
    def connect(self):
        return f"Establishing handshake with {self.endpoint} via Bearer Token."

crm_sync = APIConnector("https://api.crm.com/v1", "secret_9948")
print(crm_sync.connect())
```

**Real-World Exercise (20 min):** Model an internal data engineering pipeline with a `DataPipeline` class containing `source_path` and `row_count`, along with a `run_transform()` method.

#### Day 10: Standard Library Toolkits (`os`, `sys`, `datetime`)
**Theory (20 min):** Navigating filesystems, handling command-line arguments, and managing timestamps.

**Interactive Code (20 min):**
```python
import os
from datetime import datetime

current_folder = os.getcwd()
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print(f"Workspace: {current_folder} | Executed At: {timestamp}")
```

**Real-World Exercise (20 min):** Scan a directory, identify all `.csv` files, and rename them to append the current date to their filenames.

#### Day 11: Enterprise API Consumption (`requests` Module)
**Theory (20 min):** Integrating with HTTP endpoints, handling headers, query parameters, authorization tokens, and JSON payloads.

**Interactive Code (20 min):**
```python
import requests

response = requests.get("https://api.github.com", timeout=5)
if response.status_code == 200:
    print("GitHub Engine Online")
```

**Real-World Exercise (20 min):** Connect to a public mock API like JSONPlaceholder, fetch mock user posts, filter them for an author ID, and export the matching data to a text log.

#### Day 12: RegEx & String Parsing Masterclass
**Theory (20 min):** Using `re` to extract precise information from unstructured text streams.

**Interactive Code (20 min):**
```python
import re

log_text = "ERROR 2026-07-08: Database connection timeout from IP 192.168.1.50"
ip_address = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log_text)
print(f"Extracted Threat Source: {ip_address.group()}")
```

**Real-World Exercise (20 min):** Build a text validation function that scans any string input and returns a boolean confirming if it contains a valid email address pattern.

#### Day 13: The Numeric Engine - NumPy
**Theory (20 min):** Vectorized operations vs loops, arrays, slicing, and basic statistical modeling.

**Interactive Code (20 min):**
```python
import numpy as np

sensor_readings = np.array([22.1, 24.5, 21.9, 30.2, 23.4])
normalized_readings = sensor_readings - np.mean(sensor_readings)
print(f"Deviations: {normalized_readings}")
```

**Real-World Exercise (20 min):** Generate an array of 50 random floating-point values representing stock valuations. Use NumPy to locate the median price, standard deviation, and filter out all elements below the mean.

#### Day 14: Structured Data Pipelines - Pandas Essentials
**Theory (20 min):** Introduction to DataFrames and Series. Reading CSV files into DataFrames, inspecting shapes, and selecting rows or columns dynamically.

**Interactive Code (20 min):**
```python
import pandas as pd

mock_market_data = {
    "Product": ["SaaS Basic", "SaaS Enterprise", "Consulting"],
    "MRR": 
}
df = pd.DataFrame(mock_market_data)
print(df[df["MRR"] > 5000])
```

**Real-World Exercise (20 min):** Generate a DataFrame with 5 user profiles (`Name`, `Department`, `Rating`). Extract the `Name` and `Rating` columns for employees in the `Engineering` department.

### Module 3: Specialization & Interview Readiness (Days 15–21)

Focus: connecting Python directly to target data pathways and mastering high-yield technical interview patterns.

#### Day 15: Deep-Dive Pandas Data Wrangling
**Theory (20 min):** Data cleaning strategies: `dropna`, `fillna`, `groupby`, and merging frames like SQL joins.

**Interactive Code (20 min):**
```python
import pandas as pd

sales_data = pd.DataFrame({
    "Region": ["West", "East", "West", "North", "East"],
    "Revenue": 
})
regional_yield = sales_data.groupby("Region")["Revenue"].sum().reset_index()
print(regional_yield)
```

**Real-World Exercise (20 min):** Build a data cleaning pipeline. Take an imperfect DataFrame containing missing numerical values and mismatched text strings. Impute missing figures with column averages and convert labels to uppercase.

#### Day 16: SQL Database Engineering Connectors
**Theory (20 min):** Bridging script files and database schemas. Interfacing with databases using `sqlite3` or SQLAlchemy.

**Interactive Code (20 min):**
```python
import sqlite3
import pandas as pd

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE leads (id INT, email TEXT)")
conn.execute("INSERT INTO leads VALUES (1, 'jd@olive-growth.com')")

df = pd.read_sql_query("SELECT * FROM leads", conn)
print(df)
conn.close()
```

**Real-World Exercise (20 min):** Establish a local SQLite database instance. Build an ETL script that reads a local list, loads it into a table structure, and queries back active records.

#### Day 17: AI Integration & Automation Architecture
**Theory (20 min):** Designing intelligent automation frameworks. Communicating with large language models through APIs and parsing structured inputs from natural language.

**Interactive Code (20 min):**
```python
# Abstract blueprint of an automated AI routing agent
def trigger_ai_agent(prompt_text: str):
    mock_payload = {"prompt": prompt_text, "temperature": 0.0}
    return f"AI Classification Output for: '{prompt_text}'"

print(trigger_ai_agent("Extract all tracking codes from invoice #4402"))
```

**Real-World Exercise (20 min):** Write a script that accepts an unstructured email body, formats an optimization prompt string, and prepares a complete JSON payload ready for an AI chat completion API.

#### Day 18: Core DSA Data Structures for Interviews
**Theory (20 min):** Big-O time and space complexity, hash maps, and two-pointer approaches.

**Interactive Code (20 min):**
```python
# Classic Two-Sum Hash Map Optimization: O(n) Time
def target_lookup(nums, target):
    seen_elements = {}
    for index, val in enumerate(nums):
        complement = target - val
        if complement in seen_elements:
            return [seen_elements[complement], index]
        seen_elements[val] = index
    return []

print(target_lookup(, 9))[4][5][6][7]
```

**Real-World Exercise (20 min):** Write an optimal search function that identifies whether an input string array contains duplicate values in less than O(n^2) runtime complexity.

#### Day 19: Algorithmic Manipulation Patterns
**Theory (20 min):** Interview-heavy array and string manipulation techniques. Mastering index trackers, window slicing calculations, and multi-condition checks on numerical lists.

**Interactive Code (20 min):**
```python
# Reverse a sequence in-place using two references
def reverse_stream(data_list):
    left, right = 0, len(data_list) - 1
    while left < right:
        data_list[left], data_list[right] = data_list[right], data_list[left]
        left += 1
        right -= 1
    return data_list

print(reverse_stream())[8][9][10][11][4]
```

**Real-World Exercise (20 min):** Write an efficient sorting logic or frequency scanner that counts occurrences of characters in text records and returns the top 3 most recurring elements.

#### Day 20: Comprehensive Mock Screening Blueprint
**Theory (20 min):** Synthesizing your skills. Simulating the pressure of a real technical interview. Managing code presentation and outlining logic before writing code.

**Interactive Code (20 min):**
```python
# FizzBuzz / Data Stream Validation Pattern
def evaluate_stream(limit: int):
    results = []
    for num in range(1, limit + 1):
        if num % 3 == 0 and num % 5 == 0:
            results.append("DataAI")
        elif num % 3 == 0:
            results.append("Data")
        elif num % 5 == 0:
            results.append("AI")
        else:
            results.append(str(num))
    return results

print(evaluate_stream(15))
```

**Real-World Exercise (20 min):** Complete a 20-minute timed sprint challenge: write an automated file system audit function that processes a multi-level file path string, isolates file extensions, and aggregates counts using a dictionary tracker.

#### Day 21: Framework Consolidation & Multi-Directional Launch
**Theory (20 min):** Packaging your knowledge into production-ready skills. Decide your next specialization vector: Data Engineering, Data Science, or AI Automation.

**Action Items (40 min):**
- Set up your portfolio directory structure.
- Push all previous daily exercise files to a public GitHub repository.
- Document the repository with a strong `README.md`.

## Repository structure

```bash
python-in-21-days/
├── day_01/
├── day_02/
├── day_03/
├── day_04/
├── day_05/
├── day_06/
├── day_07/
├── day_08/
├── day_09/
├── day_10/
├── day_11/
├── day_12/
├── day_13/
├── day_14/
├── day_15/
├── day_16/
├── day_17/
├── day_18/
├── day_19/
├── day_20/
├── day_21/
└── README.md
```

## Daily workflow

- Spend 20 minutes on theory.
- Spend 20 minutes typing the example code.
- Spend 20 minutes solving the real-world exercise.
- Commit your work daily.
- Review mistakes and rewrite old code for clarity.

## Expected outcome

By the end of the 21 days, you should be able to:

- write clean Python scripts confidently,
- use core data structures effectively,
- handle files and errors safely,
- work with NumPy and Pandas,
- interact with APIs and databases,
- solve interview-style problems,
- build automation-ready mini projects.

## Next steps

After finishing the 21 days, choose one primary path and go deeper:

- **Data Analysis:** pandas, visualization, business analysis, and SQL.
- **Data Engineering:** SQL, ETL pipelines, orchestration, and scalable workflows.
- **AI Automation:** APIs, structured data, prompt workflows, and automation systems.

## License

Add your preferred license here.

## Connect

Built as part of a focused journey to become stronger in Python, automation, and data-driven systems.
