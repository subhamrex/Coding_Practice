import bs4,requests

def get_price_from_amazon(geturl):
    rs = requests.get(geturl)
    rs.raise_for_status()
    soup = bs4.BeautifulSoup(rs.text,"html.parser")
    ele = soup.select('#merchandised-content > div.a-section.octopus-pc-card.octopus-best-seller-card > div.a-section.octopus-pc-card-content > ul > li:nth-child(2) > span > div > a > div.a-section.octopus-pc-asin-info-section > div.a-section.a-spacing-none.octopus-pc-asin-price-section > div.a-section.octopus-pc-asin-price > span > span:nth-child(2) > span.a-price-whole')
    return ele[0].text.strip()

price = get_price_from_amazon("https://www.amazon.in/s/ref=lp_1389401031_nr_n_1?fst=as%3Aoff&rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389432031&bbn=1389401031&ie=UTF8&qid=1602680700&rnid=1389401031")
print(price)