from constants import TEMPERATURE_LIMITS


class BatteryMonitor:
    """
    Class to monitor battery temperature and classify breaches based on cooling type.
    
    Attributes:
        battery_characteristics (dict): A dictionary containing characteristics of the battery,
                                         such as its cooling type.
    """

    def __init__(self, battery_characteristics):
        """
        Initializes the BatteryMonitor with battery characteristics.

        Args:
            battery_characteristics (dict): A dictionary containing battery characteristics.
        """
        self.battery_characteristics = battery_characteristics

    def infer_breach(self, value):
        """
        Infers the breach status based on the provided temperature value.

        Args:
            value (float): The temperature value to evaluate.

        Returns:
            str: 'TOO_LOW' if the temperature is below the lower limit,
                 'TOO_HIGH' if above the upper limit,
                 'NORMAL' if within acceptable range.
        """
        lower_limit, upper_limit = TEMPERATURE_LIMITS[self.battery_characteristics['coolingType']]
        if value < lower_limit:
            return 'TOO_LOW'
        if value > upper_limit:
            return 'TOO_HIGH'
        return 'NORMAL'

    def classify_temperature_breach(self, temperature_in_c):
        """
        Classifies the temperature breach status.

        Args:
            temperature_in_c (float): The temperature in Celsius to classify.

        Returns:
            str: The breach classification ('TOO_LOW', 'TOO_HIGH', or 'NORMAL').
        """
        return self.infer_breach(temperature_in_c)
