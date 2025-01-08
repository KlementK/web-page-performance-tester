import argparse
from src.tester import WebPagePerformanceTester
from src.report_generator import ReportGenerator
import os

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Web Page Performance Tester")
    parser.add_argument('--url', type=str, required=True, help="URL of the web page to test")
    args = parser.parse_args()
    
    url = args.url
    print(f"Starting performance test for: {url}")
    
    # Initialize the performance tester
    tester = WebPagePerformanceTester(driver_path="webdriver/chromedriver.exe")
    
    # Run the performance test
    metrics, screenshot_path = tester.run_test(url)
    
    # Generate the performance report
    report = ReportGenerator.generate_report(url, metrics, screenshot_path)
    
    # Ensure the output/reports directory exists
    os.makedirs("output/reports", exist_ok=True)
    
    # Save the report
    report_path = f"output/reports/{metrics['domain']}_performance_report.txt"
    with open(report_path, "w") as report_file:
        report_file.write(report)
    
    print(f"Performance report saved: {report_path}")
    print(f"Screenshot saved: {screenshot_path}")

if __name__ == "__main__":
    main()
