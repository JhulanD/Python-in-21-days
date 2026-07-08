# Python-in-21-Days  
## Python for Data & AI: 21-Day Accelerated Blueprint

This repository contains a **21-day, 1-hour-per-day Python curriculum** designed to take you from Python fundamentals to practical readiness for **Data Science, Data Engineering, and AI Automation** roles.

The roadmap is structured in 3 modules:
- **Module 1:** Core Python Engine
- **Module 2:** Advanced Manipulation & Scripting Architecture
- **Module 3:** Specialization & Interview Readiness

***

## Overview

This program is built for consistent daily execution. Each day includes:

- **Theory** — core concepts and explanation
- **Interactive Code** — a short coding example
- **Real-World Exercise** — a practical task aligned with data, automation, or engineering work

The goal is not just to learn syntax, but to build the ability to:
- write clean Python scripts,
- process structured and unstructured data,
- automate repetitive tasks,
- work with files, APIs, and databases,
- prepare for real-world technical interviews.

***

## Learning Structure

### Module 1: Core Python Engine (Days 1–7)
**Focus:** Mastering the syntax, data structures, and foundational logic required to manipulate data pipelines and trigger automations.

#### Day 1: Environment & The Anatomy of Variables
**Theory (20 min):**  
Setting up a professional environment (VS Code & Jupyter Notebooks). Understanding dynamic typing, memory references, and core primitive data types such as strings, integers, floats, and booleans.

**Interactive Code (20 min):**
```python
# Type casting and string interpolation
age = 25
hourly_rate = 45.50
is_active = True
profile_summary = f"User Age: {age} | Rate: ${hourly_rate} | Status: {is_active}"
print(profile_summary)
```

**Real-World Exercise (20 min):**  
Create a script that takes raw API output inputs (simulated via variables: `client_name`, `monthly_ad_spend`, `conversion_rate`) and outputs a formatted performance string calculating total conversions.

***

#### Day 2: Control Flow & Algorithmic Logic
**Theory (20 min):**  
Conditional execution (`if-elif-else`), logical operators (`and`, `or`, `not`), and truthy/falsy values. Mastering conditional filtering used in data processing.

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

**Real-World Exercise (20 min):**  
Build an automated lead-scoring filter. Write a script that checks a lead's budget and employee count, assigning them to `"Enterprise"`, `"Mid-Market"`, or `"SMB"` automation buckets.

***

#### Day 3: Looping Mechanisms & Iteration Control
**Theory (20 min):**  
`for` loops, `while` loops, and loop control statements (`break`, `continue`). Iterating over sequences to transform batches of data.

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

**Real-World Exercise (20 min):**  
Write a loop that iterates through a list of 10 transaction amounts. Skip any negative/fraudulent transactions using `continue`, and stop execution entirely if a single transaction exceeds `$10,000`.

***

#### Day 4: Native Data Structures - Lists & Tuples
**Theory (20 min):**  
Array-like structures, indexing, slicing, mutability vs. immutability. List methods (`append`, `pop`, `sort`) and their performance implications.

**Interactive Code (20 min):**
```python
# Slicing high-frequency data chunks
historical_metrics = [44, 48, 55, 62, 70, 81, 95]
recent_metrics = historical_metrics[-3:]
print(f"Recent Trend: {recent_metrics}")
```

**Real-World Exercise (20 min):**  
Take a list of unorganized user email strings. Clean them by removing whitespaces, converting them to lowercase, and saving them into a fresh, validated list structure.

***

#### Day 5: Key-Value Engines - Dictionaries & Sets
**Theory (20 min):**  
Working with JSON-like data using Python dictionaries. Keys, values, hashing, and lookups. Using sets for deduplication operations in data pipelines.

**Interactive Code (20 min):**
```python
# Simulating a payload structure
webhook_payload = {
    "event": "lead_created",
    "data": {"name": "Alex", "email": "alex@corp.com"}
}
print(webhook_payload.get("data").get("email"))
```

**Real-World Exercise (20 min):**  
You receive a raw list of duplicate transaction IDs. Deduplicate the list using a set, then construct a dictionary containing the transaction count and summary metadata.

***

#### Day 6: Functional Architecture & Scope
**Theory (20 min):**  
Writing clean, modular code using functions (`def`). Parameters, arguments, default values, return statements, and local vs. global scope.

**Interactive Code (20 min):**
```python
def calculate_roi(investment: float, return_amount: float) -> float:
    net_profit = return_amount - investment
    return (net_profit / investment) * 100

print(f"Project ROI: {calculate_roi(1000, 2500)}%")
```

**Real-World Exercise (20 min):**  
Build a robust Python function named `clean_phone_number` that strips country codes, dashes, and spaces from a raw phone string, returning a standardized E.164 format string.

***

#### Day 7: Error Resilience & File I/O Foundations
**Theory (20 min):**  
Handling unexpected inputs using `try-except-finally`. Reading and writing text/CSV files using context managers (`with open()`).

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

