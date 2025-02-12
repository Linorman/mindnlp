# Copyright 2022 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""
Test docvqa_zh
"""

import os
import unittest
import shutil
import pytest
from mindnlp import load_dataset
from mindnlp.dataset import docvqa_zh


class TestHFDocvqazh(unittest.TestCase):
    r"""
    Test HF_Docvqa_zh
    """

    @classmethod
    def setUpClass(cls):
        cls.root = os.path.join(os.path.expanduser("~"), ".mindnlp")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.root)

    @pytest.mark.download
    @pytest.mark.local
    def test_docvqa_zh(self):
        """Test HF_Docvqa_zh"""
        num_lines = {
            "train": 32806,
            "dev": 3929,
            "test": 3904,
        }
        dataset_train, dataset_dev, dataset_test = docvqa_zh(root=self.root, split=('train', 'dev', 'test'))
        assert dataset_train.get_dataset_size() == num_lines["train"]
        assert dataset_dev.get_dataset_size() == num_lines["dev"]
        assert dataset_test.get_dataset_size() == num_lines["test"]

        dataset_train = docvqa_zh(root=self.root, split='train')
        dataset_dev = docvqa_zh(root=self.root, split='dev')
        dataset_test = docvqa_zh(root=self.root, split='test')
        assert dataset_train.get_dataset_size() == num_lines["train"]
        assert dataset_dev.get_dataset_size() == num_lines["dev"]
        assert dataset_test.get_dataset_size() == num_lines["test"]

    @pytest.mark.download
    def test_docvqa_zh_by_register(self):
        """test docvqa_zh by register"""
        _ = load_dataset('docvqa_zh',
                 root=self.root,
                 split=('dev')
                 )
