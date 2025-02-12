# Web Scraping Price Comparison Tool

## Problem Statement
With multiple e-commerce platforms available, comparing product prices across different websites can be a tedious and time-consuming task. This project aims to automate the process by extracting product details and prices from popular online stores such as Amazon, Flipkart, and Snapdeal, making price comparison seamless and efficient.

## Solution
This project is a Python-based web scraper that fetches product names and prices from various e-commerce platforms using **BeautifulSoup** and **requests**. It organizes the extracted data into a structured table format, allowing users to compare prices easily. Additionally, it includes CAPTCHA detection handling to notify users when manual intervention is required.

## Tech Stack
- **Programming Language:** Python
- **Libraries Used:**
  - `requests` (for fetching webpage data)
  - `BeautifulSoup` (for parsing HTML content)
  - `tldextract` (for extracting domain names)
  - `cv2` (for CAPTCHA image handling)
  - `prettytable` (for tabular representation of data)

## Brief Overview of Process
1. The user inputs two product URLs.
2. The script fetches the HTML content of the given URLs using the `requests` library.
3. The extracted domain is checked to determine the corresponding scraping function.
4. Using **BeautifulSoup**, product name and price are extracted based on predefined HTML structures for each website.
5. The extracted data is displayed in a table format using `PrettyTable`.
6. If CAPTCHA is detected, the script alerts the user and prompts manual input.