**Real-World Exercise (20 min):**  
Write a script that attempts to open a configuration file. If the file is missing, catch the exception, write a default JSON configuration to a new file, and log a custom warning string.

***

### Module 2: Advanced Manipulation & Scripting Architecture (Days 8–14)
**Focus:** Moving into intermediate concepts required to efficiently process data packages and interface with enterprise APIs.

#### Day 8: Py-Expressions (List Comprehensions & Lambdas)
**Theory (20 min):**  
Writing readable, high-performance, single-line data transformations. List comprehensions, dictionary comprehensions, and anonymous lambda functions.

**Interactive Code (20 min):**
```python
# Elegant batch data filtering
raw_salaries = [45000, 62000, 120000, 85000, 150000]
high_earners = [salary for salary in raw_salaries if salary > 80000]
print(high_earners)
```

**Real-World Exercise (20 min):**  
You have a list of price tags in strings (e.g., `["$120.00", "$45.50", "$9.99"]`). Use a single list comprehension to strip the dollar sign, cast them to floats, and apply a 10% tax.

***

#### Day 9: Object-Oriented Python for Production (OOP)
**Theory (20 min):**  
Classes, objects, `__init__`, attributes, and methods. Blueprinting your data connectors or automation configurations as repeatable components.

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

**Real-World Exercise (20 min):**  
Model an internal data engineering pipeline. Create a `DataPipeline` class containing attributes for `source_path` and `row_count`, along with a method called `run_transform()` that logs progress status.

***

#### Day 10: Standard Library Toolkits (`os`, `sys`, `datetime`)
**Theory (20 min):**  
Navigating filesystems, handling command-line arguments, and managing timestamps—crucial for file processing and automated scheduling jobs.

**Interactive Code (20 min):**
```python
import os
from datetime import datetime

current_folder = os.getcwd()
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print(f"Workspace: {current_folder} | Executed At: {timestamp}")
```

**Real-World Exercise (20 min):**  
Write a backup script that scans a specific directory, identifies all files ending in `.csv`, and renames them to append the current date to their filenames.

***

#### Day 11: Enterprise API Consumption (`requests` Module)
**Theory (20 min):**  
Integrating with HTTP endpoints. Sending GET and POST requests, handling headers, query parameters, authorization tokens, and decoding JSON payloads.

**Interactive Code (20 min):**
```python
import requests

# Simulating an external lookup
response = requests.get("https://api.github.com", timeout=5)
if response.status_code == 200:
    print("GitHub Engine Online")
```

**Real-World Exercise (20 min):**  
Write an automation script that connects to a public mock API like JSONPlaceholder, fetches mock user posts, filters them for an author ID, and exports the matching data to a text log.

***

#### Day 12: RegEx & String Parsing Masterclass
**Theory (20 min):**  
Using Regular Expressions (`re` module) to extract precise information from unstructured text streams such as emails, text messages, and system logs.

**Interactive Code (20 min):**
```python
import re

log_text = "ERROR 2026-07-08: Database connection timeout from IP 192.168.1.50"
ip_address = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log_text)
print(f"Extracted Threat Source: {ip_address.group()}")
```

**Real-World Exercise (20 min):**  
Build a text validation function that scans any string input and returns a boolean value confirming if it contains a valid email address pattern.

***

#### Day 13: The Numeric Engine - NumPy
**Theory (20 min):**  
Moving into the data layer. Vectorized operations vs loops. Creating NumPy arrays, slicing multidimensional blocks, and basic statistical modeling.

**Interactive Code (20 min):**
```python
import numpy as np

sensor_readings = np.array([22.1, 24.5, 21.9, 30.2, 23.4])
normalized_readings = sensor_readings - np.mean(sensor_readings)
print(f"Deviations: {normalized_readings}")
```

**Real-World Exercise (20 min):**  
Generate an array of 50 random floating-point integers representing stock valuations. Use NumPy to locate the median price, standard deviation, and filter out all elements falling below the mean.

***

#### Day 14: Structured Data Pipelines - Pandas Essentials
**Theory (20 min):**  
Introduction to DataFrames and Series. Reading Excel/CSV files into dataframes, inspecting head/tail shapes, and selecting rows or columns dynamically.

**Interactive Code (20 min):**
```python
import pandas as pd

mock_market_data = {
    "Product": ["SaaS Basic", "SaaS Enterprise", "Consulting"],
    "MRR": [4500, 12000, 7500]
}
df = pd.DataFrame(mock_market_data)
print(df[df["MRR"] > 5000])
```

**Real-World Exercise (20 min):**  
Use Pandas to programmatically generate a DataFrame consisting of 5 user profiles (`Name`, `Department`, `Rating`). Extract the `Name` and `Rating` columns for employees assigned to the `Engineering` department.

***

