SPECTACULAR_SETTINGS = {
    "TITLE": "Fastwork API",
    "DESCRIPTION": "API for Fastwork",
    "VERSION": "0.9.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SERVE_PUBLIC": True,
    "COMPONENT_SPLIT_REQUEST": True,
    "SCHEMA_PATH_PREFIX_TRIM": True,
    "DEFAULT_GENERATOR_CLASS": "drf_spectacular.generators.SchemaGenerator",
    "DISABLE_ERRORS_AND_WARNINGS": False,
    # 'SECURITY_DEFINITIONS': {
    #     'tokenAuth': {
    #         'type': 'apiKey',
    #         'in': 'header',
    #         'name': 'Authorization',
    #     },
    #     'basicAuth': {
    #         'type': 'http',
    #         'scheme': 'basic',
    #     },
    #     'bearerAuth': {
    #         'type': 'http',
    #         'scheme': 'bearer',
    #     },
    # },
    # https://drf-standardized-errors.readthedocs.io/en/latest/openapi.html#integration-wth-drf-spectacular
    "ENUM_NAME_OVERRIDES": {
        "ValidationErrorEnum": "drf_standardized_errors.openapi_serializers.ValidationErrorEnum.choices",
        "ClientErrorEnum": "drf_standardized_errors.openapi_serializers.ClientErrorEnum.choices",
        "ServerErrorEnum": "drf_standardized_errors.openapi_serializers.ServerErrorEnum.choices",
        "ErrorCode401Enum": "drf_standardized_errors.openapi_serializers.ErrorCode401Enum.choices",
        "ErrorCode403Enum": "drf_standardized_errors.openapi_serializers.ErrorCode403Enum.choices",
        "ErrorCode404Enum": "drf_standardized_errors.openapi_serializers.ErrorCode404Enum.choices",
        "ErrorCode405Enum": "drf_standardized_errors.openapi_serializers.ErrorCode405Enum.choices",
        "ErrorCode406Enum": "drf_standardized_errors.openapi_serializers.ErrorCode406Enum.choices",
        "ErrorCode415Enum": "drf_standardized_errors.openapi_serializers.ErrorCode415Enum.choices",
        "ErrorCode429Enum": "drf_standardized_errors.openapi_serializers.ErrorCode429Enum.choices",
        "ErrorCode500Enum": "drf_standardized_errors.openapi_serializers.ErrorCode500Enum.choices",
    },
    "POSTPROCESSING_HOOKS": [
        "drf_standardized_errors.openapi_hooks.postprocess_schema_enums"
    ],
}
