# Web Scraping Exercises

This repository contains 5 basic web scraping exercises using Python, `requests`, and `BeautifulSoup`. These exercises aim to extract specific data from an example webpage.

## Exercises

1. **Social Links Scraping**: Scrapes and collects all social media links from a webpage.
    - **Method 1**: Using the CSS selectors and iterating through the `<a>` tags.
    - **Method 2**: Using `find` and `find_all` to locate and extract the links.
    - **Method 3**: One-liner method using `select`.

2. **Table Data Extraction**: Extracts the data of a table from the webpage and creates a pandas DataFrame.
    - Scrapes column names and all rows in a table, and then stores them in a structured format using pandas.

3. **Fun Facts Scraping (Word Filter)**: Filters and extracts all fun facts that contain the word "is".
    - Uses a regular expression to filter and extract items based on the presence of the word "is".

## Technologies Used

- **Python 3.x**
- **Requests**: To fetch the webpage content.
- **BeautifulSoup**: To parse the HTML content.
- **Pandas**: To work with tabular data (for the table extraction exercise).
- **Regular Expressions (re module)**: For pattern matching and filtering.

## Installation

Before running any of these exercises, make sure you have Python and the necessary libraries installed.

### Prerequisites

- **Python 3.x**
- **pip** (Python package manager)

### Install Required Libraries

Install the required libraries using pip:

```bash
pip install requests beautifulsoup4 pandas