### Module 3: Specialization & Interview Readiness (Days 15–21)
**Focus:** Connecting Python directly to your target data pathways and mastering high-yield technical interview patterns.

#### Day 15: Deep-Dive Pandas Data Wrangling
**Theory (20 min):**  
Data cleaning strategies: dropping null values (`dropna`), filling gaps (`fillna`), grouping datasets (`groupby`), and merging frames like SQL joins.

**Interactive Code (20 min):**
```python
import pandas as pd

sales_data = pd.DataFrame({
    "Region": ["West", "East", "West", "North", "East"],
    "Revenue": [1500, 2300, 3100, 1100, 2900]
})
regional_yield = sales_data.groupby("Region")["Revenue"].sum().reset_index()
print(regional_yield)
```

**Real-World Exercise (20 min):**  
Build a data cleaning pipeline. Take an imperfect DataFrame containing missing numerical values and mismatched text strings. Impute missing figures with column averages and convert labels to uppercase formats.

***

#### Day 16: SQL Database Engineering Connectors
**Theory (20 min):**  
Bridging script files and database schemas. Interfacing with databases using `sqlite3` or SQLAlchemy. Querying databases via Python and outputting directly into Pandas structures.

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

**Real-World Exercise (20 min):**  
Establish a localized SQLite database instance. Programmatically construct an ETL script that reads a local list, pipes it into a table structure, and queries back active records.

***

#### Day 17: AI Integration & Automation Architecture
**Theory (20 min):**  
Designing intelligent automation frameworks. Communicating with large language models using APIs such as OpenAI or Google Gemini. Parsing structured inputs out of natural language payloads.

**Interactive Code (20 min):**
```python
# Abstract blueprint of an automated AI routing agent
def trigger_ai_agent(prompt_text: str):
    mock_payload = {"prompt": prompt_text, "temperature": 0.0}
    return f"AI Classification Output for: '{prompt_text}'"

print(trigger_ai_agent("Extract all tracking codes from invoice #4402"))
```

**Real-World Exercise (20 min):**  
Write a clean script containing a function that accepts an unstructured email body as input, formats an optimization prompt string, and prepares a complete JSON payload ready to be sent to an AI chat completion API.

***

#### Day 18: Core DSA Data Structures for Interviews
**Theory (20 min):**  
Preparing for screening interviews. Demystifying Big-O time and space complexity. Conceptualizing and writing algorithmic lookups utilizing hash maps and two-pointer approaches.

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

print(target_lookup([2, 7, 11, 15], 9))
```

**Real-World Exercise (20 min):**  
Write an optimal search function that identifies whether an input string array contains duplicate values in less than O(n^2) runtime complexity.

***

#### Day 19: Algorithmic Manipulation Patterns
**Theory (20 min):**  
Interview-heavy array and string manipulation techniques. Mastering index trackers, window slicing calculations, and handling multi-condition checks on numerical lists.

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

print(reverse_stream([1, 2, 3, 4, 5]))
```

**Real-World Exercise (20 min):**  
Write an efficient sorting logic or frequency array scanner that counts occurrences of characters inside text records, returning the top 3 most recurring elements.

***

#### Day 20: Comprehensive Mock Screening Blueprint
**Theory (20 min):**  
Synthesizing your skills. Simulating the pressure of a real technical interview. Managing code presentation structures and outlining logic aloud before writing any lines of code.

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

**Real-World Exercise (20 min):**  
Complete a full 20-minute timed sprint challenge: Write an automated file system audit function that processes a multi-level file path string, isolates file extensions, and aggregates counts using a dictionary tracker.

***

#### Day 21: Framework Consolidation & Multi-Directional Launch
**Theory (20 min):**  
Packaging your knowledge into production-ready skills. Deciding on your next specialization vector: Data Engineering, Data Science, or AI Automation. Building out a robust GitHub profile to showcase your code templates.

**Action Items (40 min):**
- Set up your portfolio directory structure.
- Push all previous daily exercise files to a public GitHub repository.
- Document your repository with an executive-level `README.md` file detailing your 21-day accelerated technical trajectory.

***

## Repository Goals

By the end of this challenge, you should be able to:

- write clean Python scripts confidently,
- understand and use core data structures,
- handle files and errors safely,
- use libraries like NumPy and Pandas,
- work with APIs and databases,
- solve interview-style problems,
- build automation-ready mini projects.

***

## Suggested Repo Structure

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

***

## How to Use This Repository

1. Read the theory for the day.
2. Type the interactive code manually.
3. Complete the real-world exercise.
4. Save your solution in the relevant day folder.
5. Revisit and improve previous scripts as your Python skills grow.

***

## Final Outcome

This roadmap is designed to help you move from beginner Python concepts into practical, career-aligned problem solving. By the end of the 21 days, you will have a stronger foundation for:
- data analysis,
- data science,
- data engineering,
- and AI automation.

***
