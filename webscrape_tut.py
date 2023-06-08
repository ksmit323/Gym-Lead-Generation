from bs4 import BeautifulSoup
import requests
import re

## Video 1
# url  = "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080gaming-oc-10gd/p/N82E16814932329"

# result = requests.get(url)
# doc = BeautifulSoup(result.text, "html.parser")

# prices = doc.find_all(string="$")
# parent = prices[0].parent
# strong = parent.find("strong")
# print(strong.string)


# ## Video 2
# with open("index2.html") as f:
#     doc = BeautifulSoup(f, "html.parser")

# tags = doc.find_all(['option'], string='Undergraduate', value='undergraduate')
# tags = doc.find_all(class_="btn-item")

# # Regular Expression
# tags = doc.find_all(string=re.compile('\$.*'))

# tags = doc.find_all('input', type='text')
# for tag in tags:
#     tag['placeholder'] = 'I changed you!'

# with open('changed.html', 'w') as file:
#     file.write(str(doc))

# ## Video 3
# url = 'https://coinmarketcap.com/'
# result = requests.get(url).text
# doc = BeautifulSoup(result, "html.parser")

# tbody = doc.tbody
# trs = tbody.contents

# trs[1].previous_sibling
# trs[0].next_siblings
# trs[0].parent
# trs[0].descendants
# trs[0].content

# prices = {}

# for tr in trs[:10]:
#     name, price = tr.contents[2:4]
#     fixed_name = name.p.string
#     fixed_price = price.a.string

#     prices[fixed_name] = fixed_price

# print(prices)


## Video 4
gpu = 3080

url = f"https://www.newegg.com/p/pl?d={gpu}"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split('/')[-2].split('>')[-1][:-1])

items_found = {}

for page in range(1, pages + 1):
    url = f"https://www.newegg.com/p/pl?d={gpu}&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    div = doc.find(class_='item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell')
    items = div.find_all(string=re.compile(gpu))

    for item in items:
        parent = item.parent
        if parent.name != 'a':
            continue

        link = parent['href']
        next_parent = item.find_parent(class_='item-container')

        try:
            price = next_parent.find(class_="price-current").strong.string
            items_found[item] = {'price': int(price.replace(",","") ), 'link': link}
        except:
            pass


sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

for item in sorted_items:
    print(item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])
    print('---------------------')
