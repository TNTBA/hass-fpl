"""Top 15 candidate sensors discovered from deep API payload analysis."""

from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import PERCENTAGE, UnitOfPower, UnitOfTemperature

from .fplEntity import FplEntity, FplEnergyEntity, FplMoneyEntity


class _MeasurementEntity(FplEntity):
    _attr_state_class = SensorStateClass.MEASUREMENT


class MaxDemandKWSensor(_MeasurementEntity):
    _attr_device_class = SensorDeviceClass.POWER
    _attr_native_unit_of_measurement = UnitOfPower.KILO_WATT

    def __init__(self, coordinator, config, account):
        super().__init__(coordinator, config, account, "Max Demand kW")

    @property
    def native_value(self):
        return self.getData("maxDemandKw")


class OnPeakDemandKWSensor(_MeasurementEntity):
    _attr_device_class = SensorDeviceClass.POWER
    _attr_native_unit_of_measurement = UnitOfPower.KILO_WATT

    def __init__(self, coordinator, config, account):
        super().__init__(coordinator, config, account, "On Peak Demand kW")

    @property
    def native_value(self):
        return self.getData("onPeakDemandKw")


class PreviousBillAmountSensor(FplMoneyEntity):
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator, config, account):
        super().__init__(coordinator, config, account, "Previous Bill Amount")

    @property
    def native_value(self):
        return self.getData("previousBillAmount")


class BillDiffSensor(FplMoneyEntity):
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator, config, account):
        super().__init__(coordinator, config, account, "Bill Difference")

    @property
    def native_value(self):
        return self.getData("billDiff")


class TodayMeterReadSensor(FplEnergyEntity):
    _attr_state_class = SensorStateClass.TOTAL_INCREASING

    def __init__(self, coordinator, config, account):
        super().__init__(coordinator, config, account, "Today Meter Read")

    @property
    def native_value(self):
        return self.getData("todayMeterRead")


class CurrentBillReadSensor(FplEnergyEntity):
    _attr_state_class = SensorStateClass.TOTAL_INCREASING

    def __init__(self, coordinator, config, account):
        super().__init__(coordinator, config, account, "Current Bill Read")

    @property
    def native_value(self):
        return self.getData("currentBillRead")


class PreviousBillReadSensor(FplEnergyEntity):
    _attr_state_class = SensorStateClass.TOTAL_INCREASING

    def __init__(self, coordinator, config, account):
        super().__init__(coordinator, config, account, "Previous Bill Read")

    @property
    def native_value(self):
        return self.getData("previousBillRead")


class AvgTemperatureSensor(_MeasurementEntity):
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_native_unit_of_measurement = UnitOfTemperature.FAHRENHEIT

    def __init__(self, coordinator, config, account):
        super().__init__(coordinator, config, account, "Average Temperature")

    @property
    def native_value(self):
        return self.getData("avgTemp")


class DailyNetReceivedKWHSensor(FplEnergyEntity):
    _attr_state_class = SensorStateClass.TOTAL

    def __init__(self, coordinator, config, account):
        super().__init__(coordinator, config, account, "Daily Net Received kWh")

    @property
    def native_value(self):
        daily = self.getData("DailyUsage")
        if daily is None:
            return None
        return daily.get("netReceivedKwh")


class DailyNetReceivedReadingSensor(FplEnergyEntity):
    _attr_state_class = SensorStateClass.TOTAL_INCREASING

    def __init__(self, coordinator, config, account):
        super().__init__(
            coordinator, config, account, "Daily Net Received Meter Reading"
        )

    @property
    def native_value(self):
        daily = self.getData("DailyUsage")
        if daily is None:
            return None
        return daily.get("netReceivedReading")


class DailyTemperatureSensor(_MeasurementEntity):
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_native_unit_of_measurement = UnitOfTemperature.FAHRENHEIT

    def __init__(self, coordinator, config, account):
        super().__init__(coordinator, config, account, "Daily Temperature")

    @property
    def native_value(self):
        daily = self.getData("DailyUsage")
        if daily is None:
            return None
        return daily.get("temperature")


class DailyHumiditySensor(_MeasurementEntity):
    _attr_device_class = SensorDeviceClass.HUMIDITY
    _attr_native_unit_of_measurement = PERCENTAGE

    def __init__(self, coordinator, config, account):
        super().__init__(coordinator, config, account, "Daily Humidity")

    @property
    def native_value(self):
        daily = self.getData("DailyUsage")
        if daily is None:
            return None
        return daily.get("humidity")


class MonthlyBillingChargeSensor(FplMoneyEntity):
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator, config, account):
        super().__init__(coordinator, config, account, "Monthly Billing Charge")

    @property
    def native_value(self):
        return self.getData("monthlyBillingCharge")


class MonthlyKwhUsedSensor(FplEnergyEntity):
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator, config, account):
        super().__init__(coordinator, config, account, "Monthly kWh Used")

    @property
    def native_value(self):
        return self.getData("monthlyKwhUsed")


class MonthlyOnPeakConsumptionSensor(FplEnergyEntity):
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator, config, account):
        super().__init__(coordinator, config, account, "Monthly On Peak Consumption")

    @property
    def native_value(self):
        return self.getData("monthlyOnPeakConsumption")
