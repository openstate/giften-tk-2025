#!/usr/bin/env python
import os
import sys
import re
from urllib.parse import urljoin

import requests
from lxml import etree
import lxml

def main(argv):
    page_url = 'https://www.rijksoverheid.nl/documenten/rapporten/2025/10/22/giften-en-schulden-van-partijen-en-kandidaten-voor-de-tweede-kamerverkiezing-2025'
    html = etree.HTML(requests.get(page_url).content)
    doc_link = [l.attrib['href'] for l in html.findall('.//a') if l.attrib['href'].endswith('.ods')]
    xpath = "//h2[contains(text(), 'Overzicht giften aan politieke partijen Tweede Kamerverkiezing 2025')]/.."
    doc_link = html.xpath(xpath)[0].get('href')
    full_doc_link = urljoin(page_url, doc_link)
    print(full_doc_link)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
