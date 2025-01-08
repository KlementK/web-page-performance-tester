from datetime import datetime

class ReportGenerator:
    @staticmethod
    def generate_report(url, metrics, screenshot_path):
        """Generate a plain-text performance report."""
        report = []
        report.append("--- Web Page Performance Report ---")
        report.append(f"URL: {url}")
        report.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        report.append("Page Load Time:")
        report.append(f"- Load Event: {metrics['load_time']} seconds\n")
        
        report.append("Resources Loaded:")
        report.append(f"- Images: {metrics['images']}")
        report.append(f"- Scripts: {metrics['scripts']}")
        report.append(f"- Stylesheets: {metrics['stylesheets']}\n")
        
        report.append(f"HTTP Requests: {metrics['http_requests']}\n")
        
        report.append(f"Screenshot: saved as {screenshot_path}")
        report.append("--------------------------------------")
        
        return "\n".join(report)
