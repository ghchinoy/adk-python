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

from ...utils.feature_decorator import experimental
from ..google_cloud_credentials import GoogleCloudCredentialsConfig

SPANNER_TOKEN_CACHE_KEY = "spanner_token_cache"
SPANNER_DEFAULT_SCOPE = ["https://www.googleapis.com/auth/spanner.data"]


@experimental
class SpannerCredentialsConfig(GoogleCloudCredentialsConfig):
  """Configuration for Google API tools (Experimental).

  Please do not use this in production, as it may be deprecated later.
  """

  def __init__(self, **kwargs):
    if "default_scopes" not in kwargs:
      kwargs["default_scopes"] = SPANNER_DEFAULT_SCOPE
    if "token_cache_key" not in kwargs:
      kwargs["token_cache_key"] = SPANNER_TOKEN_CACHE_KEY
    super().__init__(**kwargs)
