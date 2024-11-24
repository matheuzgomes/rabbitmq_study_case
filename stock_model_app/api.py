from ninja import NinjaAPI


class Setup:
    @staticmethod
    def api_setup(api: NinjaAPI):
        setup = NinjaAPI(title="B3 Quotation Project", openapi_url="b3/openapi")

        return setup


Setup.api_setup(NinjaAPI())