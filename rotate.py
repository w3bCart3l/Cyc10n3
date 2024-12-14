#  This module is designed to manage and rotate proxies efficiently. It includes methods to add, remove, and rotate proxies.
# Author A. Wilcox <github.com/w3bCart3l> 

import random
import logging
from utils import is_proxy_working

class ProxyRotator:
    """
    A class to manage and rotate proxies.
    """

    def __init__(self, proxies):
        """
        Initialize the ProxyRotator with a list of proxies.
        
        Args:
            proxies (list): A list of proxy URLs.
        """
        self.proxies = proxies
        self.current_proxy_index = 0

    def add_proxy(self, proxy):
        """
        Add a proxy to the list.
        
        Args:
            proxy (str): The proxy to add (e.g., "http://123.456.789.012:8080").
        """
        self.proxies.append(proxy)
        logging.info(f"Proxy added: {proxy}")

    def remove_proxy(self, proxy):
        """
        Remove a proxy from the list.
        
        Args:
            proxy (str): The proxy to remove.
        """
        if proxy in self.proxies:
            self.proxies.remove(proxy)
            logging.info(f"Proxy removed: {proxy}")
        else:
            logging.warning(f"Proxy not found: {proxy}")

    def get_next_proxy(self):
        """
        Get the next proxy in the list, rotating to the beginning if necessary.
        
        Returns:
            str: The next proxy.
        """
        if not self.proxies:
            raise IndexError("No proxies available")
        
        proxy = self.proxies[self.current_proxy_index]
        self.current_proxy_index = (self.current_proxy_index + 1) % len(self.proxies)
        return proxy

    def get_random_proxy(self):
        """
        Get a random proxy from the list.
        
        Returns:
            str: A random proxy.
        """
        if not self.proxies:
            raise IndexError("No proxies available")
        
        return random.choice(self.proxies)

    def validate_proxies(self, test_url, timeout=10):
        """
        Validate all proxies in the list, removing those that fail.
        
        Args:
            test_url (str): The URL to test the proxies against.
            timeout (int): The timeout for the proxy test (in seconds).
        """
        valid_proxies = []
        for proxy in self.proxies:
            if is_proxy_working(proxy, test_url, timeout):
                valid_proxies.append(proxy)
            else:
                logging.warning(f"Proxy failed: {proxy}")
        
        self.proxies = valid_proxies
        logging.info(f"Validated proxies: {len(self.proxies)} remaining")
