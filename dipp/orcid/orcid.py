#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import argparse
import urlparse
import logging
import sys
import json
from resources import ACTIVITIES, BIO, WORKS, PROFILE

logger = logging.getLogger(__name__)

endpoint = "pub.orcid.org/v1.2"

class Client:
    
    def __init__(self, endpoint):
        
        self.endpoint = endpoint

    def _make_rest_uri(self, resource, query="", orcid_id=None):
        """create the uri for the restfull webservice of orcid"""
    
        if orcid_id:
            path = '/'.join((orcid_id, resource))
        else:
            path = resource
        
        if not self.endpoint:
            logger.error('No valid endpoint specified.')
            rest_uri = None
        else:
            rest_uri = urlparse.urlunparse(('https', self.endpoint, path, '', query, ''))
        logger.debug("REST URI %s" % rest_uri)
        return rest_uri


    def read(self, resource, orcid_id):
        
        uri = self._make_rest_uri(resource, orcid_id=orcid_id)
        response = requests.get(uri, headers = {'Accept':'application/json'})
        
        if (response.status_code != 200):
            return str(response.status_code) + " " + response.text
        else:
            return response.text

    def search(self, **kwargs):
        
        firstName = kwargs.get('firstName', None)
        lastName = kwargs.get('lastName', None)
                
        if firstName and lastName:
            query = "q=given-names:%s+AND+family-name:%s" % (firstName, lastName)
        else:
            query = ''
        
        resource = "/".join(("search", BIO))
        uri = self._make_rest_uri(resource, query=query, orcid_id=None)
        response = requests.get(uri, headers = {'Accept':'application/json'})
        
        if (response.status_code != 200):
            return str(response.status_code) + " " + response.text
        else:
            return response.text


def main():
    
    logger.setLevel(logging.INFO)
    console = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    console.setFormatter(formatter)
    logger.addHandler(console)

    parser = argparse.ArgumentParser(description='Basic use of orcids public webservice')
    parser.add_argument('resource', help='Resource')
    parser.add_argument('-o', '--orcidid', help='orcid ID')
    parser.add_argument('-f', '--firstname', help='Authors given name.')
    parser.add_argument('-l', '--lastname', help='Authors family name.')
    parser.add_argument('-v', '--version', action="store_true", help='Print version number and exit')

    args = parser.parse_args()
    
    resources = {
        "bio":BIO,
        "works":WORKS,
        "profile":PROFILE
    }
    resource = resources[args.resource]
    client = Client(endpoint)
    
    if args.orcidid:
        print client.read(resource, orcid_id=args.orcidid).encode(encoding="utf-8")
        sys.exit(0)
    
    if args.firstname and args.lastname:
        print client.search(firstName=args.firstname, lastName=args.lastname)
        sys.exit(0)

if __name__ == '__main__':

    logger.setLevel(logging.DEBUG)
    console = logging.StreamHandler()
    logger.addHandler(console)
    orcid_id= "0000-0002-3187-2536"
    # endpoint = "https://pub.orcid.org/v1.2/search/orcid-bio?q=given-names:Peter+AND+family-name:Reimer"

    client = Client(endpoint)
    
    print client.read(WORKS, orcid_id="0000-0002-3187-2536")
    
    # print client.read(BIO, orcid_id="0000-0002-3187-2536")
    #print client.search(firstName="Peter", lastName="Reimer")
    
