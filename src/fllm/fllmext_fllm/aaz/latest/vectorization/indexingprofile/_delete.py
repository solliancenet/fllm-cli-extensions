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
    "vectorization indexingprofile delete",
    confirmation="Are you sure you want to perform this operation?",
)
class Delete(AAZCommand):
    """delete
    """

    _aaz_info = {
        "version": "2024-02-16",
        "resources": [
            ["fllm-plane", "/instances/{}/providers/foundationallm.vectorization/indexingprofiles/{}", "2024-02-16"],
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
        _args_schema.name = AAZStrArg(
            options=["--name"],
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.IndexingProfilesDelete(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class IndexingProfilesDelete(AAZHttpOperation):
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
                "/instances/{instanceId}/providers/FoundationaLLM.Vectorization/indexingProfiles/{name}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "DELETE"

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

        def on_200(self, session):
            pass


class _DeleteHelper:
    """Helper class for Delete"""


__all__ = ["Delete"]
