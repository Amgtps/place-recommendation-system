import scrapy
import pandas as pd
import numpy as np 


class HolidifySpider(scrapy.Spider):
    name = 'Holidify'
    allowed_domains = ['www.holidify.com']
    
    
    def __init__(self):
    
        cities = list(pd.read_csv("City_new.csv").city_cleaned.unique()) 
        self.start_urls = [f'https://www.holidify.com/places/{city.lower()}/sightseeing-and-things-to-do.html' for city in cities] 
        #self.start_urls = [f'https://www.holidify.com/state/gujarat/top-destinations-places-to-visit.html']
        #self.start_urls = [f'https://www.holidify.com/country/india/places-to-visit.html?pageNum=2']
        #self.start_urls = [f'https://www.holidify.com/state/{city.lower()}/' for city in cities]
        #self.start_urls = [f'https://www.holidify.com/state/{city.lower()}/top-destinations-places-to-visit.html' for city in cities]

    def parse(self, response):
        yield {
            #'state_name':response.css("div.d-flex h1::text").get()
            'state_name':response.css('div.mb-2.font-smaller b::text').get().strip(),
            'city_name':response.css('div.container.p-mobile-0 a::text').get().strip(), 
            #'rating': response.css("span.rating-badge b::text").extract() if response.css("span.rating-badge b::text").extract() else None , 
            #'name': response.css("div.card.content-card h3::text").extract() if response.css("div.card.content-card h3::text").extract() else None, 
            
            #'description': response.css("div.card-body p.card-text::text").extract() if response.css("div.card-body p.card-text::text").extract() else None,
            'best_time':response.css("div.row.no-gutters.objective-information.negative-margin-mobile div.col-12.col-md-6 p::text").extract()[4],
            'ideal_duration':response.css("div.row.no-gutters.objective-information.negative-margin-mobile div.col-12.col-md-6 p::text").extract()[3],
            
             
        }
        
        
