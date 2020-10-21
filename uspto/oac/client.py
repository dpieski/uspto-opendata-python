# -*- coding: utf-8 -*-
# (c) 2019 Andrew Piechocki <apiechocki@dunlapcodding.com>
import logging
from uspto.oac.document import UsptoOfficeActionCitationsDocument
from uspto.util.client import UsptoGenericBulkDataClient, download_and_print

logger = logging.getLogger(__name__)

class UsptoOfficeActionCitationsClient(UsptoGenericBulkDataClient):
    """
    Python client for accessing the USPTO Office Action Citations API V2 (https://developer.uspto.gov/ds-api/oa_citations/v2/).
    See also: https://developer.uspto.gov/api-catalog/uspto-office-action-citations-api
    """
    DATASOURCE_NAME      = 'oac'

    QUERY_URL            = 'https://ped.uspto.gov/api/queries'
    PACKAGE_REQUEST_URL  = 'https://ped.uspto.gov/api/queries/{query_id}/package?format={format}'
    PACKAGE_STATUS_URL   = 'https://ped.uspto.gov/api/queries/{query_id}?format={format}'
    PACKAGE_DOWNLOAD_URL = 'https://ped.uspto.gov/api/queries/{query_id}/download?format={format}'

    document_factory     = UsptoOfficeActionCitationsDocument


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    client = UsptoOfficeActionCitationsClient()

    # Published applications by publication number
    # US2017293197A1: appEarlyPubNumber:(US2017293197A1)
    download_and_print(client, number='US2017293197A1', type='publication')
    #download_and_print(client, number='US2017293197A1')
    #download_and_print(client, number='2017/0293197')  # No results

    # Published applications by application number
    # US2017293197A1: applId:(15431686)
    #download_and_print(client, number='15431686')

    # Granted patents by patent number
    #download_and_print(client, number='PP28532')
    #download_and_print(client, number='9788906')
    #download_and_print(client, number='D799980')
    #download_and_print(client, number='RE46571')
    #download_and_print(client, number='3525666')           # No results

    # Deleted: US11673P
    #download_and_print(client, number='PP11673')           # No results
