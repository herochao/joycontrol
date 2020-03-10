import asyncio

from joycontrol.controller_wrapper.pro_controller import ProController

async def _main():
    async with ProController() as pro_controller:

        # Now you can execute your scripts
        await pro_controller.push_buttons('down', sec=5)
        await pro_controller.wait(5)
        await pro_controller.push_button('home')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_main())
