# python packages needed
from tkinter import *
from tkinter import filedialog
from os import path
import subprocess
import sys
from graph import *
try:
    from PIL import Image
    from PIL import ImageTk
except:
    # install python packages if not already
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pygame'])
    from PIL import Image
    from PIL import ImageTk

class GUI(Canvas):
    def __init__(self, root):
        # init the gui
        self.parent = root
        self.parent.title('Graph')
        self.SW = self.parent.winfo_screenwidth()
        self.SH = self.parent.winfo_screenheight()
        self.WIDTH = self.SW // 2
        self.HEIGHT = self.SH // 2
        self.parent.resizable(0, 0)
        self.parent.overrideredirect(True)
        self.parent.geometry(f'+{self.SW // 4}+{self.SH // 4}')
        self.IMAGE_FOLDER = 'images'
        Canvas.__init__(self, self.parent, width = self.WIDTH, height = self.HEIGHT, highlightthickness = 0)
        self.load_data()
        self.draw_board()
        self.buttons_layout()

    def load_data(self):
        # load images
        dir = path.dirname(__file__)
        Bg_image = Image.open(path.join(dir, self.IMAGE_FOLDER, 'Bg.png'))
        Bg_image = Bg_image.resize((int(2400 / 2048 * self.SW), int(1260 / 1152 * self.SH)), Image.ANTIALIAS)
        self.Bg_image = ImageTk.PhotoImage(Bg_image)
        Select = Image.open(path.join(dir, self.IMAGE_FOLDER, 'Select.png'))
        Select = Select.resize((int(108 / 2048 * self.SW), int(48 / 1152 * self.SH)), Image.ANTIALIAS)
        self.Select = ImageTk.PhotoImage(Select)
        Exit = Image.open(path.join(dir, self.IMAGE_FOLDER, 'Exit.png'))
        Exit = Exit.resize((int(50 / 2048 * self.SW), int(48 / 1152 * self.SH)), Image.ANTIALIAS)
        self.Exit = ImageTk.PhotoImage(Exit)

    def draw_board(self):
        # create a basic window
        self.create_image(0, 0, image = self.Bg_image, anchor = NW)
        self.create_text(10, 10, text = 'Graph Project', font = ('Arial', int(15 / 2048 * self.SW)), fill = 'white', anchor = NW)
        exit_btn = Button(self, image = self.Exit, bd = 0, command = self.parent.destroy).place(x = self.WIDTH, y = 0, anchor = NE)

    def buttons_layout(self):
        # create the buttons layout of the window with all the choses
        file_entry = Entry(self, width = 25, font = ('Arial', int(10 / 2048 * self.SW)))
        file_entry.place(x = self.WIDTH // 2 - 10, y = self.HEIGHT // 6 - 30, anchor = 'center')
        browse_btn = Button(self, text = 'Browse', bd = 0, font = ('Arial', int(10 / 2048 * self.SW)), command = lambda: self.browse(file_entry))
        browse_btn.place(x = self.WIDTH // 2 + 100, y = self.HEIGHT // 6 - 30, anchor = W)

        self.create_text(self.WIDTH // 2 - 40, self.HEIGHT // 6 + 20, text = 'Starting node number:', font = ('Arial', int(12 / 2048 * self.SW)), fill = 'white', anchor = 'center')
        node_entry = Entry(self, width = 4, font = ('Arial', int(12 / 2048 * self.SW)))
        node_entry.place(x = self.WIDTH // 2 + 50, y = self.HEIGHT // 6 + 20, anchor = W)
        all_btn = Button(self, text = 'All nodes', bd = 0, font = ('Arial', int(10 / 2048 * self.SW)), command = lambda: self.write_entry(node_entry, 'All'))
        all_btn.place(x = self.WIDTH // 2 + 125, y = self.HEIGHT // 6 + 20, anchor = W)

        done_btn = Button(self, text = 'Done', bd = 0, font = ('Arial', int(15 / 2048 * self.SW)), command = lambda: self.done(file_entry, node_entry, methods, delete_list))
        done_btn.place(x = self.WIDTH // 2, y = self.HEIGHT // 6 * 6 - 30, anchor = E)

        NN = BooleanVar()
        NI = BooleanVar()
        Fletcher = BooleanVar()
        Fletcher_Clarke = BooleanVar()

        NN_btn = Checkbutton(self, bd = 0, variable = NN, onvalue = True, offvalue = False)
        NN_btn.place(x = self.WIDTH // 8 * 2, y = self.HEIGHT // 6 * 2, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 2 + 20, self.HEIGHT // 6 * 2, text = 'Nearest Neighbor', font = ('Arial', int(15 / 2048 * self.SW)), fill = 'white', anchor = W)
        NI_btn = Checkbutton(self, bd = 0, variable = NI, onvalue = True, offvalue = False)
        NI_btn.place(x = self.WIDTH // 8 * 2, y = self.HEIGHT // 6 * 3, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 2 + 20, self.HEIGHT // 6 * 3, text = 'Nearest Insertion', font = ('Arial', int(15 / 2048 * self.SW)), fill = 'white', anchor = W)
        Fletcher_btn = Checkbutton(self, bd = 0, variable = Fletcher, onvalue = True, offvalue = False)
        Fletcher_btn.place(x = self.WIDTH // 8 * 2, y = self.HEIGHT // 6 * 4, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 2 + 20, self.HEIGHT // 6 * 4, text = 'Fletcher', font = ('Arial', int(15 / 2048 * self.SW)), fill = 'white', anchor = W)
        Fletcher_Clarke_btn = Checkbutton(self, bd = 0, variable = Fletcher_Clarke, onvalue = True, offvalue = False)
        Fletcher_Clarke_btn.place(x = self.WIDTH // 8 * 2, y = self.HEIGHT // 6 * 5, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 2 + 20, self.HEIGHT // 6 * 5, text = 'Fletcher & Clarke', font = ('Arial', int(15 / 2048 * self.SW)), fill = 'white', anchor = W)


        NN_ER = BooleanVar()
        NI_ER = BooleanVar()
        Fletcher_ER = BooleanVar()
        Fletcher_Clarke_ER = BooleanVar()

        NN_ER_btn = Checkbutton(self, bd = 0, variable = NN_ER, onvalue = True, offvalue = False)
        NN_ER_btn.place(x = self.WIDTH // 8 * 5, y = self.HEIGHT // 6 * 2 - 20, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 5 + 20, self.HEIGHT // 6 * 2 - 20, text = 'ER', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = W)
        NI_ER_btn = Checkbutton(self, bd = 0, variable = NI_ER, onvalue = True, offvalue = False)
        NI_ER_btn.place(x = self.WIDTH // 8 * 5, y = self.HEIGHT // 6 * 3 - 20, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 5 + 20, self.HEIGHT // 6 * 3 - 20, text = 'ER', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = W)
        Fletcher_ER_btn = Checkbutton(self, bd = 0, variable = Fletcher_ER, onvalue = True, offvalue = False)
        Fletcher_ER_btn.place(x = self.WIDTH // 8 * 5, y = self.HEIGHT // 6 * 4 - 20, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 5 + 20, self.HEIGHT // 6 * 4 - 20, text = 'ER', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = W)
        Fletcher_Clarke_ER_btn = Checkbutton(self, bd = 0, variable = Fletcher_Clarke_ER, onvalue = True, offvalue = False)
        Fletcher_Clarke_ER_btn.place(x = self.WIDTH // 8 * 5, y = self.HEIGHT // 6 * 5 - 20, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 5 + 20, self.HEIGHT // 6 * 5 - 20, text = 'ER', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = W)

        NN_OPT = BooleanVar()
        NI_OPT = BooleanVar()
        Fletcher_OPT = BooleanVar()
        Fletcher_Clarke_OPT = BooleanVar()

        NN_OPT_btn = Checkbutton(self, bd = 0, variable = NN_OPT, onvalue = True, offvalue = False)
        NN_OPT_btn.place(x = self.WIDTH // 8 * 5, y = self.HEIGHT // 6 * 2 + 20, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 5 + 20, self.HEIGHT // 6 * 2 + 20, text = '2-OPT', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = W)
        NI_OPT_btn = Checkbutton(self, bd = 0, variable = NI_OPT, onvalue = True, offvalue = False)
        NI_OPT_btn.place(x = self.WIDTH // 8 * 5, y = self.HEIGHT // 6 * 3 + 20, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 5 + 20, self.HEIGHT // 6 * 3 + 20, text = '2-OPT', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = W)
        Fletcher_OPT_btn = Checkbutton(self, bd = 0, variable = Fletcher_OPT, onvalue = True, offvalue = False)
        Fletcher_OPT_btn.place(x = self.WIDTH // 8 * 5, y = self.HEIGHT // 6 * 4 + 20, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 5 + 20, self.HEIGHT // 6 * 4 + 20, text = '2-OPT', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = W)
        Fletcher_Clarke_OPT_btn = Checkbutton(self, bd = 0, variable = Fletcher_Clarke_OPT, onvalue = True, offvalue = False)
        Fletcher_Clarke_OPT_btn.place(x = self.WIDTH // 8 * 5, y = self.HEIGHT // 6 * 5 + 20, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 5 + 20, self.HEIGHT // 6 * 5 + 20, text = '2-OPT', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = W)


        NN_EROPT = BooleanVar()
        NI_EROPT = BooleanVar()
        Fletcher_EROPT = BooleanVar()
        Fletcher_Clarke_EROPT = BooleanVar()

        NN_EROPT_btn = Checkbutton(self, bd = 0, variable = NN_EROPT, onvalue = True, offvalue = False)
        NN_EROPT_btn.place(x = self.WIDTH // 8 * 6, y = self.HEIGHT // 6 * 2 - 20, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 6 + 20, self.HEIGHT // 6 * 2 - 20, text = '2-OPT', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = W)
        NI_EROPT_btn = Checkbutton(self, bd = 0, variable = NI_EROPT, onvalue = True, offvalue = False)
        NI_EROPT_btn.place(x = self.WIDTH // 8 * 6, y = self.HEIGHT // 6 * 3 - 20, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 6 + 20, self.HEIGHT // 6 * 3 - 20, text = '2-OPT', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = W)
        Fletcher_EROPT_btn = Checkbutton(self, bd = 0, variable = Fletcher_EROPT, onvalue = True, offvalue = False)
        Fletcher_EROPT_btn.place(x = self.WIDTH // 8 * 6, y = self.HEIGHT // 6 * 4 - 20, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 6 + 20, self.HEIGHT // 6 * 4 - 20, text = '2-OPT', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = W)
        Fletcher_Clarke_EROPT_btn = Checkbutton(self, bd = 0, variable = Fletcher_Clarke_EROPT, onvalue = True, offvalue = False)
        Fletcher_Clarke_EROPT_btn.place(x = self.WIDTH // 8 * 6, y = self.HEIGHT // 6 * 5 - 20, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 6 + 20, self.HEIGHT // 6 * 5 - 20, text = '2-OPT', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = W)


        NN_OPTER = BooleanVar()
        NI_OPTER = BooleanVar()
        Fletcher_OPTER = BooleanVar()
        Fletcher_Clarke_OPTER = BooleanVar()

        NN_OPTER_btn = Checkbutton(self, bd = 0, variable = NN_OPTER, onvalue = True, offvalue = False)
        NN_OPTER_btn.place(x = self.WIDTH // 8 * 6, y = self.HEIGHT // 6 * 2 + 20, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 6 + 20, self.HEIGHT // 6 * 2 + 20, text = 'ER', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = W)
        NI_OPTER_btn = Checkbutton(self, bd = 0, variable = NI_OPTER, onvalue = True, offvalue = False)
        NI_OPTER_btn.place(x = self.WIDTH // 8 * 6, y = self.HEIGHT // 6 * 3 + 20, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 6 + 20, self.HEIGHT // 6 * 3 + 20, text = 'ER', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = W)
        Fletcher_OPTER_btn = Checkbutton(self, bd = 0, variable = Fletcher_OPTER, onvalue = True, offvalue = False)
        Fletcher_OPTER_btn.place(x = self.WIDTH // 8 * 6, y = self.HEIGHT // 6 * 4 + 20, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 6 + 20, self.HEIGHT // 6 * 4 + 20, text = 'ER', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = W)
        Fletcher_Clarke_OPTER_btn = Checkbutton(self, bd = 0, variable = Fletcher_Clarke_OPTER, onvalue = True, offvalue = False)
        Fletcher_Clarke_OPTER_btn.place(x = self.WIDTH // 8 * 6, y = self.HEIGHT // 6 * 5 + 20, anchor = 'center')
        self.create_text(self.WIDTH // 8 * 6 + 20, self.HEIGHT // 6 * 5 + 20, text = 'ER', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = W)

        delete_list = [file_entry, browse_btn, node_entry, all_btn, done_btn, NN_btn, NI_btn, Fletcher_btn, Fletcher_Clarke_btn, NN_ER_btn, NI_ER_btn, Fletcher_ER_btn, Fletcher_Clarke_ER_btn, \
                       NN_OPT_btn, NI_OPT_btn, Fletcher_OPT_btn, Fletcher_Clarke_OPT_btn, NN_EROPT_btn, NI_EROPT_btn, Fletcher_EROPT_btn, Fletcher_Clarke_EROPT_btn, NN_OPTER_btn, NI_OPTER_btn, Fletcher_OPTER_btn, Fletcher_Clarke_OPTER_btn]

        methods = [NN, NI, Fletcher, Fletcher_Clarke, NN_ER, NI_ER, Fletcher_ER, Fletcher_Clarke_ER, NN_OPT, NI_OPT, Fletcher_OPT, Fletcher_Clarke_OPT, \
                   NN_EROPT, NI_EROPT, Fletcher_EROPT, Fletcher_Clarke_EROPT, NN_OPTER, NI_OPTER, Fletcher_OPTER, Fletcher_Clarke_OPTER]

    def browse(self, entry):
        # open the windows file explorer to choose the file from your computer
        filename = filedialog.askopenfilename()
        self.write_entry(entry, filename)

    def write_entry(self, entry, text):
        # write the text to the entry (needed for the all_button and browse method)
        entry.delete(0, END)
        entry.insert(0, text)

    def done(self, file_entry, node_entry, methods, delete_list):
        # get the different entries and checkbuttons values, destroy the widgests linked to the choosing window
        file = file_entry.get()
        node = node_entry.get()
        methods = [item.get() for item in methods]
        for item in delete_list:
            item.destroy()
        self.delete('all')
        self.draw_board()
        self.parent.update()
        self.show_results(file, node, methods)

    def show_results(self, file, node, methods):
        # create an instance of GraphTheory with the file name and show the results depending of the conditions you chose
        graph = GraphTheory(file)
        select_btn = Button(image = self.Select, bd = 0, command = lambda: self.menu(select_btn))
        select_btn.place(x = 0, y = self.HEIGHT, anchor = SW)

        # invalid matrix, screen with the possible mistakes you've made
        if type(graph.matrix) != list:
            self.create_text(self.WIDTH // 2, self.HEIGHT // 2 - 100, text = 'fichier non exploitable', font = ('Arial', int(20 / 2048 * self.SW)), fill = 'white', anchor = 'center')
            content = "Veuillez vérifier le nom du fichier et son format. La taille de la matrice doit être spécifier en fin de ligne 4."
            self.create_text(self.WIDTH // 2, self.HEIGHT // 2, text = content, font = ('Arial', int(12 / 2048 * self.SW)), fill = 'white', anchor = 'center')
            content = "Chaque ligne du fichier hormis celles de la matrice doit commencer par '#'. La compatibilité hors extension .txt n'est pas garanti."
            self.create_text(self.WIDTH // 2, self.HEIGHT // 2 + 50, text = content, font = ('Arial', int(12 / 2048 * self.SW)), fill = 'white', anchor = 'center')

        else:
            self.create_text(10, self.HEIGHT // 8, text = f'file: {file}', font = ('Arial', int(12 / 2048 * self.SW)), fill = 'white', anchor = NW)
            self.create_text(10, self.HEIGHT // 8 + 20, text = f'starting node: {node}', font = ('Arial', int(12 / 2048 * self.SW)), fill = 'white', anchor = NW)
            wait_btn = self.create_text(self.WIDTH // 2, self.HEIGHT // 3, text = 'Wait for the program to respond. (it might take a while)', font = ('Arial', int(20 / 2048 * self.SW)), fill = 'white')
            self.parent.update()

            all_methods = [graph.NN, graph.NI, graph.Fletcher, graph.Fletcher_Clarke]

            if node == 'All':
                self.all_nodes(graph, methods, all_methods)
                self.create_text(self.WIDTH - 10, self.HEIGHT - 10, text = 'ER: Extraction Reinsertion', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = SE)

            else:
                try:
                    node = int(node)
                    if node > len(graph.matrix):
                        self.create_text(self.WIDTH // 2, self.HEIGHT // 3, text = 'Node not found', font = ('Arial', int(20 / 2048 * self.SW)), fill = 'white')
                        self.delete(wait_btn)
                        return
                    self.known_node(graph, node, methods, all_methods)
                    self.create_text(self.WIDTH - 10, self.HEIGHT - 10, text = 'ER: Extraction Reinsertion', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = SE)
                except:
                    int_btn = self.create_text(self.WIDTH // 2, self.HEIGHT // 3, text = 'The node must be an integer', font = ('Arial', int(20 / 2048 * self.SW)), fill = 'white')

            self.delete(wait_btn)

    def known_node(self, graph, node, methods, all_methods):
        # method to show the results if you chose a specific node as a starting point
        NO_IMPROVEMENT = [x(node)[1] if y else None for x, y in zip(all_methods, methods)]
        ER_IMPROVEMENT = [graph.ER(x(node)[0], x(node)[1])[1] if y else None for x, y in zip(all_methods, methods[4:8]) ]
        OPT_IMPROVEMENT = [graph.OPT(x(node)[0], x(node)[1])[1] if y else None for x, y in zip(all_methods, methods[8:12])]
        EROPT_IMPROVEMENT = [graph.OPT(graph.ER(x(node)[0], x(node)[1])[0], graph.ER(x(node)[0], x(node)[1])[1])[1] if y else None for x, y in zip(all_methods, methods[12:16])]
        OPTER_IMPROVEMENT = [graph.ER(graph.OPT(x(node)[0], x(node)[1])[0], graph.OPT(x(node)[0], x(node)[1])[1])[1] if y else None for x, y in zip(all_methods, methods[16:20])]

        self.plot_btn = Button(text = 'plot the solution', bd = 0, command = lambda: self.plot(graph, node, all_methods, NO_IMPROVEMENT, ER_IMPROVEMENT, OPT_IMPROVEMENT, EROPT_IMPROVEMENT, OPTER_IMPROVEMENT))
        self.plot_btn.place(x = self.WIDTH // 2, y = self.HEIGHT - 10, anchor = S)

        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 2, text = 'NO LOCAL IMPROVEMENT', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 5, text = 'ER IMPROVEMENT', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 2, text = '2-OPT IMPROVEMENT', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 5, text = '2-OPT IMPROVEMENT AFTER ER', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 6, self.HEIGHT // 8 * 2, text = 'ER IMPROVEMENT AFTER 2-OPT', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)

        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 2 + 30, text = f'Nearest Neighbor: {NO_IMPROVEMENT[0]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 2 + 50, text = f'Nearest Insertion: {NO_IMPROVEMENT[1]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 2 + 70, text = f'Fletcher: {NO_IMPROVEMENT[2]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 2 + 90, text = f'Fletcher & Clarke: {NO_IMPROVEMENT[3]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 5 + 30, text = f'Nearest Neighbor: {ER_IMPROVEMENT[0]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 5 + 50, text = f'Nearest Insertion: {ER_IMPROVEMENT[1]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 5 + 70, text = f'Fletcher: {ER_IMPROVEMENT[2]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 5 + 90, text = f'Fletcher & Clarke: {ER_IMPROVEMENT[3]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 2 + 30, text = f'Nearest Neighbor: {OPT_IMPROVEMENT[0]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 2 + 50, text = f'Nearest Insertion: {OPT_IMPROVEMENT[1]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 2 + 70, text = f'Fletcher: {OPT_IMPROVEMENT[2]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 2 + 90, text = f'Fletcher & Clarke: {OPT_IMPROVEMENT[3]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 5 + 30, text = f'Nearest Neighbor: {EROPT_IMPROVEMENT[0]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 5 + 50, text = f'Nearest Insertion: {EROPT_IMPROVEMENT[1]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 5 + 70, text = f'Fletcher: {EROPT_IMPROVEMENT[2]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 5 + 90, text = f'Fletcher & Clarke: {EROPT_IMPROVEMENT[3]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 6, self.HEIGHT // 8 * 2 + 30, text = f'Nearest Neighbor: {OPTER_IMPROVEMENT[0]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 6, self.HEIGHT // 8 * 2 + 50, text = f'Nearest Insertion: {OPTER_IMPROVEMENT[1]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 6, self.HEIGHT // 8 * 2 + 70, text = f'Fletcher: {OPTER_IMPROVEMENT[2]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 6, self.HEIGHT // 8 * 2 + 90, text = f'Fletcher & Clarke: {OPTER_IMPROVEMENT[3]}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)

    def all_nodes(self, graph, methods, all_methods):
        # method to show the results if you chose to do the methods with all starting nodes
        NO_IMPROVEMENT = [x(int(node))[1] if y else None for x, y in zip(all_methods, methods) for node in range(1, len(graph.matrix) + 1)]
        NN_list = NO_IMPROVEMENT[: len(graph.matrix)]
        NI_list = NO_IMPROVEMENT[len(graph.matrix): len(graph.matrix) * 2]
        Fletcher_list = NO_IMPROVEMENT[len(graph.matrix) * 2: len(graph.matrix) * 3]
        Fletcher_Clarke_list = NO_IMPROVEMENT[len(graph.matrix) * 3: len(graph.matrix) * 4]

        ER_IMPROVEMENT = [graph.ER(x(int(node))[0], x(int(node))[1])[1] if y else None for x, y in zip(all_methods, methods[4:8]) for node in range(1, len(graph.matrix) + 1)]
        NN_ER_list = ER_IMPROVEMENT[: len(graph.matrix)]
        NI_ER_list = ER_IMPROVEMENT[len(graph.matrix): len(graph.matrix) * 2]
        Fletcher_ER_list = ER_IMPROVEMENT[len(graph.matrix) * 2: len(graph.matrix) * 3]
        Fletcher_Clarke_ER_list = ER_IMPROVEMENT[len(graph.matrix) * 3: len(graph.matrix) * 4]

        OPT_IMPROVEMENT = [graph.OPT(x(int(node))[0], x(int(node))[1])[1] if y else None for x, y in zip(all_methods, methods[8:12]) for node in range(1, len(graph.matrix) + 1)]
        NN_OPT_list = OPT_IMPROVEMENT[: len(graph.matrix)]
        NI_OPT_list = OPT_IMPROVEMENT[len(graph.matrix): len(graph.matrix) * 2]
        Fletcher_OPT_list = OPT_IMPROVEMENT[len(graph.matrix) * 2: len(graph.matrix) * 3]
        Fletcher_Clarke_OPT_list = OPT_IMPROVEMENT[len(graph.matrix) * 3: len(graph.matrix) * 4]

        EROPT_IMPROVEMENT = [graph.OPT(graph.ER(x(int(node))[0], x(int(node))[1])[0], graph.ER(x(int(node))[0], x(int(node))[1])[1])[1] if y else None for x, y in zip(all_methods, methods[12:16]) for node in range(1, len(graph.matrix) + 1)]
        NN_EROPT_list = EROPT_IMPROVEMENT[: len(graph.matrix)]
        NI_EROPT_list = EROPT_IMPROVEMENT[len(graph.matrix): len(graph.matrix) * 2]
        Fletcher_EROPT_list = EROPT_IMPROVEMENT[len(graph.matrix) * 2: len(graph.matrix) * 3]
        Fletcher_Clarke_EROPT_list = EROPT_IMPROVEMENT[len(graph.matrix) * 3: len(graph.matrix) * 4]

        OPTER_IMPROVEMENT = [graph.ER(graph.OPT(x(int(node))[0], x(int(node))[1])[0], graph.OPT(x(int(node))[0], x(int(node))[1])[1])[1] if y else None for x, y in zip(all_methods, methods[16:20]) for node in range(1, len(graph.matrix) + 1)]
        NN_OPTER_list = OPTER_IMPROVEMENT[: len(graph.matrix)]
        NI_OPTER_list = OPTER_IMPROVEMENT[len(graph.matrix): len(graph.matrix) * 2]
        Fletcher_OPTER_list = OPTER_IMPROVEMENT[len(graph.matrix) * 2: len(graph.matrix) * 3]
        Fletcher_Clarke_OPTER_list = OPTER_IMPROVEMENT[len(graph.matrix) * 3: len(graph.matrix) * 4]

        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 2, text = 'NO LOCAL IMPROVEMENT', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 5, text = 'ER IMPROVEMENT', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 2, text = '2-OPT IMPROVEMENT', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 5, text = '2-OPT IMPROVEMENT AFTER ER', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 6, self.HEIGHT // 8 * 2, text = 'ER IMPROVEMENT AFTER 2-OPT', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)

        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 2 + 30, text = f'Nearest Neighbor: {min(NN_list) if all(NN_list) else None} / {NN_list.index(min(NN_list)) + 1 if all(NN_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 2 + 50, text = f'Nearest Insertion: {min(NI_list) if all(NI_list) else None} / {NI_list.index(min(NI_list)) + 1 if all(NI_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 2 + 70, text = f'Fletcher: {min(Fletcher_list) if all(Fletcher_list) else None} / {Fletcher_list.index(min(Fletcher_list)) + 1 if all(Fletcher_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 2 + 90, text = f'Fletcher & Clarke: {min(Fletcher_Clarke_list) if all(Fletcher_Clarke_list) else None} / {Fletcher_Clarke_list.index(min(Fletcher_Clarke_list)) + 1 if all(Fletcher_Clarke_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 5 + 30, text = f'Nearest Neighbor: {min(NN_ER_list) if all(NN_ER_list) else None} / {NN_ER_list.index(min(NN_ER_list)) + 1 if all(NN_ER_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 5 + 50, text = f'Nearest Insertion: {min(NI_ER_list) if all(NI_ER_list) else None} / {NI_ER_list.index(min(NI_ER_list)) + 1 if all(NI_ER_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 5 + 70, text = f'Fletcher: {min(Fletcher_ER_list) if all(Fletcher_ER_list) else None} / {Fletcher_ER_list.index(min(Fletcher_ER_list)) + 1 if all(Fletcher_ER_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 2, self.HEIGHT // 8 * 5 + 90, text = f'Fletcher & Clarke: {min(Fletcher_Clarke_ER_list) if all(Fletcher_Clarke_ER_list) else None} / {Fletcher_Clarke_ER_list.index(min(Fletcher_Clarke_ER_list)) + 1 if all(Fletcher_Clarke_ER_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 2 + 30, text = f'Nearest Neighbor: {min(NN_OPT_list) if all(NN_OPT_list) else None} / {NN_OPT_list.index(min(NN_OPT_list)) + 1 if all(NN_OPT_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 2 + 50, text = f'Nearest Insertion: {min(NI_OPT_list) if all(NI_OPT_list) else None} / {NI_OPT_list.index(min(NI_OPT_list)) + 1 if all(NI_OPT_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 2 + 70, text = f'Fletcher: {min(Fletcher_OPT_list) if all(Fletcher_OPT_list) else None} / {Fletcher_OPT_list.index(min(Fletcher_OPT_list)) + 1 if all(Fletcher_OPT_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 2 + 90, text = f'Fletcher & Clarke: {min(Fletcher_Clarke_OPT_list) if all(Fletcher_Clarke_OPT_list) else None} / {Fletcher_Clarke_OPT_list.index(min(Fletcher_Clarke_OPT_list)) + 1 if all(Fletcher_Clarke_OPT_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 5 + 30, text = f'Nearest Neighbor: {min(NN_EROPT_list) if all(NN_EROPT_list) else None} / {NN_EROPT_list.index(min(NN_EROPT_list)) + 1 if all(NN_EROPT_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 5 + 50, text = f'Nearest Insertion: {min(NI_EROPT_list) if all(NI_EROPT_list) else None} / {NI_EROPT_list.index(min(NI_EROPT_list)) + 1 if all(NI_EROPT_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 5 + 70, text = f'Fletcher: {min(Fletcher_EROPT_list) if all(Fletcher_EROPT_list) else None} / {Fletcher_EROPT_list.index(min(Fletcher_EROPT_list)) + 1 if all(Fletcher_EROPT_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 4, self.HEIGHT // 8 * 5 + 90, text = f'Fletcher & Clarke: {min(Fletcher_Clarke_EROPT_list) if all(Fletcher_Clarke_EROPT_list) else None} / {Fletcher_Clarke_EROPT_list.index(min(Fletcher_Clarke_EROPT_list)) + 1 if all(Fletcher_Clarke_EROPT_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 6, self.HEIGHT // 8 * 2 + 30, text = f'Nearest Neighbor: {min(NN_OPTER_list) if all(NN_OPTER_list) else None} / {NN_OPTER_list.index(min(NN_OPTER_list)) + 1 if all(NN_OPTER_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 6, self.HEIGHT // 8 * 2 + 50, text = f'Nearest Insertion: {min(NI_OPTER_list) if all(NI_OPTER_list) else None} / {NI_OPTER_list.index(min(NI_OPTER_list)) + 1 if all(NI_OPTER_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 6, self.HEIGHT // 8 * 2 + 70, text = f'Fletcher: {min(Fletcher_OPTER_list) if all(Fletcher_OPTER_list) else None} / {Fletcher_OPTER_list.index(min(Fletcher_OPTER_list)) + 1 if all(Fletcher_OPTER_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)
        self.create_text(self.WIDTH // 8 * 6, self.HEIGHT // 8 * 2 + 90, text = f'Fletcher & Clarke: {min(Fletcher_Clarke_OPTER_list) if all(Fletcher_Clarke_OPTER_list) else None} / {Fletcher_Clarke_OPTER_list.index(min(Fletcher_Clarke_OPTER_list)) + 1 if all(Fletcher_Clarke_OPTER_list) else None}', font = ('Arial', int(10 / 2048 * self.SW)), fill = 'white', anchor = NW)

    def plot(self, graph, node, all_methods, NO_IMPROVEMENT, ER_IMPROVEMENT, OPT_IMPROVEMENT, EROPT_IMPROVEMENT, OPTER_IMPROVEMENT):
        # plot the graph with the path, and starting node in red (only possible if you chose a specific starting node)
        NAME = ['Nearest Neighbor', 'Nearest Insertion', 'Fletcher', 'Fletcher & Clarke']

        for x, item in enumerate(NO_IMPROVEMENT):
            if item:
                graph.plot_solution(all_methods[x](node)[0], node, f'{NAME[x]} No local improvement')

        for x, item in enumerate(ER_IMPROVEMENT):
            if item:
                graph.plot_solution(graph.ER(all_methods[x](node)[0], all_methods[x](node)[1])[0], node, f'{NAME[x]} ER improvement')

        for x, item in enumerate(OPT_IMPROVEMENT):
            if item:
                graph.plot_solution(graph.OPT(all_methods[x](node)[0], all_methods[x](node)[1])[0], node, f'{NAME[x]} 2-OPT improvement')

        for x, item in enumerate(EROPT_IMPROVEMENT):
            if item:
                graph.plot_solution(graph.OPT(graph.ER(all_methods[x](node)[0], all_methods[x](node)[1])[0], graph.ER(all_methods[x](node)[0], all_methods[x](node)[1])[1])[0], node, f'{NAME[x]} 2-OPT improvement after ER')

        for x, item in enumerate(OPTER_IMPROVEMENT):
            if item:
                graph.plot_solution(graph.ER(graph.OPT(all_methods[x](node)[0], all_methods[x](node)[1])[0], graph.OPT(all_methods[x](node)[0], all_methods[x](node)[1])[1])[0], node, f'{NAME[x]} ER improvement after 2-OPT')

        plt.show()

    def menu(self, select_btn):
        # return to the main menu
        try: self.plot_btn.destroy()
        except: pass
        select_btn.destroy()
        self.delete('all')
        self.draw_board()
        self.buttons_layout()
