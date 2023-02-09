Task_1 
    file instructions:
    
        - Open a terminal and naviagete to the test.py file
        - Run the file
        - The feed.xml file will be generated
        
    Explanation:
        - The code bit that intiates the process is at the end of the test.py file,
        it establish the connection with the data.sqlite database fetches the products,
        Create product objects and then organise them in a dictionary, that finally will create the feed.xml
        - fetch products function() will extract raw data from the product tabel to intiate the products objects creation
        - the Product Class has a constructor and helper functions that will fetch the remaining information from
        the other tables.
        - the generate_xml() function generates the XML tree and populates it using the product objects acording to Google Merchant product data specifications
