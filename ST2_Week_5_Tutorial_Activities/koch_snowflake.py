from tkinter import *
import math

class KochSnowflake:
    def __init__(self):
        window = Tk()
        window.title("Koch Snowflake")

        self.width = 700
        self.height = 650

        self.canvas = Canvas(window, width=self.width, height=self.height, bg="white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        Label(frame, text="Enter an order: ").pack(side=LEFT)
        self.order = StringVar()
        Entry(frame, textvariable=self.order, justify=RIGHT).pack(side=LEFT)
        Button(frame, text="Display Koch Snowflake", command=self.display).pack(side=LEFT)

        window.mainloop()

    def display(self):
        self.canvas.delete("line")

        # Equilateral triangle points
        p1 = (150, 500)
        p2 = (550, 500)
        height = (math.sqrt(3) / 2) * (p2[0] - p1[0])
        p3 = ((p1[0] + p2[0]) / 2, 500 - height)

        order = int(self.order.get())

        self.draw_koch(order, p1, p2)
        self.draw_koch(order, p2, p3)
        self.draw_koch(order, p3, p1)

    def draw_koch(self, order, p1, p2):
        if order == 0:
            self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], tags="line")
        else:
            x1, y1 = p1
            x5, y5 = p2

            x2 = x1 + (x5 - x1) / 3
            y2 = y1 + (y5 - y1) / 3

            x4 = x1 + 2 * (x5 - x1) / 3
            y4 = y1 + 2 * (y5 - y1) / 3

            dx = x4 - x2
            dy = y4 - y2

            angle = math.radians(60)
            x3 = x2 + dx * math.cos(angle) - dy * math.sin(angle)
            y3 = y2 + dx * math.sin(angle) + dy * math.cos(angle)

            self.draw_koch(order - 1, (x1, y1), (x2, y2))
            self.draw_koch(order - 1, (x2, y2), (x3, y3))
            self.draw_koch(order - 1, (x3, y3), (x4, y4))
            self.draw_koch(order - 1, (x4, y4), (x5, y5))


KochSnowflake()