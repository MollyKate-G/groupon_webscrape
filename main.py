import requests
from bs4 import BeautifulSoup

url = "https://www.groupon.com/?&utm_source=google&utm_medium=cpc&utm_campaign=us_dt_sea_ggl_txt_naq_sr_cbp_ch1_ybr_k*groupon_m*e_d*groupon-brand_g*groupon-exact_c*535923351489_ap*&gclid=CjwKCAjwrNmWBhA4EiwAHbjEQOq95WU3Bh0mqSuwmFZ3RSXZF6XGxzvzXMCwnNn_eBy5eMeN5fW9JxoC468QAvD_BwE"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")



groupon_deal = []

deal_cards = soup.find_all('div', class_='cui-content')

for sale in deal_cards:
    name = sale.find('div', class_="cui-udc-title one-line-truncate")
    if not name:
        continue
    if name:
        name = name.text.strip()

    address = sale.find('span', class_='cui-location-name')
    if address:
        address = address.text.strip()

    star_rating = sale.find('div', class_='numeric-count')
    if star_rating:
        star_rating = star_rating.text.strip()

    reviews = sale.find('div', class_='rating-count')
    if reviews:
        reviews = reviews.text.strip()

    regular_price = sale.find('div', class_='cui-price-original c-txt-gray-dk')
    if regular_price:
        regular_price = regular_price.text.strip()

    discount_price = sale.find('div', class_='cui-price-discount c-txt-price')
    if discount_price:
        discount_price = discount_price.text.strip()

    elif discount_price == "None":
        sale.find('div', class_='cui-verbose-urgency-price')
        discount_price = discount_price.text.strip()

    description = sale.find('div', class_='cui-udc-subtitle one-line-truncate')
    if description:
        description = description.text.strip()

    groupon_deal.append({
        'name':name,
        'address': address,
        'star_rating': star_rating,
        'reviews': reviews,
        'regular_price': regular_price,
        'discount_price': discount_price,
        'description': description
    })    


# print(groupon_deal)

for sale in groupon_deal:
    print(f"{sale['name']}\nLocation: {sale['address']}\nStar Rating: {sale['star_rating']} | Reviews: {sale['reviews']}\nRegular Price: {sale['regular_price']} | Discount Price: {sale['discount_price']}\nDescription - {sale['description']}\n")
    
