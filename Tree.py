import tkinter as tk

class AgacDugumu:
    def __init__(self, karakter=None):
        self.karakter = karakter
        self.children = {}
        self.is_end = False

class TreeClass:
    def __init__(self):
        self.root = AgacDugumu()

    def ekle(self, mail):
        current_node = self.root
        for karakter in mail:
            if karakter not in current_node.children:
                current_node.children[karakter] = AgacDugumu(karakter)
            current_node = current_node.children[karakter]
        current_node.is_end = True

    def gorsellestir(self, canvas, node=None, x=950, y=50, x_space=90, y_space=70, depth=0, current_address=""):
        if node is None:
            node = self.root

        radius = 18

        if node.is_end:
            canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="lightblue")
            canvas.create_text(x, y, text=current_address, font=("Helvetica", 10, "bold"), fill="green")
        else:
            canvas.create_text(x, y, text=node.karakter, font=("Helvetica", 10, "bold"), fill="red")

        if node.children:
            y_child = y + y_space
            x_child_start = x - (len(node.children) - 1) * x_space / 2
            for i, (karakter, child_node) in enumerate(node.children.items()):
                x_child = x_child_start + i * x_space
                canvas.create_line(x, y, x_child, y_child, fill="black")
                self.gorsellestir(canvas, child_node, x_child, y_child, x_space, y_space, depth + 1,
                                  current_address + karakter)

treenoun = TreeClass()

treenoun.ekle("ali")
treenoun.ekle("arda")
treenoun.ekle("deniz")
treenoun.ekle("derya")
treenoun.ekle("demir")
treenoun.ekle("halil")
treenoun.ekle("hakan")
treenoun.ekle("cem")
treenoun.ekle("gizem")
treenoun.ekle("göksü")
treenoun.ekle("onur")
treenoun.ekle("uğur")
treenoun.ekle("tarık")
treenoun.ekle("fehmi")
treenoun.ekle("bahadır")
treenoun.ekle("utku")
treenoun.ekle("murat")
treenoun.ekle("ahmet")
treenoun.ekle("emre")
treenoun.ekle("pelin")
treenoun.ekle("görkem")
treenoun.ekle("eren")
treenoun.ekle("batu")
treenoun.ekle("batuhan")
treenoun.ekle("emir")
treenoun.ekle("gani")
treenoun.ekle("kenan")
treenoun.ekle("ece")
treenoun.ekle("bilge")
treenoun.ekle("buse")
treenoun.ekle("gamze")
treenoun.ekle("yasemin")
treenoun.ekle("serdar")
treenoun.ekle("serhat")
treenoun.ekle("ömer")
treenoun.ekle("kadir")

root = tk.Tk()
root.title("Ağacı Görselleştirme")

canvas = tk.Canvas(root, width=1800, height=900)
canvas.pack()

treenoun.gorsellestir(canvas)

root.mainloop()