"""
Zero-Clause BSD

Permission to use, copy, modify, and/or distribute this software for any
urpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING
FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
"""

"""
Usage:

Configure of the search parameters below (INSTANCE and ORG_ID)
and call this script without any arguments. output will be written to ./output
relative to your working directory (the directory is created if missing).
Existing files are over written.
"""

# this is the default HOTOSM tasking manager instance
INSTANCE = 'https://tasking-manager-tm4-production-api.hotosm.org'
# The Tasking Manager organisationId we are listing projects for
ORG_ID = 34


import json
import requests
import pandas as pd
import logging
import pathlib


def main():
    # for collecting rearch results
    results = []
    page = 1

    logging.info('start fetching search result pages')
    while 1:
        url = f'{INSTANCE}/api/v2/projects/'
        params = {
            'organisationId': ORG_ID,
            'page': page,
            'projectStatuses': "ARCHIVED,PUBLISHED,DRAFT"
        }
        logging.debug(f'fetching: {url}, {params}')
        resp = requests.get(url, params=params)
        resp = json.loads(resp.content)

        results += resp['results']

        # results are returned as paginated objects, so need to call the API
        # multiple times
        logging.debug(resp['pagination'])
        if resp['pagination']['hasNext']:
            page = resp['pagination']['nextNum']
        else:
            # all pages have been appended to `results`
            logging.info(f'projects returned by search: {len(results)}')
            break

    df = pd.DataFrame(results)
    metadatafile = f'output/tm-projects-organisationId-{ORG_ID}.csv'
    logging.debug(f'using metadata output file: {metadatafile}')
    df.to_csv(metadatafile)


    projectIds = list(map(lambda results: results['projectId'], results))

    for projectId in projectIds:
        logging.debug(f'fetching geometry for project: {projectId}')
        resp = requests.get(f'{INSTANCE}/api/v2/projects/{projectId}/')
        geo = json.loads(resp.content)
        f = open(f'output/{projectId}.geojson', 'w')
        f.write(json.dumps(geo, indent=2))
        f.close()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('script started')
    output_dir = './output'
    logging.info(f'using: {output_dir}')
    pathlib.Path(output_dir).mkdir(parents=True, exist_ok= True)
    main()
