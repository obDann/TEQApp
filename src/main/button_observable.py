from Observable import Observable

class ButtonObservable(Observable):
    '''
    '''
    
    def __init__(self, button=None):
        ''' (Observable, Button) -> None
        
        Initialize a ButtonObservable object
        '''
        Observable.__init__(self)
        self.button = button

    def raise_event(self, page):
        ''' (Observable, tk.Frame) -> None
        
        Notifys all Observers
        '''
        self.page = page;
        Observable.raise_event(self)        

    def set_button(self, button):
        ''' (Observable, 
        '''
        self.button = button