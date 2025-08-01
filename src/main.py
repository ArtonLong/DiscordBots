from cedmodcleanupbot import CleanupBot
from reactbot import ReactBot
from donatormanagmentbot import DonatorManagmentBot
import os
import asyncio

async def run_bots():
    cleanup_botEU1 = CleanupBot()
    cleanup_botEU2 = CleanupBot()
    react_bot = ReactBot([1209138626152103946, 1234146125326454877])
    donator_bot = DonatorManagmentBot(1208219396791730226, 1216884748077498418, [1266685217578422333, 1249485247372853278, 1248751562101231657], [1209949259076739184], 1400529250204909660, [1221906406035423292, 1248721750095564871, 1248721839212204152, 1248722038336651315, 1208569460856848447])
    await asyncio.gather(
        cleanup_botEU1.start(os.getenv("SCP_SL_EU_BOT_TOKEN")),
        cleanup_botEU2.start(os.getenv("SCP_SL_EU_BOT_2_TOKEN")),
        react_bot.start(os.getenv("SCP_SL_EU_BOT_TOKEN"))
    )

if __name__ == "__main__":
    asyncio.run(run_bots())
