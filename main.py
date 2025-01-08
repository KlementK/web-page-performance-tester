import argparse
import os
from src.tester import WebPagePerformanceTester
from src.report_generator import ReportGenerator


def main():
    """Main function to handle the web page performance test."""
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Web Page Performance Tester")
    parser.add_argument('--url', type=str, required=True, help="URL of the web page to test")
    parser.add_argument('--export', choices=['txt', 'csv', 'json', 'all'], default='txt',
                        help="Export format for the report")
    args = parser.parse_args()

    url = args.url
    export_format = args.export

    print(f"Starting performance test for: {url}")

    # Initialize the performance tester
    tester = WebPagePerformanceTester(driver_path="webdriver/chromedriver.exe")

    # Run the performance test
    result = tester.run_test(url)

    if result is None:
        print("Performance test failed. Please check the error message above.")
        return  # Exit if the test fails

    metrics, screenshot_path = result

    # Generate and save the report in the requested format
    domain = metrics['domain']
    os.makedirs("output/reports", exist_ok=True)

    if export_format in ['txt', 'all']:
        report = ReportGenerator.generate_report(url, metrics, screenshot_path)
        report_path = f"output/reports/{domain}_performance_report.txt"
        with open(report_path, "w") as report_file:
            report_file.write(report)
        print(f"Performance report saved: {report_path}")

    if export_format in ['csv', 'all']:
        csv_path = f"output/reports/{domain}_performance_report.csv"
        ReportGenerator.export_to_csv(url, metrics, screenshot_path, csv_path)
        print(f"CSV report saved: {csv_path}")

    if export_format in ['json', 'all']:
        json_path = f"output/reports/{domain}_performance_report.json"
        ReportGenerator.export_to_json(url, metrics, screenshot_path, json_path)
        print(f"JSON report saved: {json_path}")

    print(f"Screenshot saved: {screenshot_path}")

    return  # Ensure the script exits cleanly


if __name__ == "__main__":
    main()
