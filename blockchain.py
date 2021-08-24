genesis_block = {
    "previous_hash": "",
    "index": 0,
    "transactions": []
}
blockchain = [genesis_block]
open_transactions = []
owner = "Shashank"
participants = {"Shashank"}


def hash_block(block):
    return "-".join([str(block[key]) for key in block])


def get_balance(participant):
    return [[txn["amount"] for txn in block["transactions"] if txn["sender"] == participant] for block in blockchain]


def add_value(recipient, sender=owner, amount=1.0):
    """
        Append a new value as well as the last blockchain value to the blockchain

        Arguments:
            :sender: The sender of coins
            :recipient: The reciever of coins
            :amount: The amount of coin sent with the transaction, (default [1.0])
    """
    transaction = {
        "sender": sender,
        "recipient": recipient,
        "amount": amount
    }

    open_transactions.append(transaction)

    participants.add(sender)
    participants.add(recipient)


def mine_block():
    """ Mining a block in a block chain """
    last_block = blockchain[-1]
    block = {
        "previous_hash": hash_block(last_block),
        "index": len(blockchain),
        "transactions": open_transactions
    }

    blockchain.append(block)
    return True


def get_transaction_value():
    # get the recipient name
    txn_recipient = input("Enter the recipient name: ")

    # get the transaction amount
    txn_amount = float(input("Enter the transaction amount "))

    # return the tuple of transaction
    return txn_recipient, txn_amount


def get_user_choice():
    return input("Enter your choice: ")


def print_blockchain_elements():
    print("---" * 10)
    print("Outputting Block")
    print("---" * 10)
    for block in blockchain:
        print(block)
    else:
        print("---" * 10)


def verify_chain():
    """ Verify the current blockchain and return True if it is valid """
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block["previous_hash"] != hash_block(blockchain[index - 1]):
            return False;
    return True


waiting_for_input = True

while waiting_for_input:
    # ask user to make his/her choice
    print("Please choose: ")
    print("1: Add a new transaction value")
    print("2: Mine a new block")
    print("3: Output the blockchain blocks")
    print("4: Output Participants")
    print("h: Manipulate the chain")
    print("q: Exit the program")

    # get user choice
    user_choice = get_user_choice()

    if user_choice == "1":
        recipient, amount = get_transaction_value()
        add_value(recipient, amount=amount)
    elif user_choice == "2":
       if mine_block():
           open_transactions = []
    elif user_choice == "3":
        print_blockchain_elements()
    elif user_choice == "4":
        print(participants)
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = {
                "previous_hash": "",
                "index": 0,
                "transactions": [{
                    "sender": "Chris",
                    "recipient": "Shashank",
                    "amount": 10
                }]
            }
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("Invalid input please pick a value from the list")

    if not verify_chain():
        print_blockchain_elements()
        break
    print(get_balance("Shashank"))
else:
    print("User left")
