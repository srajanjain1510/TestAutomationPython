from DesignPatterns.behavioral.chain_of_responsibility_pattery import Chain, ConcreteHandlerA, ConcreteHandlerB

if __name__ == '__main__':
    chain = Chain()
    chain.add_handler(ConcreteHandlerA())
    chain.add_handler(ConcreteHandlerB())

    requests = ['A','B','C']

    for request in requests:
        print(f'Processing request {request}')
        chain.handle_request(request)
