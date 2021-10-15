#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Created by zyj at 2021/10/15.
    Description:
    Changelog: all notable changes to this file will be documented
"""

from dataclasses import dataclass, field
from datetime import datetime

from dataclasses_json import dataclass_json, config
from marshmallow import Schema, fields


@dataclass_json
@dataclass
class DataModel:
    int_field: int
    str_field: str
    time_field: datetime = field(
        metadata = config(
            encoder = datetime.isoformat,
            decoder = datetime.fromisoformat,
            mm_field = fields.DateTime(format = 'iso')
        )
    )
    default_field: str = ""  # 默认值


model = DataModel(1, "1",datetime.now())



class DataModelSchema(Schema):
    int_field = fields.Int()
    str_field = fields.Str()
    time_field = fields.DateTime()

model2 = DataModelSchema()
model2.str_field = "3"
model2.int_field = 2
model2.time_field = datetime.now()

if __name__ == "__main__":
    print(model.to_json(), DataModel.from_json(model.to_json()))
    print(model.to_dict(), DataModel.from_dict(model.to_dict()))
    print(DataModelSchema().dump(model2),DataModelSchema().load(DataModelSchema().dump(model2)))
    # print(DataModelSchema.schema().load('[{"int_field": 1, "str_field": "1", "default_field": ""}]',many = True))
