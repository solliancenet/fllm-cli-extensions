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

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.completed_steps = AAZListArg(
            options=["--completed-steps"],
            arg_group="Body",
        )
        _args_schema.content_identifier = AAZObjectArg(
            options=["--content-identifier"],
            arg_group="Body",
        )
        _args_schema.id = AAZStrArg(
            options=["--id"],
            arg_group="Body",
        )
        _args_schema.object_id = AAZStrArg(
            options=["--object-id"],
            arg_group="Body",
        )
        _args_schema.processing_type = AAZIntArg(
            options=["--processing-type"],
            arg_group="Body",
            enum={"0": 0, "1": 1},
        )
        _args_schema.remaining_steps = AAZListArg(
            options=["--remaining-steps"],
            arg_group="Body",
        )
        _args_schema.steps = AAZListArg(
            options=["--steps"],
            arg_group="Body",
            blank={},
        )

        completed_steps = cls._args_schema.completed_steps
        completed_steps.Element = AAZStrArg()

        content_identifier = cls._args_schema.content_identifier
        content_identifier.canonical_id = AAZStrArg(
            options=["canonical-id"],
        )
        content_identifier.content_source_profile_name = AAZStrArg(
            options=["content-source-profile-name"],
        )
        content_identifier.multipart_id = AAZListArg(
            options=["multipart-id"],
        )

        multipart_id = cls._args_schema.content_identifier.multipart_id
        multipart_id.Element = AAZStrArg()

        remaining_steps = cls._args_schema.remaining_steps
        remaining_steps.Element = AAZStrArg()

        steps = cls._args_schema.steps
        steps.Element = AAZObjectArg()

        _element = cls._args_schema.steps.Element
        _element.id = AAZStrArg(
            options=["id"],
        )
        _element.parameters = AAZDictArg(
            options=["parameters"],
        )

        parameters = cls._args_schema.steps.Element.parameters
        parameters.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.VectorizationrequestsUpsert(ctx=self.ctx)()
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

    class VectorizationrequestsUpsert(AAZHttpOperation):
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
                "/instances/{instanceId}/providers/FoundationaLLM.Vectorization/vectorizationrequests/{name}",
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
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"client_flatten": True}}
            )
            _builder.set_prop("completedSteps", AAZListType, ".completed_steps")
            _builder.set_prop("contentIdentifier", AAZObjectType, ".content_identifier")
            _builder.set_prop("id", AAZStrType, ".id")
            _builder.set_prop("objectId", AAZStrType, ".object_id")
            _builder.set_prop("processingType", AAZIntType, ".processing_type")
            _builder.set_prop("remainingSteps", AAZListType, ".remaining_steps")
            _builder.set_prop("steps", AAZListType, ".steps")

            completed_steps = _builder.get(".completedSteps")
            if completed_steps is not None:
                completed_steps.set_elements(AAZStrType, ".")

            content_identifier = _builder.get(".contentIdentifier")
            if content_identifier is not None:
                content_identifier.set_prop("canonicalId", AAZStrType, ".canonical_id")
                content_identifier.set_prop("contentSourceProfileName", AAZStrType, ".content_source_profile_name")
                content_identifier.set_prop("multipartId", AAZListType, ".multipart_id")

            multipart_id = _builder.get(".contentIdentifier.multipartId")
            if multipart_id is not None:
                multipart_id.set_elements(AAZStrType, ".")

            remaining_steps = _builder.get(".remainingSteps")
            if remaining_steps is not None:
                remaining_steps.set_elements(AAZStrType, ".")

            steps = _builder.get(".steps")
            if steps is not None:
                steps.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".steps[]")
            if _elements is not None:
                _elements.set_prop("id", AAZStrType, ".id")
                _elements.set_prop("parameters", AAZDictType, ".parameters")

            parameters = _builder.get(".steps[].parameters")
            if parameters is not None:
                parameters.set_elements(AAZStrType, ".")

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


__all__ = ["Upsert"]