import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from calculations import get_solutions_info, calculate_total_errors


class GUI:
    def __init__(self):
        self._init_window()

        self.root.mainloop()

    def _init_user_input_frame(self):
        frame_top = tk.Frame(self.root, bg='#ffe0e0', bd=5)
        frame_top.place(relx=0.0, rely=0.0, relwidth=0.20, relheight=1)

        # for solution graph
        self.x0_field = tk.Entry(frame_top, bg='white', font=30)
        self.x0_field.pack()
        x0_btn = tk.Button(frame_top, text='set x0', command=self.update_final_report)
        x0_btn.pack()

        self.y0_field = tk.Entry(frame_top, bg='white', font=30)
        self.y0_field.pack()
        y0_btn = tk.Button(frame_top, text='set y0', command=self.update_final_report)
        y0_btn.pack()

        self.X_field = tk.Entry(frame_top, bg='white', font=30)
        self.X_field.pack()
        X_btn = tk.Button(frame_top, text='set X', command=self.update_final_report)
        X_btn.pack()

        self.N_field = tk.Entry(frame_top, bg='white', font=30)
        self.N_field.pack()
        N_btn = tk.Button(frame_top, text='set N', command=self.update_final_report)
        N_btn.pack()

        self.start_x_grid_field = tk.Entry(frame_top, bg='white', font=30)
        self.start_x_grid_field.pack()
        start_x_grid_btn = tk.Button(frame_top, text='set start x on grid', command=self.update_final_report)
        start_x_grid_btn.pack()

        self.end_x_grid_field = tk.Entry(frame_top, bg='white', font=30)
        self.end_x_grid_field.pack()
        end_x_grid_btn = tk.Button(frame_top, text='set end x on grid', command=self.update_final_report)
        end_x_grid_btn.pack()

        self.start_y_grid_field = tk.Entry(frame_top, bg='white', font=30)
        self.start_y_grid_field.pack()
        start_y_grid_btn = tk.Button(frame_top, text='set start y on grid', command=self.update_final_report)
        start_y_grid_btn.pack()

        self.end_y_grid_field = tk.Entry(frame_top, bg='white', font=30)
        self.end_y_grid_field.pack()
        end_y_grid_btn = tk.Button(frame_top, text='set end y on grid', command=self.update_final_report)
        end_y_grid_btn.pack()

        # for total error graph
        self.start_step_TE_field = tk.Entry(frame_top, bg='white', font=30)
        self.start_step_TE_field.pack()
        start_step_TE_btn = tk.Button(frame_top, text='set total error steps start', command=self.update_final_report)
        start_step_TE_btn.pack()

        self.end_step_TE_field = tk.Entry(frame_top, bg='white', font=30)
        self.end_step_TE_field.pack()
        end_step_TE_btn = tk.Button(frame_top, text='set total error steps end', command=self.update_final_report)
        end_step_TE_btn.pack()

        self.start_n_TE_field = tk.Entry(frame_top, bg='white', font=30)
        self.start_n_TE_field.pack()
        start_n_TE_btn = tk.Button(frame_top, text='set start number of steps on TE grid',
                                   command=self.update_final_report)
        start_n_TE_btn.pack()

        self.end_n_TE_field = tk.Entry(frame_top, bg='white', font=30)
        self.end_n_TE_field.pack()
        end_n_TE_btn = tk.Button(frame_top, text='set end number of steps on TE grid', command=self.update_final_report)
        end_n_TE_btn.pack()

        self.start_TE_field = tk.Entry(frame_top, bg='white', font=30)
        self.start_TE_field.pack()
        start_TE_btn = tk.Button(frame_top, text='set start TE on TE grid', command=self.update_final_report)
        start_TE_btn.pack()

        self.end_TE_field = tk.Entry(frame_top, bg='white', font=30)
        self.end_TE_field.pack()
        end_TE_btn = tk.Button(frame_top, text='set end TE on TE grid', command=self.update_final_report)
        end_TE_btn.pack()

        # for local error graph
        self.start_x_LE_field = tk.Entry(frame_top, bg='white', font=30)
        self.start_x_LE_field.pack()
        start_x_LE_btn = tk.Button(frame_top, text='set start x on LE grid', command=self.update_final_report)
        start_x_LE_btn.pack()

        self.end_x_LE_field = tk.Entry(frame_top, bg='white', font=30)
        self.end_x_LE_field.pack()
        end_x_LE_btn = tk.Button(frame_top, text='set end x on LE grid', command=self.update_final_report)
        end_x_LE_btn.pack()

        self.start_LE_field = tk.Entry(frame_top, bg='white', font=30)
        self.start_LE_field.pack()
        start_LE_btn = tk.Button(frame_top, text='set start LE on LE grid', command=self.update_final_report)
        start_LE_btn.pack()

        self.end_LE_field = tk.Entry(frame_top, bg='white', font=30)
        self.end_LE_field.pack()
        end_LE_btn = tk.Button(frame_top, text='set end LE on LE grid', command=self.update_final_report)
        end_LE_btn.pack()

    def _init_graph_values(self):
        self.x0 = 1
        self.y0 = 0.5
        self.X = 9
        self.N = 10

        self.start_x_grid = 1
        self.end_x_grid = 9
        self.start_y_grid = 0
        self.end_y_grid = 0.5

        self.start_step_TE = 1
        self.end_step_TE = 10
        self.start_n_TE = 1
        self.end_n_TE = 10
        self.start_TE_TE = -0.1
        self.end_TE_TE = 1.6

        self.start_x_LE = 1
        self.end_x_LE = 9
        self.start_LE_LE = -0.005
        self.end_LE_LE = 0.06

    def _init_final_report_frame(self):
        self.final_report = tk.Frame(self.root, bg='#e0e0ff', bd=5)
        self.final_report.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1)

        self._init_graph_values()

        self.update_final_report()

    def _init_window(self):
        self.root = tk.Tk()
        self.root.title('Computational practicum GUI')
        self.root.geometry('1150x900')
        self.root.resizable(width=False, height=False)

        self._init_user_input_frame()

        self._init_final_report_frame()

    def _read_input(self):
        try:
            self.x0 = float(self.x0_field.get())
        except:
            pass
        try:
            self.y0 = float(self.y0_field.get())
        except:
            pass
        try:
            self.X = float(self.X_field.get())
        except:
            pass
        try:
            self.N = float(self.N_field.get())
        except:
            pass
        try:
            self.start_x_grid = float(self.start_x_grid_field.get())
        except:
            pass
        try:
            self.end_x_grid = float(self.end_x_grid_field.get())
        except:
            pass
        try:
            self.start_y_grid = float(self.start_y_grid_field.get())
        except:
            pass
        try:
            self.end_y_grid = float(self.end_y_grid_field.get())
        except:
            pass
        try:
            self.start_step_TE = int(self.start_step_TE_field.get())
        except:
            pass
        try:
            self.end_step_TE = int(self.end_step_TE_field.get())
        except:
            pass

        try:
            self.start_n_TE = float(self.start_n_TE_field.get())
        except:
            pass
        try:
            self.end_n_TE = float(self.end_n_TE_field.get())
        except:
            pass
        try:
            self.start_TE_TE = float(self.start_TE_field.get())
        except:
            pass
        try:
            self.end_TE_TE = float(self.end_TE_field.get())
        except:
            pass
        try:
            self.start_x_LE = float(self.start_x_LE_field.get())
        except:
            pass
        try:
            self.end_x_LE = float(self.end_x_LE_field.get())
        except:
            pass
        try:
            self.start_LE_LE = float(self.start_LE_field.get())
        except:
            pass
        try:
            self.end_LE_LE = float(self.end_LE_field.get())
        except:
            pass

    def update_final_report(self):
        self._read_input()

        exact_d, euler_d, imp_euler_d, RK_d = get_solutions_info(x0=self.x0, y0=self.y0, X=self.X, step_number=self.N)
        euler_total_err, imp_euler_total_err, RK_total_err = calculate_total_errors(x0=self.x0, y0=self.y0, X=self.X,
                                                                                    step_range_start=self.start_step_TE,
                                                                                    step_range_end=self.end_step_TE)

        for widget in self.final_report.winfo_children():
            widget.destroy()

        fin_rep_label = tk.Label(self.final_report, text='Final report', font=40)
        fin_rep_label.pack()

        figure = plt.Figure(figsize=(8, 8), dpi=100)

        ax1 = figure.add_subplot(221)
        ax5 = figure.add_subplot(222)
        ax8 = figure.add_subplot(223)


        ax1.title.set_text('Solution')
        ax1.plot(exact_d['x'], exact_d['y(exact)'], marker='o', label='Exact')
        ax1.plot(exact_d['x'], euler_d['y(Euler)'], marker='o', label="Euler's")
        ax1.plot(exact_d['x'], imp_euler_d['y(ImpEuler)'], marker='o', label="Improved Euler's")
        ax1.plot(exact_d['x'], RK_d['y(RK)'], marker='o', label="Runge-Kutta")
        ax1.set_xlabel("x")
        ax1.set_ylabel("y")
        ax1.legend()
        ax1.set_xlim(float(self.start_x_grid), float(self.end_x_grid))
        ax1.set_ylim(float(self.start_y_grid), float(self.end_y_grid))

        ax5.title.set_text("Local errors")
        ax5.plot(euler_d['x'], euler_d['LTE'], marker='o', label="Euler's")
        ax5.plot(euler_d['x'], imp_euler_d['LTE'], marker='o', label="Improved Euler's")
        ax5.plot(euler_d['x'], RK_d['LTE'], marker='o', label="Runge-Kutta")
        ax5.set_xlabel("x")
        ax5.set_ylabel("local error")
        ax5.legend()
        ax5.set_xlim(float(self.start_x_LE), float(self.end_x_LE))
        ax5.set_ylim(float(self.start_LE_LE), float(self.end_LE_LE))

        ax8.title.set_text("Total errors on given interval")
        ax8.plot(euler_total_err['ns'], euler_total_err['TE'], marker='o', label="Euler's")
        ax8.plot(euler_total_err['ns'], imp_euler_total_err['TE'], marker='o', label="Improved Euler's")
        ax8.plot(euler_total_err['ns'], RK_total_err['TE'], marker='o', label="Runge-Kutta")
        ax8.set_xlabel("number of steps")
        ax8.set_ylabel("max GTE")
        ax8.legend()
        ax8.set_xlim(float(self.start_n_TE), float(self.end_n_TE))
        ax8.set_ylim(float(self.start_TE_TE), float(self.end_TE_TE))

        figure.tight_layout(pad=2.0)

        chart_type = FigureCanvasTkAgg(figure, self.final_report)
        chart_type.get_tk_widget().pack()
