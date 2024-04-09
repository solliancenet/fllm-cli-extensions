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
    "vectorization vectorizationrequest upsert",
)
class Upsert(AAZCommand):
    """upsert
    """

    _aaz_info = {
        "version": "2024-02-16",
        "resources": [
            ["fllm-plane", "/instances/{}/providers/foundationallm.vectorization/vectorizationrequests/{}", "2024-02-16"],
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
            help="VectorizationRequest",
            blank={},
        )

        body = cls._args_schema.body
        body.item = AAZObjectArg(
            options=["item"],
        )
        cls._build_args_vectorization_step_create(body.item)
        body.completed_steps = AAZStrArg(
            options=["completed-steps"],
            help="completed_steps",
        )
        body.content_identifier = AAZObjectArg(
            options=["content-identifier"],
            help="ContentIdentifier",
        )
        body.id = AAZStrArg(
            options=["id"],
            help="id",
        )
        body.object_id = AAZStrArg(
            options=["object-id"],
            help="object_id",
        )
        body.processing_type = AAZStrArg(
            options=["processing-type"],
            help="VectorizationProcessingType",
            enum={"Asynchronous": "Asynchronous", "Synchronous": "Synchronous"},
        )
        body.remaining_steps = AAZStrArg(
            options=["remaining-steps"],
            help="remaining_steps",
        )
        body.steps = AAZListArg(
            options=["steps"],
            help="steps",
        )

        content_identifier = cls._args_schema.body.content_identifier
        content_identifier.canonical_id = AAZStrArg(
            options=["canonical-id"],
            help="canonical_id",
        )
        content_identifier.content_source_profile_name = AAZStrArg(
            options=["content-source-profile-name"],
            help="content_source_profile_name",
        )
        content_identifier.metadata = AAZDictArg(
            options=["metadata"],
            help="metadata",
        )
        content_identifier.multipart_id = AAZStrArg(
            options=["multipart-id"],
            help="multipart_id",
        )

        metadata = cls._args_schema.body.content_identifier.metadata
        metadata.Element = AAZStrArg()

        steps = cls._args_schema.body.steps
        steps.Element = AAZObjectArg()
        cls._build_args_vectorization_step_create(steps.Element)
        return cls._args_schema

    _args_vectorization_step_create = None

    @classmethod
    def _build_args_vectorization_step_create(cls, _schema):
        if cls._args_vectorization_step_create is not None:
            _schema.id = cls._args_vectorization_step_create.id
            _schema.parameters = cls._args_vectorization_step_create.parameters
            return

        cls._args_vectorization_step_create = AAZObjectArg()

        vectorization_step_create = cls._args_vectorization_step_create
        vectorization_step_create.id = AAZStrArg(
            options=["id"],
            help="id",
        )
        vectorization_step_create.parameters = AAZDictArg(
            options=["parameters"],
            help="parameters",
        )

        parameters = cls._args_vectorization_step_create.parameters
        parameters.Element = AAZStrArg()

        _schema.id = cls._args_vectorization_step_create.id
        _schema.parameters = cls._args_vectorization_step_create.parameters

    def _execute_operations(self):
        self.pre_operations()
        self.VectorizationRequestsUpsert(ctx=self.ctx)()
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

    class VectorizationRequestsUpsert(AAZHttpOperation):
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
                "/instances/{instanceId}/providers/FoundationaLLM.Vectorization/vectorizationRequests/{name}",
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
            _UpsertHelper._build_schema_vectorization_step_create(_builder.set_prop("Item", AAZObjectType, ".item"))
            _builder.set_prop("completed_steps", AAZStrType, ".completed_steps")
            _builder.set_prop("content_identifier", AAZObjectType, ".content_identifier")
            _builder.set_prop("id", AAZStrType, ".id")
            _builder.set_prop("object_id", AAZStrType, ".object_id")
            _builder.set_prop("processing_type", AAZStrType, ".processing_type")
            _builder.set_prop("remaining_steps", AAZStrType, ".remaining_steps")
            _builder.set_prop("steps", AAZListType, ".steps")

            content_identifier = _builder.get(".content_identifier")
            if content_identifier is not None:
                content_identifier.set_prop("canonical_id", AAZStrType, ".canonical_id")
                content_identifier.set_prop("content_source_profile_name", AAZStrType, ".content_source_profile_name")
                content_identifier.set_prop("metadata", AAZDictType, ".metadata")
                content_identifier.set_prop("multipart_id", AAZStrType, ".multipart_id")

            metadata = _builder.get(".content_identifier.metadata")
            if metadata is not None:
                metadata.set_elements(AAZStrType, ".")

            steps = _builder.get(".steps")
            if steps is not None:
                _UpsertHelper._build_schema_vectorization_step_create(steps.set_elements(AAZObjectType, "."))

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
            _schema_on_200.error_message = AAZStrType()
            _schema_on_200.is_success = AAZBoolType()
            _schema_on_200.object_id = AAZStrType()

            return cls._schema_on_200


class _UpsertHelper:
    """Helper class for Upsert"""

    @classmethod
    def _build_schema_vectorization_step_create(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("id", AAZStrType, ".id")
        _builder.set_prop("parameters", AAZDictType, ".parameters")

        parameters = _builder.get(".parameters")
        if parameters is not None:
            parameters.set_elements(AAZStrType, ".")


__all__ = ["Upsert"]
