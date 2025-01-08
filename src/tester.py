import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    TimeoutException,
    WebDriverException,
    InvalidArgumentException
)
from urllib.parse import urlparse

class WebPagePerformanceTester:
    def __init__(self, driver_path):
        """Initialize the tester with the path to ChromeDriver."""
        self.driver_path = driver_path
        self.driver = None
    
    def _initialize_driver(self):
        """Initialize ChromeDriver with necessary options."""
        service = Service(self.driver_path)
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Headless mode for faster execution
        options.add_argument("--disable-gpu")
        options.add_argument("--use-gl=swiftshader")
        options.add_argument("--enable-unsafe-webgl")
        options.add_argument("--no-sandbox")
        options.add_argument("--start-maximized")
        
        # Set logging preferences using set_capability
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        
        self.driver = webdriver.Chrome(service=service, options=options)
    
    def _get_domain(self, url):
        """Extract the domain name from the URL for naming files."""
        parsed_url = urlparse(url)
        return parsed_url.netloc.replace('.', '_')
    
    def _count_http_requests(self):
        """Count the total number of HTTP requests from browser logs."""
        logs = self.driver.get_log("performance")
        http_requests = 0
        for entry in logs:
            message = entry["message"]
            if '"Network.requestWillBeSent"' in message:
                http_requests += 1
        return http_requests
    
    def run_test(self, url):
        """Run the performance test on the given URL."""
        try:
            self._initialize_driver()
            self.driver.set_page_load_timeout(15)  # Set a 15-second timeout for page load
            self.driver.get(url)
            
            # Measure page load time
            start_time = time.time()
            self.driver.execute_script("return document.readyState === 'complete'")
            load_time = time.time() - start_time
            
            # Count resources
            images = len(self.driver.find_elements(By.TAG_NAME, 'img'))
            scripts = len(self.driver.find_elements(By.TAG_NAME, 'script'))
            stylesheets = len(self.driver.find_elements(By.TAG_NAME, 'link'))
            
            # Count HTTP requests
            http_requests = self._count_http_requests()
            
            # Capture screenshot
            domain = self._get_domain(url)
            screenshot_path = f"output/screenshots/{domain}_screenshot.png"
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
            self.driver.save_screenshot(screenshot_path)
            
            # Return collected metrics and screenshot path
            metrics = {
                "domain": domain,
                "load_time": round(load_time, 2),
                "images": images,
                "scripts": scripts,
                "stylesheets": stylesheets,
                "http_requests": http_requests
            }
            
            return metrics, screenshot_path
        
        except TimeoutException:
            print(f"Error: The page '{url}' took too long to load and was aborted.")
            return None
        except InvalidArgumentException:
            print(f"Error: The URL '{url}' is invalid. Please check the format.")
            return None
        except WebDriverException as e:
            print(f"Error: WebDriver encountered an issue: {e}")
            return None
        finally:
            if self.driver:
                self.driver.quit()
