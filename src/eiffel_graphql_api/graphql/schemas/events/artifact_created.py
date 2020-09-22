# Copyright 2019-2020 Axis Communications AB.
#
# For a full list of individual contributors, please see the commit history.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Eiffel artifact created."""
import graphene

from ..base import EiffelObjectType
from ..lib.generic import json_schema_to_graphql, load

# pylint: disable=too-few-public-methods


class ArtifactCreated(EiffelObjectType):
    """Artifact created object type."""

    data = json_schema_to_graphql(
        "ArtifactCreatedData",
        load("EiffelArtifactCreatedEvent.json").get("data").get("properties"),
        override_name={"tags": "artifactTags"},
    )
    mongo = None

    def __init__(self, mongo):
        """Initialize mongo instance."""
        # pylint:disable=super-init-not-called
        self.mongo = mongo


class ArtifactCreatedConnection(graphene.Connection):
    """Artifact created connection."""

    class Meta:
        """Graphene meta data."""

        node = ArtifactCreated
