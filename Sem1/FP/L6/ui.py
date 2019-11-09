class UI:
    def __init__(self,service):
        self._service = service
    def print_menu(self):
        print("    1  to show all the movies")
        print("    2  to show all the clients")
        print("    x  to exit")
    def start(self):
        while True:
            self.print_menu()
            command = input("> ")
            if command == "1":
                self.show_all_movies()
            elif command == "2":
                pass
            elif command == "x":
                return
            else:
                print("Not a valid command")

    def show_all_movies(self):
        print(" ")
        print("MOVIES")
        print(" ")
        for m in self._service.listMovies:
            print(m)
