#!/usr/bin/env python

import requests
import argparse
import urlparse
import logging
import sys
from dipp.orcid import __version__

logger = logging.getLogger(__name__)


def main():
    
    logger.setLevel(logging.DEBUG)
    console = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    console.setFormatter(formatter)
    logger.addHandler(console)


if __name__ == '__main__':

    logger.setLevel(logging.INFO)
    console = logging.StreamHandler()
    logger.addHandler(console)
    
    endpoint = "https://pub.orcid.org/search/orcid-bio?q=given-names:Peter+AND+family-name:Reimer"
    response = requests.get(endpoint,
                        headers = {'Accept':'application/xml'})
    if (response.status_code != 200):
        print str(response.status_code) + " " + response.text
    else:
        print response.text

