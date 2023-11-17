import glob
import logging

from pathlib import Path

from prebuilt import Extractor, TableSetter

logging.basicConfig(filename='prebuilt.log', format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG)

logger = logging.getLogger(__name__)


def insert():
    script_path = Path(__file__).parent.resolve()
    files_path = glob.glob(f"{str(script_path)}/datasets/original/*")

    files = {Path(p).stem: Path(p).name for p in files_path}

    for n in files.keys():
        # time.sleep(20)
        setter = TableSetter(api_key, files[n])
        setter.run(destination_name=f'{n}')


def ask():
    # ['products_data', 'Adidas US Sales Datasets']

    logging.info("TESTING Quality of Software:")

    extraction = Extractor(api_key,
                           "Show me the development of sales of clothing in 2021.")
    extraction.get_meta_template()
    extraction.key_word_selection()
    extraction.select_tables()

    requests = [
        "Summarize the sales of Apparel products per city, but exclude all sales that had an operating margin of less than 30%.",
        "Show the performance of the different ad spends in relation to the gender and sales.",
        "Compare the operating margins between the sales methods and list their differences per city.",
        "What the best distribution of budget between TV, Radio and Newspaper Ads is and list their ROAS?",
        "Check if there is a correlation between pay zones and the reason why people left.",
        "Give me some insights about the relation of subscription types, location, genders and devices.",
        "Are there any patterns in the job roles and the duration of employment?",
        "Analyze whether the employee performance has a relation to the frequency of termination."
    ]

    '''for customer_request in requests:

        logging.info(f"customer request: {customer_request}")

        extraction = Extractor(api_key, customer_request)
        extraction.get_meta_template()
        extraction.key_word_selection()
        extraction.select_tables()'''


if __name__ == "__main__":
    ask()
