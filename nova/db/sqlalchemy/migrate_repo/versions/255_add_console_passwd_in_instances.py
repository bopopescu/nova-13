# Copyright (c) 2014 Cisco Systems, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table


def upgrade(engine):
    """Function adds console_passwd field."""
    meta = MetaData(bind=engine)

    instances = Table('instances', meta, autoload=True)
    shadow_instances = Table('shadow_instances', meta, autoload=True)
    console_passwd = Column('console_passwd', String(256), nullable=True)

    if not hasattr(instances.c, 'console_passwd'):
        instances.create_column(console_passwd)

    if not hasattr(shadow_instances.c, 'console_passwd'):
        shadow_instances.create_column(console_passwd.copy())


def downgrade(engine):
    """Function drops console_passwd field."""
    meta = MetaData(bind=engine)

    instances = Table('instances', meta, autoload=True)
    shadow_instances = Table('shadow_instances', meta, autoload=True)

    if hasattr(instances.c, 'console_passwd'):
        instances.c.console_passwd.drop()

    if hasattr(shadow_instances.c, 'console_passwd'):
        shadow_instances.c.console_passwd.drop()
