#! /usr/bin/env python
import httplib2
# These aren't needed, just for this example
from pprint import pformat

import untangle

from everett.ext.yamlfile import ConfigYamlEnv
from everett.manager import ConfigManager

config = ConfigManager([
    ConfigYamlEnv('local_config.yaml'),
])

def post_elexon(url):
    http_obj = httplib2.Http()
    resp, content = http_obj.request(
        uri=url,
        method='GET',
        headers={'Content-Type': 'application/xml; charset=UTF-8'},
    )
    print('===Response===')

    print(pformat(resp))
    print('===Content===')

    print(content.decode("utf-8"))

    # obj = untangle.parse(content.decode("utf-8"))
    # print(obj.response.responseBody)

    print('===Finished===')


def main():
    YOUR_API_KEY_HERE = config['BMRS_API_KEY']
    # post_elexon(
    #     url=f'https://api.bmreports.com/BMRS/B1770/v1?APIKey={YOUR_API_KEY_HERE}&SettlementDate=2019-01-01&Period=1&ServiceType=xml',
    # )
    FromDate = '2019-01-01 00:00:00'
    ToDate = '2019-01-02 00:00:00'
    resptype = 'csv' # <xml/XML/csv/CSV>
    post_elexon(
        url=f'https://api.bmreports.com/BMRS/ROLSYSDEM/v1?APIKey={YOUR_API_KEY_HERE}&ServiceType={resptype}',
        # url=f'https://api.bmreports.com/BMRS/ROLSYSDEM/v1?APIKey={YOUR_API_KEY_HERE}&FromDate={FromDate}&ToDate={ToDate}&ServiceType={resptype}',
    )


if __name__ == '__main__':
    main()