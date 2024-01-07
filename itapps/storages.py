from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = "c1008080dcbs"
    account_key = "0SviVshYybYnF1Fkv5AnFRVBRwUlkfK2XiRUj6Ihib4tJjTYSGgMvI9OsdQMDJac266cWiNT9eJx+ASt7J700g=="
    azure_container = "media"
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = "c1008080dcbs"
    account_key = "0SviVshYybYnF1Fkv5AnFRVBRwUlkfK2XiRUj6Ihib4tJjTYSGgMvI9OsdQMDJac266cWiNT9eJx+ASt7J700g=="
    azure_container = "static"
    expiration_secs = None
    