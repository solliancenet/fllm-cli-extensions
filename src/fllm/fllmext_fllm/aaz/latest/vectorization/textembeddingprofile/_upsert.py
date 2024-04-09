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
    "vectorization textembeddingprofile upsert",
)
class Upsert(AAZCommand):
    """upsert
    """

    _aaz_info = {
        "version": "2024-02-16",
        "resources": [
            ["fllm-plane", "/instances/{}/providers/foundationallm.vectorization/textembeddingprofiles/{}", "2024-02-16"],
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
            help="TextEmbeddingProfile",
            blank={},
        )

        body = cls._args_schema.body
        body.configuration_references = AAZDictArg(
            options=["configuration-references"],
            help="configuration_references",
        )
        body.created_by = AAZStrArg(
            options=["created-by"],
            help="created_by",
        )
        body.created_on = AAZObjectArg(
            options=["created-on"],
            help="created_on",
            blank={},
        )
        body.deleted = AAZBoolArg(
            options=["deleted"],
            help="deleted",
        )
        body.description = AAZStrArg(
            options=["description"],
            help="description",
        )
        body.display_name = AAZStrArg(
            options=["display-name"],
            help="display_name",
        )
        body.name = AAZStrArg(
            options=["name"],
            help="name",
        )
        body.object_id = AAZStrArg(
            options=["object-id"],
            help="object_id",
        )
        body.settings = AAZDictArg(
            options=["settings"],
            help="settings",
        )
        body.text_embedding = AAZStrArg(
            options=["text-embedding"],
            help="TextEmbeddingType",
            enum={"SemanticKernelTextEmbedding": "SemanticKernelTextEmbedding"},
        )
        body.type = AAZStrArg(
            options=["type"],
            help="type",
        )
        body.updated_by = AAZStrArg(
            options=["updated-by"],
            help="updated_by",
        )
        body.updated_on = AAZObjectArg(
            options=["updated-on"],
            help="updated_on",
            blank={},
        )

        configuration_references = cls._args_schema.body.configuration_references
        configuration_references.Element = AAZStrArg()

        settings = cls._args_schema.body.settings
        settings.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.TextEmbeddingProfilesUpsert(ctx=self.ctx)()
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

    class TextEmbeddingProfilesUpsert(AAZHttpOperation):
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
                "/instances/{instanceId}/providers/FoundationaLLM.Vectorization/textEmbeddingProfiles/{name}",
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
            _builder.set_prop("configuration_references", AAZDictType, ".configuration_references")
            _builder.set_prop("created_by", AAZStrType, ".created_by")
            _builder.set_prop("created_on", AAZObjectType, ".created_on")
            _builder.set_prop("deleted", AAZBoolType, ".deleted")
            _builder.set_prop("description", AAZStrType, ".description")
            _builder.set_prop("display_name", AAZStrType, ".display_name")
            _builder.set_prop("name", AAZStrType, ".name")
            _builder.set_prop("object_id", AAZStrType, ".object_id")
            _builder.set_prop("settings", AAZDictType, ".settings")
            _builder.set_prop("text_embedding", AAZStrType, ".text_embedding")
            _builder.set_prop("type", AAZStrType, ".type")
            _builder.set_prop("updated_by", AAZStrType, ".updated_by")
            _builder.set_prop("updated_on", AAZObjectType, ".updated_on")

            configuration_references = _builder.get(".configuration_references")
            if configuration_references is not None:
                configuration_references.set_elements(AAZStrType, ".")

            settings = _builder.get(".settings")
            if settings is not None:
                settings.set_elements(AAZStrType, ".")

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
