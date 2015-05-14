#!/usr/local/bin/python

import json
import boto.ec2
import sys

tag_name = sys.argv[1]

conn = boto.ec2.connect_to_region("us-east-1")
reservations = conn.get_all_instances(filters={"tag:Name" : tag_name})

for reserved in reservations:
  for instance in reserved.instances:
    print instance.id
