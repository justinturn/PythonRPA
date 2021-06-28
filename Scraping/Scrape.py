import requests
import lxml
import cssselect
import lxml.etree
import lxml.html

start_url = f'https://www.cpspedigrees.com/poland/pigs/show/{1}'
response = requests.get(start_url)
tree = lxml.html.fromstring(response.text)

links = tree.xpath('/html/body/div[1]/div[4]/div/div[2]/div[2]')

out = []
# for link in links:
#     # we use this if just in case some <a> tags lack an href attribute
#     if 'href' in link.attrib:
#         out.append(link.attrib['href'])
