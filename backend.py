from flask import Flask, render_template, request, jsonify
import hashlib
import time

app = Flask(__name__)

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        
        self.data = data
        self.hash = hash
        self.nonce = nonce

def calculate_hash(index, previous_hash, timestamp, data, nonce):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data) + str(nonce)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Genesis Block", 0), 0)

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = time.time()
    nonce = 0
    hash = calculate_hash(index, previous_block.hash, timestamp, data, nonce)

    while not hash.startswith("0000"):  # Proof-of-work: Simple requirement for the hash to start with four zeros
        nonce += 1
        hash = calculate_hash(index, previous_block.hash, timestamp, data, nonce)

    return Block(index, previous_block.hash, timestamp, data, hash, nonce)

class Blockchain:
    def __init__(self):
        self.chain = [create_genesis_block()]

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        self.chain.append(new_block)

my_blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('index.html', blockchain=my_blockchain.chain)

@app.route('/transaction', methods=['POST'])
def transaction():
    sender = request.form['sender']
    receiver = request.form['receiver']
    amount = int(request.form['amount'])

    new_block_data = f"{sender} sent {amount} to {receiver}"
    previous_block = my_blockchain.get_last_block()
    new_block = create_new_block(previous_block, new_block_data)

    my_blockchain.add_block(new_block)

    return jsonify({'message': 'Transaction added successfully'})

if __name__ == '__main__':
    app.run(debug=True)
