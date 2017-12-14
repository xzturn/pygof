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
# Factory Pattern with Python
#
# -*- coding: utf8 -*-

from abc import ABCMeta, abstractmethod


################################################################################
# The Simple Factory Pattern

class AbstractProduct(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class AdvancedAbstractProduct(AbstractProduct):
    @abstractmethod
    def advance(self, abstract_product):
        pass


class Product1(AbstractProduct):
    def describe(self):
        print("This is Product1.")


class Product2(AbstractProduct):
    def describe(self):
        print("This is Product2.")


class Product3(AdvancedAbstractProduct):
    def describe(self):
        print("This is Product3.")

    def advance(self, abstract_product):
        print("%s is PRO of %s." % (type(self).__name__, type(abstract_product).__name__))


class Product4(AdvancedAbstractProduct):
    def describe(self):
        print("This is Product4.")

    def advance(self, abstract_product):
        print("%s is PRO of %s." % (type(self).__name__, type(abstract_product).__name__))


class SimpleFactory(object):
    @staticmethod
    def create(object_type):
        return eval(object_type)().describe()


################################################################################
# The Factory Method Pattern

class AbstractCreator(metaclass=ABCMeta):
    def __init__(self):
        self._products = []

    @abstractmethod
    def create(self):
        pass

    def get_products(self):
        return self._products

    def add_product(self, product):
        self._products.append(product)


class Creator1(AbstractCreator):
    def create(self):
        self.add_product(Product1)
        self.add_product(Product2)


class Creator2(AbstractCreator):
    def create(self):
        self.add_product(Product1)
        self.add_product(Product3)
        self.add_product(Product4)


################################################################################
# The Abstract Factory Pattern

class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_product(self):
        pass

    @abstractmethod
    def create_advanced_product(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product(self):
        return Product1()

    def create_advanced_product(self):
        return Product3()


class ConcreteFactory2(AbstractFactory):
    def create_product(self):
        return Product2()

    def create_advanced_product(self):
        return Product4()


class ProductStore:
    @staticmethod
    def make_products():
        for factory in [ConcreteFactory1(), ConcreteFactory2()]:
            prod = factory.create_product()
            adv_prod = factory.create_advanced_product()
            prod.describe()
            adv_prod.advance(prod)


################################################################################

if __name__ == "__main__":
    # simple factory test
    sf = SimpleFactory()
    product_type = input("Which product do you want, Product1,2,3 or 4 > ")
    sf.create(product_type)

    # factory method test
    creator_type = input("Which creator do you want to use, Creator1 or 2 > ")
    cc = eval(creator_type)()
    cc.create()
    print("Creating with {}, has products -- {}".format(type(cc).__name__, cc.get_products()))

    # abstract factor test
    ps = ProductStore()
    ps.make_products()
