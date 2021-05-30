import re, os, sys, logging, json, time, requests

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Date, Numeric, cast, distinct
from sqlalchemy import and_, or_, extract

script_cwd       = os.path.dirname(os.path.realpath(__file__))
script_base, tmp = script_cwd.split('/dev/')
config_file      = os.path.join(script_base, 'conf', 'config.json')

with open(config_file, 'r') as f:
    config = json.load(f)

script_base = config['script_base']

platform = config['platform']
username = config['username']
password = config['password']
hostname = config['hostname']
database = config['database']

from_path = config['from_path']
to_path   = config['to_path']

connection_string = platform + "://" + username + ":" + password + "@" + hostname + "/" + database

engine = create_engine(connection_string)

connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()