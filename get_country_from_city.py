def getCountryFromCityName(city):
    country = ''
    city = cleanCityName(city)
    city = urllib.parse.quote_plus(city)
    url = 'http://www.geonames.org/search.html?q={city}&country='.format(city = city)
    html = urlopen(url).read()
    getpage_soup= BeautifulSoup(html, 'html.parser')
    try:
        result_table_rows = getpage_soup.findAll('tr')[3]
        country = result_table_rows.findAll('td')[2].text
        country_list = country.split(",")
        if len(country_list) > 1:
            country = country_list[0]
    except:
        country = 'N/A'
        
    return country
