import logging
import threading
import time
import psutil
from typing import Callable, Any
from functools import wraps


def log_entry_exit(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logging.info(f"Entering {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Exiting {func.__name__}")
        return result
    return wrapper


def exception_handler(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Exception in {func.__name__}: {e}")
            raise
    return wrapper


class SelfHealing:
    def __init__(self) -> None:
        """
        Initialize SelfHealing with monitoring flag and restart threshold.
        """
        self.monitoring: bool = False
        self.restart_threshold: int = 90  # CPU usage %

    @log_entry_exit
    def initialize(self) -> None:
        """
        Initialize self-healing mechanisms and start monitoring thread.
        """
        logging.info("Self-healing mechanisms initialized")
        print("Self-healing mechanisms initialized")

        # Start monitoring thread
        self.monitoring = True
        threading.Thread(target=self.monitor_system, daemon=True).start()

    @log_entry_exit
    @exception_handler
    def monitor_system(self) -> None:
        """
        Monitor system resources and restart components if thresholds exceeded.
        """
        while self.monitoring:
            cpu_usage: float = psutil.cpu_percent(interval=1)
            memory_usage: float = psutil.virtual_memory().percent

            if cpu_usage > self.restart_threshold or memory_usage > 90:
                logging.warning(f"High resource usage: CPU {cpu_usage}%, Memory {memory_usage}%")
                print(f"High resource usage: CPU {cpu_usage}%, Memory {memory_usage}%")
                self.restart_components()

            time.sleep(10)

    @log_entry_exit
    @exception_handler
    def restart_components(self) -> None:
        """
        Restart critical components to recover from high resource usage.
        """
        logging.info("Restarting components...")
        print("Restarting components...")
        # Placeholder for restart logic
        # For example, restart firewall or blockchain clients
        try:
            # Simulate restart
            time.sleep(2)
            logging.info("Components restarted successfully")
            print("Components restarted successfully")
        except Exception as e:
            logging.error(f"Restart error: {e}")
