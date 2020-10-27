from IPython.display import JSON
import json
import requests
import pandas as pd
import logging
import pathlib


# Confiugration of the search.
# this is the default HOTOSM tasking manager instance
INSTANCE = 'https://tasking-manager-tm4-production-api.hotosm.org'
# The Tasking Manager organisationId we are listing projects for
orgId = 34




def main():


    # for collecting rearch results
    results = []
    page = 1

    logging.INFO('start fetching search result pages')
    while 1:
        url = f'{INSTANCE}/api/v2/projects/?organisationId={orgId}&page={page}'
        logging.debug(f'fetching: {url}')
        resp = requests.get(url)
        resp = json.loads(resp.content)

        results += resp['results']

        # results are returned as paginated objects, so need to call the API
        # multiple times
        logging.debug(resp['pagination'])
        if resp['pagination']['hasNext']:
            page = resp['pagination']['nextNum']
        else:
            # all pages have been appended to `results`
            logging.INFO(f'projects returned by search: {len(results)}')
            break

    df = pd.DataFrame(results)
    metadatafile = f'output/tm-projects-organisationId-{orgId}.csv'
    logging.debug(f'using metadata output file: {metadatafile})
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
