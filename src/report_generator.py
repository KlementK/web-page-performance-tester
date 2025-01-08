import os
import csv
import json
from datetime import datetime

class ReportGenerator:
    @staticmethod
    def generate_report(url, metrics, screenshot_path):
        """Generate a plain-text performance report."""
        report = [
            "--- Web Page Performance Report ---",
            f"URL: {url}",
            f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
            "Page Load Time:",
            f"- Load Event: {metrics['load_time']} seconds\n",
            "Resources Loaded:",
            f"- Images: {metrics['images']}",
            f"- Scripts: {metrics['scripts']}",
            f"- Stylesheets: {metrics['stylesheets']}\n",
            f"HTTP Requests: {metrics['http_requests']}\n",
            f"Screenshot: saved as {screenshot_path}",
            "--------------------------------------"
        ]
        return "\n".join(report)

    @staticmethod
    def export_to_csv(url, metrics, screenshot_path, csv_path):
        """Export the performance report to a CSV file."""
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        with open(csv_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Metric", "Value"])
            writer.writerow(["URL", url])
            writer.writerow(["Date", datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
            writer.writerow(["Load Time (seconds)", metrics["load_time"]])
            writer.writerow(["Images", metrics["images"]])
            writer.writerow(["Scripts", metrics["scripts"]])
            writer.writerow(["Stylesheets", metrics["stylesheets"]])
            writer.writerow(["HTTP Requests", metrics["http_requests"]])
            writer.writerow(["Screenshot", screenshot_path])

    @staticmethod
    def export_to_json(url, metrics, screenshot_path, json_path):
        """Export the performance report to a JSON file."""
        os.makedirs(os.path.dirname(json_path), exist_ok=True)
        data = {
            "URL": url,
            "Date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "Load Time (seconds)": metrics["load_time"],
            "Images": metrics["images"],
            "Scripts": metrics["scripts"],
            "Stylesheets": metrics["stylesheets"],
            "HTTP Requests": metrics["http_requests"],
            "Screenshot": screenshot_path
        }
        with open(json_path, "w") as file:
            json.dump(data, file, indent=4)
