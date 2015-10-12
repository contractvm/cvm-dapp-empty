# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import time
from libcontractvm import Wallet, ConsensusManager, DappManager

class EmptyManager (DappManager.DappManager):
	def __init__ (self, consensusManager, wallet = None):
		super (EmptyManager, self).__init__(consensusManager, wallet)
