# import scrapy
# from scrapy_splash import SplashRequest

# class SplashPostSpider(scrapy.Spider):
#     name = "splash_post"

#     lua_script = """
#     function main(splash)
#         splash:go(splash.args.url)
#         splash:wait(1)
        
#         -- Find the <a> element by its text content
#         local a_element = splash:select('title:contains("IPTU - Não Residencial")')
        
#         -- Check if the element was found
#         if a_element then
#             -- Click the <a> element to simulate interaction
#             a_element:mouse_click()
#             splash:wait(2) -- Wait for the new page to load
            
#             -- Retrieve the HTML content of the new page
#             local html = splash:html()
            
#             -- Return the HTML content
#             return html
#         else
#             error("Unable to find the desired <a> element")
#         end
#     end
#     """

#     def start_requests(self):
#         post_url = '/index.html'
#         post_data = 'foo=bar'
#         yield SplashRequest(post_url, self.parse, 
#                             args={'lua_source': self.lua_script, 'http_method': 'POST', 'body': post_data})

#     def parse(self, response):
#         print(response)