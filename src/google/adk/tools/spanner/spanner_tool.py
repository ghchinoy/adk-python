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

from typing import Any
from typing import Callable
from typing import Optional

from ...utils.feature_decorator import experimental
from ..google_cloud_tool import GoogleCloudTool
from .config import SpannerToolConfig
from .spanner_credentials import SpannerCredentialsConfig


@experimental
class SpannerTool(GoogleCloudTool):
  """GoogleApiTool class for tools that call Google APIs.

  This class is for developers to handcraft customized Google API tools rather
  than auto generate Google API tools based on API specs.

  This class handles all the OAuth complexity, credential management,
  and common Google API patterns so subclasses can focus on their
  specific functionality.
  """

  def __init__(
      self,
      func: Callable[..., Any],
      *,
      credentials_config: Optional[SpannerCredentialsConfig] = None,
      spanner_tool_config: Optional[SpannerToolConfig] = None,
  ):
    """Initialize the Google API tool.

    Args:
        func: callable that impelments the tool's logic, can accept one
          'credential" parameter
        credentials_config: credentials config used to call Google API. If None,
          then we don't hanlde the auth logic
    """
    super().__init__(
        func=func,
        credentials_config=credentials_config,
        tool_config=spanner_tool_config
        if spanner_tool_config
        else SpannerToolConfig(),
    )
