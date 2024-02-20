# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from foundationallm.cli.core.aaz import *


@register_command(
    "configuration configuration branding show",
)
class Show(AAZCommand):
    """Get the branding configuration from app configuration.
    """

    _aaz_info = {
        "version": "2024-02-16",
        "resources": [
            ["fllm-plane", "/instances/{}/providersx/foundationallm.configuration/configurations/branding", "2024-02-16"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.instance_id = AAZStrArg(
            options=["--instance-id"],
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.GetBrandingConfigurations(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class GetBrandingConfigurations(AAZHttpOperation):
        CLIENT_TYPE = "FllmClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/instances/{instanceId}/providersX/FoundationaLLM.Configuration/configurations/branding",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "instanceId", self.ctx.args.instance_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-02-16",
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.accent_color = AAZStrType(
                serialized_name="accentColor",
            )
            _schema_on_200.accent_text_color = AAZStrType(
                serialized_name="accentTextColor",
            )
            _schema_on_200.allow_agent_selection = AAZStrType(
                serialized_name="allowAgentSelection",
            )
            _schema_on_200.background_color = AAZStrType(
                serialized_name="backgroundColor",
            )
            _schema_on_200.company_name = AAZStrType(
                serialized_name="companyName",
            )
            _schema_on_200.fav_icon_url = AAZStrType(
                serialized_name="favIconUrl",
            )
            _schema_on_200.kiosk_mode = AAZBoolType(
                serialized_name="kioskMode",
            )
            _schema_on_200.logo_text = AAZStrType(
                serialized_name="logoText",
            )
            _schema_on_200.logo_url = AAZStrType(
                serialized_name="logoUrl",
            )
            _schema_on_200.page_title = AAZStrType(
                serialized_name="pageTitle",
            )
            _schema_on_200.primary_button_background_color = AAZStrType(
                serialized_name="primaryButtonBackgroundColor",
            )
            _schema_on_200.primary_button_text_color = AAZStrType(
                serialized_name="primaryButtonTextColor",
            )
            _schema_on_200.primary_color = AAZStrType(
                serialized_name="primaryColor",
            )
            _schema_on_200.primary_text_color = AAZStrType(
                serialized_name="primaryTextColor",
            )
            _schema_on_200.secondary_button_background_color = AAZStrType(
                serialized_name="secondaryButtonBackgroundColor",
            )
            _schema_on_200.secondary_button_text_color = AAZStrType(
                serialized_name="secondaryButtonTextColor",
            )
            _schema_on_200.secondary_color = AAZStrType(
                serialized_name="secondaryColor",
            )
            _schema_on_200.secondary_text_color = AAZStrType(
                serialized_name="secondaryTextColor",
            )

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]