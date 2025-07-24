# Copyright 2025 Google LLC
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

from __future__ import annotations

import google.api_core.client_info
from google.auth.credentials import Credentials
from google.cloud import spanner
from google.cloud.spanner_v1 import __version__ as spanner_version

from ... import version

USER_AGENT = f"adk-spanner-tool google-adk/{version.__version__}"


def get_spanner_client(
    *, project: str, credentials: Credentials
) -> spanner.Client:
  """Get a Spanner client."""

  client_info = google.api_core.client_info.ClientInfo(
      client_library_version=spanner_version, user_agent=USER_AGENT
  )

  spanner_client = spanner.Client(
      project=project, credentials=credentials, client_info=client_info
  )

  return spanner_client
