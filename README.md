# **Web Page Performance Tester**

This project is a **Web Page Performance Tester** that measures key performance metrics of a web page, including page load time, resource counts (images, scripts, stylesheets), and the total number of HTTP requests. Additionally, it captures a screenshot of the page and exports the results in multiple formats (TXT, CSV, JSON).

---

## **Features**

- Measures **page load time**.
- Counts the number of **images**, **scripts**, and **stylesheets** loaded by the page.
- Tracks the total number of **HTTP requests** made during the page load.
- Captures a **screenshot** of the fully loaded page.
- Exports performance reports in:
  - **Plain-text (TXT)**.
  - **Comma-Separated Values (CSV)**.
  - **JavaScript Object Notation (JSON)**.
- Handles common errors such as **timeout issues** and **invalid URLs**.

---

## **Installation Instructions**

### **Prerequisites**

1. **Python 3.8+** must be installed.
2. **Google Chrome** must be installed.
3. **ChromeDriver** must be downloaded (compatible with your Chrome version).
   - You can download ChromeDriver from [here](https://sites.google.com/chromium.org/driver/downloads).
4. Ensure **ChromeDriver**.exe is placed in a folder named `webdriver/` inside the project directory.

---

### **Steps to Install**

Before running the script, ensure you have:

1. Cloned the repository.
2. Created and activated a virtual environment.
3. Installed the required dependencies using `requirements.txt`.

---

## **Usage**

### **Basic Command**

To run the performance tester for a specific URL, use the following command:

```bash
python main.py --url <URL> --export <FORMAT>
```

- Replace `<URL>` with the web page URL you want to test.
- Replace `<FORMAT>` with one of the following export formats:
  - `txt` (default): Exports a plain-text report.
  - `csv`: Exports a CSV report.
  - `json`: Exports a JSON report.
  - `all`: Exports all three formats (TXT, CSV, and JSON).

### **Example Commands**

1. Export a plain-text report for `https://example.com`:

```bash
python main.py --url https://example.com --export txt
```

2. Export a CSV report for `https://example.com`:

```bash
python main.py --url https://example.com --export csv
```

3. Export all report formats for `https://example.com`

```bash
python main.py --url https://example.com --export all
```


---

## **Output**

The performance tester creates an `output/` folder in the project directory. Inside this folder, the following subfolders and files are generated:

1. **Reports** (`output/reports/`):
- Contains the performance reports in TXT, CSV, and JSON formats.

2. **Screenshots** (`output/screenshots/`):
- Contains screenshots of the tested web pages in PNG format.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to copy, modify, and share this project. Contributions are welcome!
