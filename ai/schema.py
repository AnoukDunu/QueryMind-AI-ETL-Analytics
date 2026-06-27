# This file tells the LLM what my database schema looks like
# This helps the LLM identify data and produce accurate results 
# LLMs aren't magic, y'know

def get_schema():
    return """
        Table: cln_products

        Description: Contains e-commerce product data including pricing, ratings and estimated revenue
        
        Columns:
        - id (integer, primary key, unique identifier for each product)
        - title (text, product name)
        - price (decimal, product price with 2 decimal precision)
        - description (text, detailed product description)
        - category (text, product category)
        - image (text, URL of product image)
        - rating_rate (float, average rating score of the product)
        - rating_count (integer, number of ratings received)
        - estimated_revenue (float, calculated revenue estimate)
        - updated_at (timestamp, last updated time of the record)
    """

