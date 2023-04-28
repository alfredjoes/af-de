#!/usr/bin/env python
# -*- coding: utf-8 -*-



import django



print(pandas.__version__)


print(django.__path__)



print(dir(django) )


def get_methods(self):
  return (list(filter(lambda m: not m.startswith("_") and callable(getattr(self, m)),dir(self))))


print(get_methods(django))




