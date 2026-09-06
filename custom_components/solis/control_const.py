import logging
from dataclasses import dataclass
from datetime import datetime

from homeassistant.components.button import ButtonEntityDescription
from homeassistant.components.number import NumberDeviceClass, NumberEntityDescription
from homeassistant.components.select import SelectEntityDescription
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.time import TimeEntityDescription
from homeassistant.const import PERCENTAGE, UnitOfElectricCurrent, UnitOfPower
from homeassistant.helpers.entity import DeviceInfo

from .const import API_NAME, DOMAIN, EMPTY_ATTR, SERIAL

RETRIES = 100
RETRY_WAIT = 10

_LOGGER = logging.getLogger(__name__)


class SolisBaseControlEntity:
    _attr_entity_registry_enabled_default = True

    def __init__(self, service, config_name, inverter_sn, cid, info):
        self._measured: datetime | None = None
        self._entity_type = "control"
        self._attributes = dict(EMPTY_ATTR)
        self._attributes[SERIAL] = inverter_sn
        self._attributes[API_NAME] = service.api_name
        self._api = service.api
        self._platform_name = config_name
        self._name = f"{config_name.title()} {info.name}"
        self._key = f"{config_name}_{info.key}"
        self._inverter_sn = inverter_sn
        self._cid = cid
        self._splitter = ()
        self._index = 0
        self._joiner = ","

    @property
    def unique_id(self) -> str:
        return f"{self._platform_name}_{self._inverter_sn}_{self._key}"

    @property
    def name(self) -> str:
        return self._name

    @property
    def cid(self) -> int:
        return int(self._cid)

    @property
    def index(self) -> int:
        return self._index

    @property
    def device_info(self) -> DeviceInfo | None:
        """Return a device description for device registry."""
        return DeviceInfo(
            identifiers={
                (
                    DOMAIN,
                    f"{self._attributes[SERIAL]}_{self._attributes[API_NAME]}",
                )
            },
            manufacturer=f"Solis",
            name=f"Solis_Inverter_{self._attributes[SERIAL]}",
        )

    async def write_control_data(self, value: str) -> bool:
        data = await self._api.write_control_data(self._attributes[SERIAL], self.cid, value)
        return data

    def split(self, value):
        if len(self._splitter) > 0:
            # if there's more than one split string then replace all of the later ones with the first before we split
            for x in self._splitter[1:]:
                value = value.replace(x, self._splitter[0])
            values = value.split(self._splitter[0])

            if self._index <= len(values):
                return values[self._index]
            else:
                _LOGGER.warning(f"Unable to retrieve item {self._index:d} from {value} for {self._key}")
        else:
            return value


@dataclass
class SolisSelectEntityDescription(SelectEntityDescription):
    option_dict: dict = None
    unit: type = float


@dataclass
class SolisNumberEntityDescription(NumberEntityDescription):
    splitter: tuple = ()


@dataclass
class SolisTimeEntityDescription(TimeEntityDescription):
    splitter: tuple = ()


@dataclass
class SolisButtonEntityDescription(ButtonEntityDescription):
    joiner: str = ","


# Control types dict[bool: dict] where key is HMI flag

CONTROL_TYPES = {
    "time": SolisTimeEntityDescription,
    "number": SolisNumberEntityDescription,
    "select": SolisSelectEntityDescription,
    "button": SolisButtonEntityDescription,
}

ALL_CONTROLS = {
    True: {
      
        "15": [
            SolisNumberEntityDescription(
                name="Power limit setting",
                key="power_limit_setting",
                native_unit_of_measurement=PERCENTAGE,
                device_class=NumberDeviceClass.POWER_FACTOR,
                icon="mdi:transmission-tower-export",
                native_min_value=0,
                native_max_value=110,
                native_step=1,
            )
        ],
        "696": [
            SolisNumberEntityDescription(
    },
}
