# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import logging

from contractvmd import config, dapp
from contractvmd.proto import Protocol
from contractvmd.chain.message import Message

logger = logging.getLogger(config.APP_NAME)

class EmptyProto:
	DAPP_CODE = [ 0x01, 0x04 ]
	METHOD_LIST = []


class EmptyMessage (Message):
	def toJSON (self):
		data = super (EmptyMessage, self).toJSON ()
		return data


class EmptyAPI (dapp.API):
	def __init__ (self, vm, dht, api):
		self.api = api
		self.vm = vm
		self.dht = dht

		rpcmethods = {}
		errors = {}

		super (EmptyAPI, self).__init__(vm, dht, rpcmethods, errors)


class EmptyCore (dapp.Core):
	def __init__ (self, chain, database):
		super (EmptyCore, self).__init__ (chain, database)


class empty (dapp.Dapp):
	def __init__ (self, chain, db, dht, apimaster):
		self.core = EmptyCore (chain, db)
		api = EmptyAPI (self.core, dht, apimaster)		
		super (empty, self).__init__(EmptyProto.DAPP_CODE, EmptyProto.METHOD_LIST, chain, db, dht, api)
		

	def handleMessage (self, m):
		pass			
		
