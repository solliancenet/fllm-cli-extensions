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
    "agent upsert",
)
class Upsert(AAZCommand):
    """Creates or updates an agent.
    """

    _aaz_info = {
        "version": "2024-02-16",
        "resources": [
            ["fllm-plane", "/instances/{}/providers/foundationallm.agent/agents/{}", "2024-02-16"],
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
        _args_schema.name = AAZStrArg(
            options=["--name"],
            required=True,
        )
        _args_schema.body = AAZObjectArg(
            options=["--body"],
            help="KnowledgeManagementAgent",
            blank={},
        )

        body = cls._args_schema.body
        body.conversation_history = AAZObjectArg(
            options=["conversation-history"],
            help="ConversationHistory",
        )
        body.description = AAZStrArg(
            options=["description"],
        )
        body.embedding_profile = AAZStrArg(
            options=["embedding-profile"],
        )
        body.gatekeeper = AAZObjectArg(
            options=["gatekeeper"],
            help="Gatekeeper",
        )
        body.indexing_profile = AAZStrArg(
            options=["indexing-profile"],
        )
        body.language_model = AAZObjectArg(
            options=["language-model"],
            help="LanguageModel",
        )
        body.name = AAZStrArg(
            options=["name"],
        )
        body.object_id = AAZStrArg(
            options=["object-id"],
        )
        body.orchestrator = AAZStrArg(
            options=["orchestrator"],
        )
        body.prompt = AAZStrArg(
            options=["prompt"],
        )
        body.sessions_enabled = AAZBoolArg(
            options=["sessions-enabled"],
        )
        body.type = AAZStrArg(
            options=["type"],
        )

        conversation_history = cls._args_schema.body.conversation_history
        conversation_history.enabled = AAZBoolArg(
            options=["enabled"],
        )
        conversation_history.max_history = AAZIntArg(
            options=["max-history"],
            default=0,
        )

        gatekeeper = cls._args_schema.body.gatekeeper
        gatekeeper.options = AAZListArg(
            options=["options"],
            blank={},
        )
        gatekeeper.use_system_setting = AAZBoolArg(
            options=["use-system-setting"],
        )

        options = cls._args_schema.body.gatekeeper.options
        options.Element = AAZStrArg()

        language_model = cls._args_schema.body.language_model
        language_model.api_endpoint = AAZStrArg(
            options=["api-endpoint"],
        )
        language_model.api_key = AAZStrArg(
            options=["api-key"],
        )
        language_model.api_version = AAZStrArg(
            options=["api-version"],
        )
        language_model.deployment = AAZStrArg(
            options=["deployment"],
        )
        language_model.provider = AAZStrArg(
            options=["provider"],
        )
        language_model.temperature = AAZFloatArg(
            options=["temperature"],
            blank={},
        )
        language_model.type = AAZStrArg(
            options=["type"],
        )
        language_model.use_chat = AAZBoolArg(
            options=["use-chat"],
        )
        language_model.version = AAZStrArg(
            options=["version"],
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.AgentsUpsert(ctx=self.ctx)()
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

    class AgentsUpsert(AAZHttpOperation):
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
                "/instances/{instanceId}/providers/FoundationaLLM.Agent/agents/{name}",
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
                    "instanceId", self.ctx.args.instance_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "name", self.ctx.args.name,
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
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args.body,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"client_flatten": True}}
            )
            _builder.set_prop("conversation_history", AAZObjectType, ".conversation_history")
            _builder.set_prop("description", AAZStrType, ".description")
            _builder.set_prop("embedding_profile", AAZStrType, ".embedding_profile")
            _builder.set_prop("gatekeeper", AAZObjectType, ".gatekeeper")
            _builder.set_prop("indexing_profile", AAZStrType, ".indexing_profile")
            _builder.set_prop("language_model", AAZObjectType, ".language_model")
            _builder.set_prop("name", AAZStrType, ".name")
            _builder.set_prop("object_id", AAZStrType, ".object_id")
            _builder.set_prop("orchestrator", AAZStrType, ".orchestrator")
            _builder.set_prop("prompt", AAZStrType, ".prompt")
            _builder.set_prop("sessions_enabled", AAZBoolType, ".sessions_enabled")
            _builder.set_prop("type", AAZStrType, ".type")

            conversation_history = _builder.get(".conversation_history")
            if conversation_history is not None:
                conversation_history.set_prop("enabled", AAZBoolType, ".enabled")
                conversation_history.set_prop("max_history", AAZIntType, ".max_history")

            gatekeeper = _builder.get(".gatekeeper")
            if gatekeeper is not None:
                gatekeeper.set_prop("options", AAZListType, ".options")
                gatekeeper.set_prop("use_system_setting", AAZBoolType, ".use_system_setting")

            options = _builder.get(".gatekeeper.options")
            if options is not None:
                options.set_elements(AAZStrType, ".")

            language_model = _builder.get(".language_model")
            if language_model is not None:
                language_model.set_prop("api_endpoint", AAZStrType, ".api_endpoint")
                language_model.set_prop("api_key", AAZStrType, ".api_key")
                language_model.set_prop("api_version", AAZStrType, ".api_version")
                language_model.set_prop("deployment", AAZStrType, ".deployment")
                language_model.set_prop("provider", AAZStrType, ".provider")
                language_model.set_prop("temperature", AAZFloatType, ".temperature")
                language_model.set_prop("type", AAZStrType, ".type")
                language_model.set_prop("use_chat", AAZBoolType, ".use_chat")
                language_model.set_prop("version", AAZStrType, ".version")

            return self.serialize_content(_content_value)

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
            _schema_on_200.object_id = AAZStrType(
                serialized_name="ObjectId",
            )

            return cls._schema_on_200


class _UpsertHelper:
    """Helper class for Upsert"""


__all__ = ["Upsert"]
