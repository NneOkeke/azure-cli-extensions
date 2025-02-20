# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "apic api definition import-specification",
)
class ImportSpecification(AAZCommand):
    """Imports the API specification.

    :example: Import specification example 1
        az apic api definition import-specification -g api-center-test -n contosoeuap --api-id echo-api-2 --version-id 2023-08-01 --definition-id openapi3 --format "inline" --value '{"openapi":"3.0.1","info":{"title":"httpbin.org","description":"API Management facade for a very handy and free online HTTP tool.","version":"1.0"}}' --specification '{"name":"openapi","version":"3.0.0"}'

    :example: Import specification example 2
        az apic api definition import-specification -g api-center-test -n contoso --api-id echo-api --version-id 2023-11-01 --definition-id openapi --format "link" --value 'https://petstore3.swagger.io/api/v3/openapi.json' --specification '{"name":"openapi","version":"3.0.0"}'

    :example: Import specification from file example
        az apic api definition import-specification -g api-center-test -n contosoeuap --api-id echo-api --version-id 2023-08-01 --definition-id openapi --format "inline" --value '@petstore.json'
    """

    _aaz_info = {
        "version": "2024-03-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.apicenter/services/{}/workspaces/{}/apis/{}/versions/{}/definitions/{}/importspecification", "2024-03-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, None)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.api_id = AAZStrArg(
            options=["--api-id"],
            help="The id of the API.",
            required=True,
            id_part="child_name_2",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]{3,90}$",
                max_length=90,
                min_length=1,
            ),
        )
        _args_schema.definition_id = AAZStrArg(
            options=["--definition-id"],
            help="The id of the API definition.",
            required=True,
            id_part="child_name_4",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]{3,90}$",
                max_length=90,
                min_length=1,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.service_name = AAZStrArg(
            options=["-n", "--service-name"],
            help="The name of Azure API Center service.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]{3,90}$",
                max_length=90,
                min_length=1,
            ),
        )
        _args_schema.version_id = AAZStrArg(
            options=["--version-id"],
            help="The id of the API version.",
            required=True,
            id_part="child_name_3",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]{3,90}$",
                max_length=90,
                min_length=1,
            ),
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["-w", "--workspace", "--workspace-name"],
            help="The name of the workspace.",
            required=True,
            id_part="child_name_1",
            default="default",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]{3,90}$",
                max_length=90,
                min_length=1,
            ),
        )

        # define Arg Group "Payload"

        _args_schema = cls._args_schema
        _args_schema.format = AAZStrArg(
            options=["--format"],
            arg_group="Payload",
            help="Format of the API specification source.",
            enum={"inline": "inline", "link": "link"},
        )
        _args_schema.specification = AAZObjectArg(
            options=["--specification"],
            arg_group="Payload",
            help="API specification details.",
        )
        _args_schema.value = AAZStrArg(
            options=["--value"],
            arg_group="Payload",
            help="Value of the API specification source.",
        )

        specification = cls._args_schema.specification
        specification.name = AAZStrArg(
            options=["name"],
            help="Specification name.",
        )
        specification.version = AAZStrArg(
            options=["version"],
            help="Specification version.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.ApiDefinitionsImportSpecification(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class ApiDefinitionsImportSpecification(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiCenter/services/{serviceName}/workspaces/{workspaceName}/apis/{apiName}/versions/{versionName}/definitions/{definitionName}/importSpecification",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "apiName", self.ctx.args.api_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "definitionName", self.ctx.args.definition_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "serviceName", self.ctx.args.service_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "versionName", self.ctx.args.version_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-03-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("format", AAZStrType, ".format")
            _builder.set_prop("specification", AAZObjectType, ".specification")
            _builder.set_prop("value", AAZStrType, ".value")

            specification = _builder.get(".specification")
            if specification is not None:
                specification.set_prop("name", AAZStrType, ".name")
                specification.set_prop("version", AAZStrType, ".version")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            pass


class _ImportSpecificationHelper:
    """Helper class for ImportSpecification"""


__all__ = ["ImportSpecification"]
