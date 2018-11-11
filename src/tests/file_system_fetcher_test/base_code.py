if __name__ == "__main__":
    import sys
    '''
    Import commands
    '''
    sys.path.insert(0, "../../commands")
    sys.path.append("../../output")
    from file_system_fetcher import *
    from output_queue import *

    tk_root = Tk()
    tk_root.withdraw()
    my_fsf = FileSystemFetcher(tk_root)
    x = my_fsf.execute()
    tk_root.mainloop()
