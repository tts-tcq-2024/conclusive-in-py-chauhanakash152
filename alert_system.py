# alert_system.py

class AlertSystem:
    """
    Class to handle alerting mechanisms based on battery temperature breaches.

    Attributes:
        alert_target (str): The target for alerting, either 'TO_CONTROLLER' or 'TO_EMAIL'.
    """

    def __init__(self, alert_target):
        """
        Initializes the AlertSystem with the specified alert target.

        Args:
            alert_target (str): The target to send alerts to (e.g., controller or email).
        """
        self.alert_target = alert_target

    def send_to_controller(self, breach_type):
        """
        Sends the breach type information to the controller.

        Args:
            breach_type (str): The classification of the temperature breach.
        """
        header = 0xfeed
        print(f'{header}, {breach_type}')

    def send_to_email(self, breach_type):
        """
        Sends an email alert based on the temperature breach classification.

        Args:
            breach_type (str): The classification of the temperature breach.
        """
        recipient = "a.b@c.com"
        if breach_type == 'TOO_LOW':
            print(f'To: {recipient}')
            print('Hi, the temperature is too low')
        elif breach_type == 'TOO_HIGH':
            print(f'To: {recipient}')
            print('Hi, the temperature is too high')

    def check_and_alert(self, battery_monitor, temperature_in_c):
        """
        Checks for temperature breaches and sends alerts accordingly.

        Args:
            battery_monitor (BatteryMonitor): An instance of the BatteryMonitor class.
            temperature_in_c (float): The current temperature in Celsius to evaluate.
        """
        breach_type = battery_monitor.classify_temperature_breach(temperature_in_c)
        if self.alert_target == 'TO_CONTROLLER':
            self.send_to_controller(breach_type)
        elif self.alert_target == 'TO_EMAIL':
            self.send_to_email(breach_type)
