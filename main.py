# Demonstration of functionality
# Author: A. Wilcox <github.com/w3bCart3l>

import logging
from rotate import ProxyRotator
from router import ProxyRouter
from settings import SchedulerConfig, URLManager, RichConfig
from utils import load_proxies_from_file

def main():
    # Initialize logging
    logging.basicConfig(level=logging.INFO)

    # Load proxies from file
    proxies = load_proxies_from_file('sources.toml')

    # Initialize ProxyRotator with the list of proxies
    proxy_rotator = ProxyRotator(proxies)

    # Initialize ProxyRouter with loaded proxies
    proxy_router = ProxyRouter(proxies)

    # Initialize SchedulerConfig, URLManager, and RichConfig
    scheduler_config = SchedulerConfig()
    url_manager = URLManager()
    rich_config = RichConfig()

    # Example job for scheduler
    def example_job():
        logging.info("Running example job...")

    # Schedule the example job
    scheduler_config.add_job(example_job, 'interval', seconds=30)

    # Add a URL to sources.toml as an example
    url_manager.add_url("http", "http://example.com/proxies.txt")

    # Make a request using ProxyRouter
    response = proxy_router.request('GET', 'http://httpbin.org/ip')
    if response:
        logging.info(f"Response: {response.text}")

if __name__ == "__main__":
    main()
