import logging


class LoggingSetup():
    # This class manages a logging file that catches and records
    # important scenarios during tests running.
    logging.basicConfig(filename=
                        r"/object_oriented_programing/pet_management_system/pet_store_management_logger.log",
                        level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s:',
                        force=True)

