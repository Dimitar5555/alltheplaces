from locations.storefinders.rio_seo import RioSeoSpider


class AirgasUSSpider(RioSeoSpider):
    name = "airgas_us"
    item_attributes = {"brand": "Airgas", "brand_wikidata": "Q80635"}
    allowed_domains = ["locations.airgas.com"]
    start_urls = [
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Kansas%20City,%20KS,%20US&radius=400&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Seattle,%20WA,%20US&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Alabama&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Alaska&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Arizona&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Arkansas&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=California&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Colorado&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Connecticut&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Delaware&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Florida&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Georgia&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Hawaii&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Idaho&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Illinois&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Indiana&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Iowa&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Kansas&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Kentucky&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Louisiana&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Maine&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Maryland&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Massachusetts&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Michigan&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Minnesota&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Mississippi&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Missouri&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Montana&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Nebraska&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Nevada&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=New%20Hampshire&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=New%20Jersey&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=New%20Mexico&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=New%20York&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=North%20Carolina&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=North%20Dakota&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Ohio&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Oklahoma&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Oregon&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Pennsylvania&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Rhode%20Island&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=South%20Carolina&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=South%20Dakota&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Tennessee&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Texas&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Utah&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Vermont&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Virginia&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Washington&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=West%20Virginia&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Wisconsin&radius=1000&limit=1000",
        "https://maps.locations.airgas.com/api/getAsyncLocations?template=search&level=search&search=Wyoming&radius=1000&limit=1000",
    ]
