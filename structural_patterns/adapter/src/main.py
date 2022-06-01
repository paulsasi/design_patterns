import json_counter
import scraper
import adapter

if __name__ == '__main__':

    # Directly using JsonCOunter yelds to error. We need an adapter!

    # data = scraper.Scraper().get_data()
    # n_fields = json_counter.JsonCounter.compute_field_number(data)
    # print(f"The input json has {n_fields} fields")

    data_scraper = scraper.Scraper()
    data = adapter.Adapter(adaptee=data_scraper).get_data()
    n_fields = json_counter.JsonCounter.compute_field_number(data)
    print(f"The input json has {n_fields} fields")

