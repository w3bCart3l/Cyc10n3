# This file manages settings for scheduling proxy scrape jobs, adding proxylist sources to the sources.toml file, and UI configuration
# This file facilitates easy configuration and integration with future modules
# Author: A. Wilcox <github.com/w3bCart3l>

import os
import logging
from rich.console import Console
from rich.logging import RichHandler
from apscheduler.schedulers.background import BackgroundScheduler
import toml

# Initialize Rich Console
console = Console()

# Scrape Job Scheduling Configuration
class SchedulerConfig:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

    def add_job(self, func, trigger, **kwargs):
        """
        Add a job to the scheduler.
        
        Args:
            func (callable): The function to schedule.
            trigger (str): The type of trigger (e.g., 'interval', 'cron').
            **kwargs: Additional arguments for the trigger.
        """
        self.scheduler.add_job(func, trigger, **kwargs)
        console.log(f"Job scheduled: {func.__name__} with trigger {trigger}", style="bold green")

# URL Management for sources.toml
class URLManager:
    def __init__(self, sources_file="sources.toml"):
        self.sources_file = sources_file
        if not os.path.exists(sources_file):
            raise FileNotFoundError(f"{sources_file} not found")

    def add_url(self, proto, url):
        """
        Add a URL to the sources.toml file.
        
        Args:
            proto (str): The protocol section (e.g., 'http', 'socks5').
            url (str): The URL to add.
        """
        with open(self.sources_file, "r") as file:
            sources = toml.load(file)
        
        if proto not in sources:
            sources[proto] = {"sources": []}
        
        sources[proto]["sources"].append(url)
        
        with open(self.sources_file, "w") as file:
            toml.dump(sources, file)
        
        console.log(f"URL added to {proto}: {url}", style="bold green")

# Rich Console Configuration
class RichConfig:
    def __init__(self):
        logging.basicConfig(level="INFO", format="%(message)s", handlers=[RichHandler()])
        console.log("Rich logging initialized", style="bold green")

# Example of how to use the settings
if __name__ == "__main__":
    # Initialize configurations
    scheduler_config = SchedulerConfig()
    url_manager = URLManager()
    rich_config = RichConfig()

    # Add a scrape job example
    def example_job():
        console.log("Running example job...", style="bold blue")
    
    scheduler_config.add_job(example_job, 'interval', seconds=30)

    # Add a URL to sources.toml example
    url_manager.add_url("http", "http://example.com/proxies.txt")

    # Rich console example
    console.print("[bold magenta]This is a Rich console example![/bold magenta]")
