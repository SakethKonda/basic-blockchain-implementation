from util import *
from blocks import Block


class Blockchain:
	difficulty = difficulty
	
	def __init__(self):
		self.chain = []
		self.pending=[]		
		self.init_genesis_block()

	def init_genesis_block(self):
		genisis_block = Block(0,sample_data,time.time(),'0')
		genisis_block.hash = genisis_block.compute_hash()
		self.chain.append(genisis_block)

	@property
	def last_block(self):
		return self.chain[-1]

	def add_block(self,block,proof):
		prev_hash = self.last_block.hash
		if prev_hash != block.prev_hash:
			return False
		if not self.is_valid_proof(block,proof):
			return False

		block.hash = proof
		self.chain.append(block)
		return True

	def is_valid_proof(self,block,block_hash):
		return(block_hash.startswith('0'*Blockchain.difficulty) and
			block_hash == block.compute_hash())

	def proof_of_work(self,block):
		block.nonce = 0
		hash = block.compute_hash()
		while not hash.startswith('0'*Blockchain.difficulty):
			block.nonce += 1
			hash = block.compute_hash()
		return hash

	def add_new(self,data):
		self.pending.extend(data)

	def mine(self):
		if not self.pending:
			return False

		for data in self.pending:
			last_block = self.last_block
			new_block = Block(last_block.index+1,data,
				time.time(),last_block.hash)
			proof = self.proof_of_work(new_block)
			self.add_block(new_block,proof)

		self.pending=[]

	def return_data(self,uidx,auth=1):
		blocks = []
		for block in self.chain:
			if(block.uidx == uidx):
				blocks.append(block.return_details(auth))
		if not len(blocks):
			return f"No details found for {uidx}"

		index=0
		res = f'Data for {uidx}\n'
		while index < len(blocks)-1:
			res+= return_formatted_block(blocks[index])
			index += 1
			res+= arrow+'\n'
		res += return_formatted_block(blocks[index])
		return res

	def return_blockchain(self,auth=2):
		blocks =[]
		res=''
		if not len(self.chain):
			return "Blockchain is empty!"
		for block in self.chain:
			blocks.append(block.return_details(auth))

		if(len(blocks)>1):
			index = 1
			while index < len(blocks)-1:
				res+= return_formatted_block(blocks[index])+'\n'
				index += 1
				res += arrow +'\n'
			res += return_formatted_block(blocks[index]) +'\n'
		return res

if __name__ == '__main__':
	with open('test_data.csv','r') as f:
		dict_reader = csv.DictReader(f)
		data = list(dict_reader)

	blockchain = Blockchain()
	blockchain.add_new(data)
	blockchain.mine()
	blockchain.return_blockchain(2)
	# print(blockchain.return_data('876304952623'))