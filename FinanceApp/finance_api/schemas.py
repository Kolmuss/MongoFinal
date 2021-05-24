import coreapi
from rest_framework.schemas import AutoSchema


class CurrencySchema(AutoSchema):
    def get_manual_fields(self, path, method):
        if method.lower() in ["post", ]:
            extra_fields = [
                coreapi.Field('name', location='query', description='name'),
                coreapi.Field('code', location='query', description='code'),
                coreapi.Field('symbol', location='query', description='symbol'),
                coreapi.Field('rate', location='query', description='rate'),

                coreapi.Field('created_at', location='query', description='created_at'),
                coreapi.Field('updated_at', location='query', description='updated_at'),
                coreapi.Field('deleted_at', location='query', description='deleted_at'),
            ]

            manual_fields = super().get_manual_fields(path, method)
            return manual_fields + extra_fields


# class CategorySchema(AutoSchema):
#     def get_manual_fields(self, path, method):
#         if method.lower() in ["post", ]:
#             extra_fields = [
#                 coreapi.Field('title', type='string', location='query', description='name'),
#                 coreapi.Field('user', type='string', location='query', description='code'),
#                 coreapi.Field('code', type='string', location='query', description='symbol'),
#
#                 coreapi.Field('created_at', type='timestamp', location='query', description='created_at'),
#                 coreapi.Field('updated_at', type='timestamp', location='query', description='updated_at'),
#                 coreapi.Field('deleted_at', type='timestamp', location='query', description='deleted_at'),
#             ]
#
#             manual_fields = super().get_manual_fields(path, method)
#             return manual_fields + extra_fields
