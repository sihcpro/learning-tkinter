from os import getenv

CRAW_EVERY_SECONDS = int(getenv("CRAW_EVERY_SECONDS", 0))

SOF_NUM_OF_PAGE = int(getenv("SOF_NUM_OF_PAGE", 3))
SOF_PAGE_SIZE = int(getenv("SOF_PAGE_SIZE", 15))

SOF_URL = getenv("SOF_URL", None)
SOF_INDEX_COLUMN = getenv("SOF_INDEX_COLUMN", "No")
SOF_OUTPUT_FILENAME = getenv("SOF_OUTPUT_FILENAME", None)
