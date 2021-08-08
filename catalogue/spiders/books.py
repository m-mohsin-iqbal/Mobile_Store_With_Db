import json
import scrapy
import csv
import os.path
import json


class MiodottoreSpider(scrapy.Spider):
    name = 'mobilestore'
    title = 'mobilestore'
    base_url = 'https://mobilestore.co.za/'
    template_url = 'https://mobilestore.co.za'
    start_urls = [
        "https://mobilestore.co.za/telkom",
        "https://www.mobilestore.co.za/mtn",
        "https://mobilestore.co.za/vodacom"
    ]
    active_page = None
    filter = None

    @classmethod
    def clean_data(cls, data):
        if data and isinstance(data, str):
            data = data.encode('ascii', 'ignore').decode()
        return data

    @classmethod
    def get_index(cls, lst, index, default=''):
        """
        return element on given index from list
        :param lst: list from which we will return element
        :param index: index of element
        :param default: return value if index out of range
        :return:
        """
        return cls.clean_data(lst[index]) if isinstance(lst, list) and len(lst) > index else default

    def get_dict_value(self, data, key_list, default=''):
        """
        gets a dictionary and key_list, apply key_list sequentially on dictionary and return value
        :param data: dictionary
        :param key_list: list of key
        :param default: return value if key not found
        :return:
        """
        for key in key_list:
            if data and isinstance(data, dict):
                data = data.get(key, default)
            elif data and isinstance(data, list):
                data = self.get_index(data, key) if isinstance(key, int) else default
            else:
                return default
        return self.clean_data(data)

    def start_requests(self):
        for each_url in self.start_urls:
            self.filter = None
            yield scrapy.Request(url=each_url, dont_filter=True,
                                 meta={"filter": self.get_index(each_url.split("/"), -1), 'first': True})

    def parse(self, response):
        my_filter = response.url.split("/")[3]
        if "?&" in my_filter:
            my_filter = self.get_index(my_filter.split("?&"),0)

        for each in response.css('.dealsWrap a'):
            self.active_page = None
            item = dict()
            item['imageUrl'] = each.css(".dealImg img::attr(src)").get()
            item['ProviderLogo'] = each.css(".logo::attr(src)").get()
            item['brand'] = self.get_index(each.css("h2::text").get().split(" "), 0)
            item['model'] = ",".join(each.css("h2::text").get().split(" ")[1:])
            item['phoneDescription'] = each.css("h3 span::text").get()
            item['phoneDescription2'] = each.css("h3 span+span::text").get()
            item['packageDetail'] = ''.join(each.css("h4::text").getall()).replace(" ", "").replace("\r", '').replace(
                "\n", ' ')
            item['packageName'] = each.css(".packageDetails .badge::text").get()
            item['price'] = each.css(".dataPrice strong::text").get() + ' ' + each.css(".dataPrice small::text").get()
            item['Url'] = '{}{}'.format(self.template_url,each.css("::attr(href)").get())
            if 'Sim,Card' in item['model']:
                continue
            # save data  into csv file
            filename = 'data.csv'
            file_exists = os.path.isfile(filename)

            with open(filename, 'a', encoding="utf-8") as csvfile:
                headers = item.keys()
                writer = csv.DictWriter(csvfile, delimiter=',',
                                        lineterminator='\n',
                                        fieldnames=headers)

                if not file_exists:
                    writer.writeheader()  # file doesn't exist yet, write a header
                writer.writerow(item)

            # save data into json file
            with open("data.json", "a") as outfile:
                json.dump(item, outfile)
            yield item

        print("page", response.css(".active a::text").get())
        if response.css(".active a::text").get():
            active_page = response.css(".active a::text").get()
            # print("Active page: ", active_page)
            next_page = response.css(".active+li a::attr(href)").get()
            # print("next ",next_page)
            if next_page:
                print(self.base_url)
                print(my_filter)
                print(next_page)
                url = self.base_url+my_filter+"?&"+next_page
                print("url:  ", url)
                yield scrapy.Request(url=url, callback=self.parse)
