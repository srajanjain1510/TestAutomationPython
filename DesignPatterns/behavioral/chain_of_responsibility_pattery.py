from abc import ABC, abstractmethod


class Handler(ABC):

    @abstractmethod
    def handle_request(self, request):
        pass


class ConcreteHandlerA(Handler):

    def handle_request(self, request):
        if request == 'A':
            print('Handled by concrete handler A')
        else:
            print('passed to other concrete handler')
            super().handle_request(request)


class ConcreteHandlerB(Handler):

    def handle_request(self, request):
        if request == 'B':
            print('Handled by concrete handler B')
        else:
            print('Passed to other handler')
            super().handle_request(request)


class Chain:
    def __init__(self):
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def handle_request(self, request):
        for handler in self.handlers:
            handler.handle_request(request)
