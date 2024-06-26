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
    "agent list",
)
class List(AAZCommand):
    """list
    """

    _aaz_info = {
        "version": "2024-02-16",
        "resources": [
            ["fllm-plane", "/instances/{}/providers/foundationallm.agent/agents", "2024-02-16"],
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
        self.AgentsList(ctx=self.ctx)()
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

    class AgentsList(AAZHttpOperation):
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
                "/instances/{instanceId}/providers/FoundationaLLM.Agent/agents",
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

            cls._schema_on_200 = AAZListType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.Element = AAZObjectType()

            _element = cls._schema_on_200.Element
            _element.conversation_history = AAZObjectType()
            _element.created_by = AAZStrType()
            _element.created_on = AAZObjectType()
            _element.deleted = AAZBoolType()
            _element.description = AAZStrType()
            _element.display_name = AAZStrType()
            _element.gatekeeper = AAZObjectType()
            _element.language_model = AAZObjectType()
            _element.name = AAZStrType()
            _element.object_id = AAZStrType()
            _element.orchestration_settings = AAZObjectType()
            _element.prompt_object_id = AAZStrType()
            _element.sessions_enabled = AAZBoolType()
            _element.type = AAZStrType()
            _element.updated_by = AAZStrType()
            _element.updated_on = AAZObjectType()

            conversation_history = cls._schema_on_200.Element.conversation_history
            conversation_history.enabled = AAZBoolType()
            conversation_history.max_history = AAZIntType()

            gatekeeper = cls._schema_on_200.Element.gatekeeper
            gatekeeper.options = AAZListType()
            gatekeeper.use_system_setting = AAZBoolType()

            options = cls._schema_on_200.Element.gatekeeper.options
            options.Element = AAZStrType()

            language_model = cls._schema_on_200.Element.language_model
            language_model.api_endpoint = AAZStrType()
            language_model.api_key = AAZStrType()
            language_model.api_version = AAZStrType()
            language_model.deployment = AAZStrType()
            language_model.provider = AAZStrType()
            language_model.temperature = AAZFloatType()
            language_model.type = AAZStrType()
            language_model.use_chat = AAZBoolType()
            language_model.version = AAZStrType()

            orchestration_settings = cls._schema_on_200.Element.orchestration_settings
            orchestration_settings.agent_parameters = AAZDictType()
            orchestration_settings.endpoint_configuration = AAZDictType()
            orchestration_settings.model_parameters = AAZDictType()
            orchestration_settings.orchestrator = AAZStrType()

            agent_parameters = cls._schema_on_200.Element.orchestration_settings.agent_parameters
            agent_parameters.Element = AAZStrType()

            endpoint_configuration = cls._schema_on_200.Element.orchestration_settings.endpoint_configuration
            endpoint_configuration.Element = AAZStrType()

            model_parameters = cls._schema_on_200.Element.orchestration_settings.model_parameters
            model_parameters.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
