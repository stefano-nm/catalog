from .catalog_base import CatalogBase
from .utils import get


class Catalog(CatalogBase):
    def __init__(self, *args, **kwargs):
        CatalogBase.__init__(self, *args, object_name="Service", **kwargs)

    @get
    def catalog(self, **kwargs):
        return self._catalog(**kwargs)

    @get
    def service(self, **kwargs):
        return self._object(**kwargs)
