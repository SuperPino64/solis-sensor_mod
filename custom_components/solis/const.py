"""Constants
For more information: https://github.com/hultenvp/solis-sensor/
"""

from typing import Any

from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import (
    PERCENTAGE,
    UnitOfApparentPower,
    UnitOfElectricCurrent,
    UnitOfElectricPotential,
    UnitOfEnergy,
    UnitOfFrequency,
    UnitOfPower,
    UnitOfReactivePower,
    UnitOfTemperature,
)

from .soliscloud_const import *

VERSION = "3.7.2"

# ATTRIBUTES
LAST_UPDATED = "Last updated"
SERIAL = "Inverter serial"
API_NAME = "API Name"

EMPTY_ATTR: dict[str, Any] = {
    LAST_UPDATED: None,
    SERIAL: None,
    API_NAME: None,
}


CONF_PORTAL_DOMAIN = "portal_domain"
CONF_USERNAME = "portal_username"
CONF_PASSWORD = "portal_password"
CONF_SECRET = "portal_secret"
CONF_KEY_ID = "portal_key_id"
CONF_PLANT_ID = "portal_plant_id"
CONF_CONTROL = "portal_control_api"
CONF_REFRESH_OK = "refresh_ok"
CONF_REFRESH_NOK = "refresh_nok"

DOMAIN = "solis"
SENSOR_PREFIX = "Solis"
DEFAULT_DOMAIN = "https://v3.soliscloud.com:13333"

# Supported sensor types:
# Key: ['label', unit, icon, device class, state class, api_attribute_name]
SENSOR_TYPES = {
    "inverterpowerstate": [
        "Power State",
        None,
        "mdi:power",
        None,
        SensorStateClass.MEASUREMENT,
        INVERTER_POWER_STATE,
    ],
    "inverterstate": [
        "State",
        None,
        "mdi:state-machine",
        None,
        SensorStateClass.MEASUREMENT,
        INVERTER_STATE,
    ],
    "timestamponline": [
        "Timestamp Inverter Online",
        None,
        "mdi:calendar-clock",
        None,
        SensorStateClass.MEASUREMENT,
        INVERTER_TIMESTAMP_ONLINE,
    ],
    "timestampmeasurement": [
        "Timestamp Measurements Received",
        None,
        "mdi:calendar-clock",
        None,
        SensorStateClass.MEASUREMENT,
        INVERTER_TIMESTAMP_UPDATE,
    ],
    "status": ["Status", None, "mdi:solar-power", None, None, "status"],
    "hmiversionall": [
        "HMI Version all",
        None,
        "mdi:solar-power",
        None,
        None,
        HMI_VERSION_ALL,
    ],
    "temperature": [
        "Temperature",
        UnitOfTemperature.CELSIUS,
        "mdi:thermometer",
        SensorDeviceClass.TEMPERATURE,
        SensorStateClass.MEASUREMENT,
        INVERTER_TEMPERATURE,
    ],
    "radiatortemperature1": [
        "Radiator temperature 1",  # Solarman only
        UnitOfTemperature.CELSIUS,
        "mdi:thermometer",
        SensorDeviceClass.TEMPERATURE,
        SensorStateClass.MEASUREMENT,
        RADIATOR1_TEMP,
    ],
    "acoutputvoltage1": [
        "AC Voltage R",
        UnitOfElectricPotential.VOLT,
        "mdi:flash-outline",
        SensorDeviceClass.VOLTAGE,
        SensorStateClass.MEASUREMENT,
        PHASE1_VOLTAGE,
    ],
    "acoutputcurrent1": [
        "AC Current R",
        UnitOfElectricCurrent.AMPERE,
        "mdi:flash-outline",
        SensorDeviceClass.CURRENT,
        SensorStateClass.MEASUREMENT,
        PHASE1_CURRENT,
    ],
    "actualpower": [
        "AC Output Total Power",
        UnitOfPower.WATT,
        "mdi:solar-power",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
        INVERTER_ACPOWER,
    ],
    "acfrequency": [
        "AC Frequency",
        UnitOfFrequency.HERTZ,
        "mdi:sine-wave",
        None,
        SensorStateClass.MEASUREMENT,
        INVERTER_ACFREQUENCY,
    ],
    "energylastmonth": [
        "Energy Last Month",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash-outline",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
        INVERTER_ENERGY_LAST_MONTH,
    ],
    "energytoday": [
        "Energy Today",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash-outline",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
        INVERTER_ENERGY_TODAY,
    ],
    "energythismonth": [
        "Energy This Month",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash-outline",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
        INVERTER_ENERGY_THIS_MONTH,
    ],
    "energythisyear": [
        "Energy This Year",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash-outline",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
        INVERTER_ENERGY_THIS_YEAR,
    ],
    "energytotal": [
        "Energy Total",
        UnitOfEnergy.KILO_WATT_HOUR,
        "mdi:flash-outline",
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
        INVERTER_ENERGY_TOTAL_LIFE,
    ],
}

for i in range(1,2):
    SENSOR_TYPES[f"dcinputvoltagepv{i}"] = [
        f"DC Voltage PV{i}",
        UnitOfElectricPotential.VOLT,
        "mdi:flash-outline",
        SensorDeviceClass.VOLTAGE,
        SensorStateClass.MEASUREMENT,
        globals()[f"STRING{i}_VOLTAGE"],
    ]

    SENSOR_TYPES[f"dcinputcurrentpv{i}"] = [
        f"DC Current PV{i}",
        UnitOfElectricCurrent.AMPERE,
        "mdi:flash-outline",
        SensorDeviceClass.CURRENT,
        SensorStateClass.MEASUREMENT,
        globals()[f"STRING{i}_CURRENT"],
    ]

    SENSOR_TYPES[f"dcinputpowerpv{i}"] = [
        f"DC Power PV{i}",
        UnitOfPower.WATT,
        "mdi:solar-power",
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
        globals()[f"STRING{i}_POWER"],
    ]
