from hashlib import sha256
MAX_NONCE = 5


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeroes):
    prefix_str = '0'*prefix_zeroes
    for nonce in range(MAX_NONCE):
        text = str(block_number)+transactions+previous_hash+str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print('Good job! You cracked it !!! \n Nonce is {}'.format(nonce))
            return new_hash

    raise BaseException(
        f"Couldn't find correct hash after trying {MAX_NONCE} times")


if __name__ == 'main':
    transaction = '''
    Sayan->Sid->20,
    Sid->Rahul->26
    '''

    difficulty = 1

    newHash = mine(
        2, transaction, '0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)

    print(newHash)
