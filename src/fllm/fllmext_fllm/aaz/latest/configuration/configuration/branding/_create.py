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
    "configuration configuration branding create",
)
class Create(AAZCommand):
    """Create the branding configuration in app configuration.
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
        return None

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

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.accent_color = AAZStrArg(
            options=["--accent-color"],
            arg_group="Body",
        )
        _args_schema.accent_text_color = AAZStrArg(
            options=["--accent-text-color"],
            arg_group="Body",
        )
        _args_schema.allow_agent_selection = AAZStrArg(
            options=["--allow-agent-selection"],
            arg_group="Body",
        )
        _args_schema.background_color = AAZStrArg(
            options=["--background-color"],
            arg_group="Body",
        )
        _args_schema.company_name = AAZStrArg(
            options=["--company-name"],
            arg_group="Body",
        )
        _args_schema.fav_icon_url = AAZStrArg(
            options=["--fav-icon-url"],
            arg_group="Body",
        )
        _args_schema.kiosk_mode = AAZBoolArg(
            options=["--kiosk-mode"],
            arg_group="Body",
        )
        _args_schema.logo_text = AAZStrArg(
            options=["--logo-text"],
            arg_group="Body",
        )
        _args_schema.logo_url = AAZStrArg(
            options=["--logo-url"],
            arg_group="Body",
        )
        _args_schema.page_title = AAZStrArg(
            options=["--page-title"],
            arg_group="Body",
        )
        _args_schema.primary_button_background_color = AAZStrArg(
            options=["--primary-button-background-color"],
            arg_group="Body",
        )
        _args_schema.primary_button_text_color = AAZStrArg(
            options=["--primary-button-text-color"],
            arg_group="Body",
        )
        _args_schema.primary_color = AAZStrArg(
            options=["--primary-color"],
            arg_group="Body",
        )
        _args_schema.primary_text_color = AAZStrArg(
            options=["--primary-text-color"],
            arg_group="Body",
        )
        _args_schema.secondary_button_background_color = AAZStrArg(
            options=["--secondary-button-background-color"],
            arg_group="Body",
        )
        _args_schema.secondary_button_text_color = AAZStrArg(
            options=["--secondary-button-text-color"],
            arg_group="Body",
        )
        _args_schema.secondary_color = AAZStrArg(
            options=["--secondary-color"],
            arg_group="Body",
        )
        _args_schema.secondary_text_color = AAZStrArg(
            options=["--secondary-text-color"],
            arg_group="Body",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.UpdateBrandingConfigurations(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class UpdateBrandingConfigurations(AAZHttpOperation):
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
            return "PUT"

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
                    "Content-Type", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"client_flatten": True}}
            )
            _builder.set_prop("accentColor", AAZStrType, ".accent_color")
            _builder.set_prop("accentTextColor", AAZStrType, ".accent_text_color")
            _builder.set_prop("allowAgentSelection", AAZStrType, ".allow_agent_selection")
            _builder.set_prop("backgroundColor", AAZStrType, ".background_color")
            _builder.set_prop("companyName", AAZStrType, ".company_name")
            _builder.set_prop("favIconUrl", AAZStrType, ".fav_icon_url")
            _builder.set_prop("kioskMode", AAZBoolType, ".kiosk_mode")
            _builder.set_prop("logoText", AAZStrType, ".logo_text")
            _builder.set_prop("logoUrl", AAZStrType, ".logo_url")
            _builder.set_prop("pageTitle", AAZStrType, ".page_title")
            _builder.set_prop("primaryButtonBackgroundColor", AAZStrType, ".primary_button_background_color")
            _builder.set_prop("primaryButtonTextColor", AAZStrType, ".primary_button_text_color")
            _builder.set_prop("primaryColor", AAZStrType, ".primary_color")
            _builder.set_prop("primaryTextColor", AAZStrType, ".primary_text_color")
            _builder.set_prop("secondaryButtonBackgroundColor", AAZStrType, ".secondary_button_background_color")
            _builder.set_prop("secondaryButtonTextColor", AAZStrType, ".secondary_button_text_color")
            _builder.set_prop("secondaryColor", AAZStrType, ".secondary_color")
            _builder.set_prop("secondaryTextColor", AAZStrType, ".secondary_text_color")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            pass


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
