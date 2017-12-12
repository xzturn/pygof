# Copyright 2017 XZturn, Inc. All Rights Reserved.
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
# ==============================================================================
#
# Singleton Pattern with Python
#
# -*- coding: utf8 -*-


class SimpleSingleton(object):
    """
    Simplest Singleton
    """
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SimpleSingleton, cls).__new__(cls)
        return cls.instance


class Singleton(object):
    """
    Classic Singleton
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not Singleton._instance:
            Singleton._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return Singleton._instance


class LazySingleton:
    """
    Lazy Initialization Singleton
    """
    __instance = None

    def __init__(self):
        if not LazySingleton.__instance:
            print("__init__ method called..")
        else:
            print("Instance already created:", self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance


class Borg(object):
    """
    Borg/Monostate Pattern: share state and behavior
    """
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class MetaSingleton(type):
    """
    MetaClass for Singleton
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

