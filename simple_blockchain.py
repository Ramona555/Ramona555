
from Block import Block
import datetime 

blocks_number_need_to_generate = 10

blockchains=[Block.create_genesis_block()]

print("创世区块是",blockchains[0].hash)

for i in range(1,blocks_number_need_to_generate):
    transaction="传输信号增加了 3 bit"
    blockchains.append(Block(blockchains[i-1].hash,transaction,datetime.datetime.now()))

    print("区块{}已经被创建，信息是{}".format(1,transaction))
    print("区块的哈希值是：",blockchains[i].hash)
    
'''
blocks_number_need_to_generate = 10
blockchains = [Block.create_genesis_block()]
previous_block = blockchains[0]
proof=[Block.proof_of_work]

print("创世区块是", previous_block.hash)

for i in range(1, blocks_number_need_to_generate):
    transaction = "传输信号增加了 3 bit"
    
    
    # 创建新区块
    new_block = Block(previous_block.hash, transaction, datetime.datetime.now(), proof)
    blockchains.append(new_block)

    print("区块{}已经被创建，信息是{}".format(i, transaction))
    print("区块的哈希值是：", new_block.hash)
    
    previous_block = new_block'''