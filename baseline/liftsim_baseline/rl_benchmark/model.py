#   Copyright (c) 2018 PaddlePaddle Authors. All Rights Reserved.
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

import os
import paddle.fluid as fluid
import parl.layers as layers
import numpy as np
from parl.framework.model_base import Model
from parl.framework.agent_base import Agent
from parl.utils import get_gpu_count


class RLDispatcherModel(Model):
    def __init__(self, act_dim):
        self._act_dim = act_dim
        self._fc_1 = layers.fc(size=512, act='relu')
        self._fc_2 = layers.fc(size=256, act='relu')
        self._fc_3 = layers.fc(size=128, act='tanh')
        self._output = layers.fc(size=act_dim)

    def value(self, obs):
        self._h_1 = self._fc_1(obs)
        self._h_2 = self._fc_2(self._h_1)
        self._h_3 = self._fc_3(self._h_2)
        self._pred = self._output(self._h_3)
        return self._pred