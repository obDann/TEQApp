from Observable import Observable

class ButtonObservable(Observable):
    '''
    Observable object that allows observers to observe a button
    '''

    def __init__(self, button=None):
        ''' (Observable, Button) -> None

        Initialize a ButtonObservable object
        '''
        Observable.__init__(self)
        self.button = button
        self.template = ''

    def raise_event(self, page):
        ''' (Observable, tk.Frame) -> None

        Notifys all Observers
        '''
        self.page = page;
        Observable.raise_event(self)

    def set_button(self, button):
        ''' (Observable, Button) -> None

        Sets the button for an observable object
        '''
        self.button = button
