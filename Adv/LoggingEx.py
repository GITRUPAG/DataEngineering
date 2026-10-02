import logging

logging.basicConfig(filename= "app.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s"
                    )

logging.info("Processing file")

logging.error("Database connection failed")

logging.warning("File is large")

# Logging levels

# Debug
# info
# warning
# error
# critical

logging.debug("DEbugging!!!")

logging.info("Info")

data = [1, 2, 3, 4, 5]

logging.info(
    "Extracted %d records", len(data)
)

data = [
    {"name": "Ravi", "age": None}
]

for record in data:
    if record["age"] is None:
        logging.warning("Missing age for %s", record["name"])


try:
    result = 10/0
except Exception as e:
    logging.error(type(e))


