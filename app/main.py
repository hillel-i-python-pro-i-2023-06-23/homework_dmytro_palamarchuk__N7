"""Module homework #5"""

from dotenv import load_dotenv

from app.loggers.loggers import get_core_logger
from app.loggers.init_logging import init_logging
from app.data_provider import DataProvider
from app.data_processing import organize_data, get_formatted_output


def main() -> None:
    """Main entry point"""

    # Upload dotenv configuration
    load_dotenv()
    # Initialize logging
    init_logging()

    logger = get_core_logger()

    logger.info("Application Starting")

    group_members = DataProvider().generate_group_members()
    organized_data = organize_data(humans=group_members)
    output = get_formatted_output(data=organized_data)
    print(output)

    logger.info("Application Finished")
