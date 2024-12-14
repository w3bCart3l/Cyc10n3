#  Provides utility functions for the module 
# Author: A. Wilcox <github.com/w3bCart3l>
import requests
import logging

def is_proxy_working(proxy, test_url, timeout=10):
    """
    Check if a proxy is working by making a request to a test URL.
    
    Args:
        proxy (str): The proxy to test.
        test_url (str): The URL to test the proxy against.
        timeout (int): The timeout for the request (in seconds).
    
    Returns:
        bool: True if the proxy is working, False otherwise.
    """
    proxies = {"http": proxy, "https": proxy}
    try:
        response = requests.get(test_url, proxies=proxies, timeout=timeout)
        if response.status_code == 200:
            logging.info(f"Proxy working: {proxy}")
            return True
    except requests.RequestException as e:
        logging.warning(f"Proxy failed: {proxy}, Error: {e}")
    return False

def load_proxies_from_file(file_path):
    """
    Load proxies from a file.
    
    Args:
        file_path (str): Path to the file containing proxies.
    
    Returns:
        list: A list of proxies.
    """
    with open(file_path, "r") as file:
        return file.read().splitlines()
