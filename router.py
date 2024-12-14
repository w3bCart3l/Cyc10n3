# Handles the routing of requests through rotating proxies.
# It integrates with the proxy rotator to manage proxy usage and includes methods to create a session and make requests with rotating proxies. 
# Author: A. Wilcox <github.com/w3bCart3l>

import requests
import logging
from rotate import ProxyRotator
from utils import is_proxy_working

class ProxyRouter:
    """
    A class to manage routing requests through rotating proxies.
    """

    def __init__(self, proxies):
        """
        Initialize the ProxyRouter with a list of proxies.
        
        Args:
            proxies (list): A list of proxy URLs.
        """
        self.proxy_rotator = ProxyRotator(proxies)

    def get_session(self):
        """
        Get a requests session with a rotating proxy.
        
        Returns:
            requests.Session: A session with a proxy set.
        """
        session = requests.Session()
        proxy = self.proxy_rotator.get_next_proxy()
        session.proxies = {"http": proxy, "https": proxy}
        return session

    def request(self, method, url, **kwargs):
        """
        Make a request using a rotating proxy.
        
        Args:
            method (str): HTTP method (e.g., 'GET', 'POST').
            url (str): The URL for the request.
            **kwargs: Additional arguments for the request.
        
        Returns:
            requests.Response: The response object.
        """
        session = self.get_session()
        try:
            response = session.request(method, url, **kwargs)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logging.warning(f"Request failed with proxy {session.proxies['http']}: {e}")
            return None
