.. flipkart scrapper documentation master file, created by
   sphinx-quickstart on Sat Jun  1 21:37:12 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to flipkart scrapper's documentation!
=============================================

This documentation is based on scrapy module in python3.

In this project we will scrape the data of laptops like name, rating, price from flipkart website.

Introduction: scrapy
____________________

Scrapy is an application framework for crawling web sites and extracting structured data which can be used for a wide range of useful applications, like data mining, information processing or historical archival.

prerequisites:
______________

---python3

---scrapy



Getting started:
________________

To start with build a new project folder in your home directory. Now open this directory in your terminal and enter the command:

.. code-block:: ruby


   $  scrapy startproject tutorial
   


this command creates a directory named tutorial with the following contents:


tutorial/
    scrapy.cfg                          # deploy configuration file

    tutorial/                           # project's Python module, you'll import your code from here
        __init__.py

        items.py                        # project items definition file

        middlewares.py                  # project middlewares file

        pipelines.py                    # project pipelines file

        settings.py                     # project settings file

        spiders/                        # a directory where you'll later put your spiders
            __init__.py 



The spider code:
________________

Open the spiders folder and create a new python project. copy the following code in it. (the code is self explanatory)

.. code-block:: python

    
     import scrapy
     import pickle
     from ..items import FlipcartScrapyItem

     class myspider(scrapy.Spider):
	     page_plus = 2
	     name = 'spidy'
	     start_urls = [
		      'https://www.flipkart.com/search?q=laptops&otracker=AS_Query_HistoryAutoSuggest_0_0&otracker1=AS_Query_HistoryAutoSuggest_0_0&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY&as-searchtext=laptops&page=1'
	     ] 
	
	     def parse(self, response):
		     items  = FlipcartScrapyItem()
		     box = response.css('div.bhgxx2.col-12-12')
		     for entries in box :
			     title = entries.css('div._3wU53n::text').extract()
			     rating = entries.css('div.hGSR34::text').extract()
			     price = entries.css('div._1vC4OE._2rQ-NK::text').extract()

			     items['title'] = title
			     items['rating'] = rating
			     items['price'] = price

		             yield  items
		
		     next_page = 'https://www.flipkart.com/search?q=laptops&otracker=AS_Query_HistoryAutoSuggest_0_0&otracker1=AS_Query_HistoryAutoSuggest_0_0&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY&as-searchtext=laptops&page=" + str(myspider.page_plus) + "'
	   	     if myspider.page_plus <= 11:
			     myspider.page_plus +=1
			     yield response.follow(next_page,callback = self.parse
Items.py:
_________

Now open the items.py file and create the following objects.

.. code-block:: python


    # -*- coding: utf-8 -*-

    # Define here the models for your scraped items
    #
    # See documentation in:
    # https://doc.scrapy.org/en/latest/topics/items.html

    import scrapy


    class FlipcartScrapyItem(scrapy.Item):
        # define the fields for your item here like:
        # name = scrapy.Field()
	    title = scrapy.Field()
	    rating = scrapy.Field()
	    price = scrapy.Field()
    
Spider crawling:
________________

open your root directory in terminal and enter the following command:

.. code-block:: ruby

   $  scrapy crawl spidy -o result.pickle

  (spidy is the name we have given to the spider in the spider code)


This command creartes a result.pickle file in your root directory.
you can also use .csv and .json file formats.

The result:
___________

The spider crawled 10 pages and extracted data of around 150 laptops.

here is the data extracted.

.. image:: /image/image1.png

.. image:: /image/image2.png

.. image:: /image/image3.png

.. image:: /image/image4.png

.. note:: The no of laptops to be scraped can be controlled by changing the page no limit in the spider code.

.. 

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
