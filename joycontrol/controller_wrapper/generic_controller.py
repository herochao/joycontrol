import logging
import asyncio

from joycontrol import logging_default as log
from joycontrol.protocol import controller_protocol_factory
from joycontrol.server import create_hid_server
from joycontrol.controller_state import button_push


logger = logging.getLogger(__name__)

class GenericController:

    def __init__(self, controller, capture_file=None, spi_flash=None):
        self.factory = controller_protocol_factory(controller, spi_flash=spi_flash)
        self.capture_file = capture_file

    async def __aenter__(self):
        self.transport, protocol = await create_hid_server(self.factory, 17, 19, self.capture_file)
        self.controller_state = protocol.get_controller_state()
        await self.controller_state.connect()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        logger.info('Stopping communication...')
        await self.transport.close()

    async def push_buttons(self, *buttons, sec=0.1):
        await button_push(self.controller_state, buttons, sec)

    async def sleep(self, time):
        asyncio.sleep(time)
