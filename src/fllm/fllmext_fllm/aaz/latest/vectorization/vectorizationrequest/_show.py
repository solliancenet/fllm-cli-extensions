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
    "vectorization vectorizationrequest show",
)
class Show(AAZCommand):
    """show
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
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.VectorizationRequestsGet(ctx=self.ctx)()
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

    class VectorizationRequestsGet(AAZHttpOperation):
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
            _element.item = AAZObjectType(
                serialized_name="Item",
            )
            _ShowHelper._build_schema_vectorization_step_read(_element.item)
            _element.completed_steps = AAZStrType()
            _element.content_identifier = AAZObjectType()
            _element.id = AAZStrType()
            _element.object_id = AAZStrType()
            _element.processing_type = AAZStrType()
            _element.remaining_steps = AAZStrType()
            _element.steps = AAZListType()

            content_identifier = cls._schema_on_200.Element.content_identifier
            content_identifier.canonical_id = AAZStrType()
            content_identifier.content_source_profile_name = AAZStrType()
            content_identifier.metadata = AAZDictType()
            content_identifier.multipart_id = AAZStrType()

            metadata = cls._schema_on_200.Element.content_identifier.metadata
            metadata.Element = AAZStrType()

            steps = cls._schema_on_200.Element.steps
            steps.Element = AAZObjectType()
            _ShowHelper._build_schema_vectorization_step_read(steps.Element)

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_vectorization_step_read = None

    @classmethod
    def _build_schema_vectorization_step_read(cls, _schema):
        if cls._schema_vectorization_step_read is not None:
            _schema.id = cls._schema_vectorization_step_read.id
            _schema.parameters = cls._schema_vectorization_step_read.parameters
            return

        cls._schema_vectorization_step_read = _schema_vectorization_step_read = AAZObjectType()

        vectorization_step_read = _schema_vectorization_step_read
        vectorization_step_read.id = AAZStrType()
        vectorization_step_read.parameters = AAZDictType()

        parameters = _schema_vectorization_step_read.parameters
        parameters.Element = AAZStrType()

        _schema.id = cls._schema_vectorization_step_read.id
        _schema.parameters = cls._schema_vectorization_step_read.parameters


__all__ = ["Show"]
