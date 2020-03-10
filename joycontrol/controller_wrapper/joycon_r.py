from joycontrol.controller_wrapper.generic_controller import GenericController
from joycontrol.protocol import Controller

class JoyCon_R(GenericController):
    def __init__(self, capture_file=None, spi_flash=None):
        super().__init__(Controller.JOYCON_R, capture_file, spi_flash)
