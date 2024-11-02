def infer_breach(value, limits):
    """Determine if a value is within, above, or below the defined limits."""
    if value < limits['lower']:
        return 'TOO_LOW'
    if value > limits['upper']:
        return 'TOO_HIGH'
    return 'NORMAL'


def get_temperature_limits(coolingType):
    """Define temperature limits based on cooling type."""
    limits = {
        'PASSIVE_COOLING': {'lower': 0, 'upper': 35},
        'HI_ACTIVE_COOLING': {'lower': 0, 'upper': 45},
        'MED_ACTIVE_COOLING': {'lower': 0, 'upper': 40}
    }
    return limits.get(coolingType, {'lower': 0, 'upper': 0})


def classify_temperature_breach(coolingType, temperatureInC):
    """Classify the temperature breach based on cooling type and temperature."""
    limits = get_temperature_limits(coolingType)
    return infer_breach(temperatureInC, limits)


def check_and_alert(alertTarget, batteryChar, temperatureInC):
    """Check temperature classification and alert the appropriate target."""
    breachType = classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
    alert_dispatcher = {
        'TO_CONTROLLER': send_to_controller,
        'TO_EMAIL': send_to_email
    }
    alert_action = alert_dispatcher.get(alertTarget)
    if alert_action:
        alert_action(breachType)


def send_to_controller(breachType):
    """Simulate sending breach information to a controller."""
    header = 0xfeed
    print(f'{header}, {breachType}')


def send_to_email(breachType):
    """Simulate sending breach information via email."""
    recipient = "a.b@c.com"
    message = {
        'TOO_LOW': "Hi, the temperature is too low",
        'TOO_HIGH': "Hi, the temperature is too high"
    }
    if breachType in message:
        print(f'To: {recipient}')
        print(message[breachType])
