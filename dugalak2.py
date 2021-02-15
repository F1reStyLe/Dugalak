import tkinter as tk

win = tk.Tk()

win.title('Dugalak')
win.geometry("800x640-100-100")

def dilute(viscozity_now,viscozity_need,react_volume):
    return react_volume * (viscozity_now/viscozity_need - 1) / 12

def over_dilute(viscozity_now,viscozity_need,react_volume,stirol_in_react,resin_in_react):
    stirol_over = abs(dilute(viscozity_now,viscozity_need,react_volume))
    return stirol_over / stirol_in_react * resin_in_react

def aerosyl_needed(viscozity_now,viscozity_need,react_volume):
    return abs(dilute(viscozity_now, viscozity_need, react_volume) / 10 * 0.8)

def hydroquinone_needed(gel_now, gel_need,nox,react_volume):
    step_nox = 1.3 - nox/10
    step = 0
    while gel_now < gel_need:
        gel_now = gel_now * step_nox
        step += 10
    return react_volume / 1100 * step

def cobalt_needed(gel_now, gel_need, react_volume, nox):
    gel_diff = gel_now / gel_need
    return (react_volume / 1200 * (gel_diff - 1))/(2/nox)

def Clear_All():
    label_viscozity_need.grid_forget()
    label_viscozity_now.grid_forget()
    label_gel_now.grid_forget()
    label_gel_need.grid_forget()
    label_react_volume.grid_forget()
    label_answer_Co.grid_forget()
    label_answer_hydro.grid_forget()
    label_nox.grid_forget()
    label_answer_styrol.grid_forget()
    label_answer_resin.grid_forget()
    label_stirol_in_react.grid_forget()
    label_resin_in_react.grid_forget()
    label_answer_aerosyl.grid_forget()

    viscozity_now.grid_forget()
    viscozity_need.grid_forget()
    gel_now.grid_forget()
    gel_need.grid_forget()
    react_volume.grid_forget()
    answer.grid_forget()
    nox.grid_forget()
    stirol_in_react.grid_forget()
    resin_in_react.grid_forget()

    react_volume.delete(0, 'end')
    stirol_in_react.delete(0,'end')
    resin_in_react.delete(0, 'end')
    viscozity_now.delete(0, 'end')
    viscozity_need.delete(0, 'end')
    gel_now.delete(0, 'end')
    gel_need.delete(0, 'end')
    nox.delete(0, 'end')

    btn_calc.grid_forget()
    btn_calc_viscozity.grid_forget()
    btn_calc_viscozity_tix.grid_forget()

def choise_viscozity_method():
    Clear_All()
    label_react_volume.grid(row=1, column=0)
    label_viscozity_now.grid(row=2, column=0)
    label_viscozity_need.grid(row=3, column=0)

    react_volume.grid(row=1, column=1)
    viscozity_now.grid(row=2, column=1)
    viscozity_need.grid(row=3, column=1)

    btn_calc_viscozity.grid(row=6, column=0)

def choise_viscozity_method_over():
    Clear_All()
    label_react_volume.grid(row=1, column=0)
    label_viscozity_now.grid(row=2, column=0)
    label_viscozity_need.grid(row=3, column=0)
    label_resin_in_react.grid(row=4, column=0)
    label_stirol_in_react.grid(row=5, column=0)

    react_volume.grid(row=1, column=1)
    viscozity_now.grid(row=2, column=1)
    viscozity_need.grid(row=3, column=1)
    resin_in_react.grid(row=4, column=1)
    stirol_in_react.grid(row=5, column=1)

    btn_calc_viscozity.grid(row=6, column=0)

def choise_viscozity_tix_method():
    Clear_All()
    label_react_volume.grid(row=1, column=0)
    label_viscozity_now.grid(row=2, column=0)
    label_viscozity_need.grid(row=3, column=0)

    react_volume.grid(row=1, column=1)
    viscozity_now.grid(row=2, column=1)
    viscozity_need.grid(row=3, column=1)

    btn_calc_viscozity_tix.grid(row=6, column=0)

def choise_gel_method():
    Clear_All()
    label_react_volume.grid(row=1, column=0)
    react_volume.grid(row=1, column=1)
    label_gel_now.grid(row=2, column=0)
    gel_now.grid(row=2, column=1)
    label_gel_need.grid(row=3, column=0)
    gel_need.grid(row=3, column=1)
    btn_calc.grid(row=5, column=0)
    label_nox.grid(row=4, column=0)
    nox.grid(row=4, column=1)


def Choise_gel():
    answer.delete(0, 'end')
    if int(gel_now.get()) < int(gel_need.get()):
        result = hydroquinone_needed(int(gel_now.get()), int(gel_need.get()), int(nox.get()), int(react_volume.get()))
        answer.grid(row=6, column=1)
        label_answer_hydro.grid(row=6, column=0)
        answer.insert(0, '{:.0f}'.format(result))
    elif int(gel_now.get()) > int(gel_need.get()):
        result = cobalt_needed(int(gel_now.get()), int(gel_need.get()), int(react_volume.get()), int(nox.get()))
        answer.grid(row=6, column=1)
        label_answer_Co.grid(row = 6, column = 0)
        answer.insert(0, '{:.3f}'.format(result))


def Choise_viscozity():
    answer.delete(0, 'end')
    if int(viscozity_need.get()) < int(viscozity_now.get()):
        result = dilute(int(viscozity_now.get()),int(viscozity_need.get()),int(react_volume.get()))
        answer.grid(row = 7, column = 1)
        label_answer_styrol.grid(row = 7, column = 0)
        answer.insert(0, '{:.0f}'.format(result))
    elif int(viscozity_need.get()) > int(viscozity_now.get()):
        result = over_dilute(int(viscozity_now.get()), int(viscozity_need.get()), int(react_volume.get()), int(stirol_in_react.get()), int(resin_in_react.get()))
        answer.grid(row=7, column=1)
        label_answer_resin.grid(row=7, column=0)
        answer.insert(0, '{:.0f}'.format(result))

def Choise_viscozity_tix():
    answer.delete(0, 'end')
    if int(viscozity_need.get()) < int(viscozity_now.get()):
        result = dilute(int(viscozity_now.get()),int(viscozity_need.get()),int(react_volume.get()))
        answer.grid(row = 7, column = 1)
        label_answer_styrol.grid(row = 7, column = 0)
        answer.insert(0, '{:.0f}'.format(result))
    elif int(viscozity_need.get()) > int(viscozity_now.get()):
        result = aerosyl_needed(int(viscozity_now.get()), int(viscozity_need.get()), int(react_volume.get()))
        answer.grid(row=7, column=1)
        label_answer_aerosyl.grid(row=7, column=0)
        answer.insert(0, '{:.1f}'.format(result))

viscozity_now = tk.Entry(win)
viscozity_need = tk.Entry(win)
gel_now = tk.Entry(win)
gel_need = tk.Entry(win)
nox = tk.Entry(win)
react_volume = tk.Entry(win)
stirol_in_react = tk.Entry(win)
resin_in_react = tk.Entry(win)
answer = tk.Entry(win)

label_viscozity_need = tk.Label(win, text='Введите необходимую вязкость:')
label_viscozity_now = tk.Label(win, text='Введите вязкость:')
label_gel_now = tk.Label(win, text = 'Введите время желатинизации:')
label_gel_need = tk.Label(win, text = 'Введите необходимое время желатинизации:')
label_react_volume = tk.Label(win, text = 'Введите объем загрузки:')
label_answer_Co = tk.Label(win, text = 'Необходимо добавить Co12%(кг.):')
label_answer_hydro = tk.Label(win, text = 'Необходимо добавить гидрохинона(г.):')
label_nox = tk.Label(win, text = 'Количество отвердителя:')
label_stirol_in_react = tk.Label(win, text = 'Количество стирола в загрузке:')
label_resin_in_react = tk.Label(win, text = 'Количество смолы в загрузке:')
label_answer_styrol = tk.Label(win, text = 'Необходимо добавить стирола(кг.):')
label_answer_resin = tk.Label(win, text = 'Необходимо добавить смолы(кг.)')
label_answer_aerosyl = tk.Label(win, text = 'Необходимо добавить аэросила(кг.):')

btn_lami = tk.Button(win, text = 'Вязкость высокая:', command = choise_viscozity_method)
btn_lami_over = tk.Button(win, text = 'Вязкость низкая', command = choise_viscozity_method_over)
btn_tixo = tk.Button(win, text = 'Вязкость тиксотропная:', command = choise_viscozity_tix_method)
btn_gel = tk.Button(win, text = 'Желатинизация:', command = choise_gel_method)
btn_lami.grid(row = 0, column = 0, stick = 'we')
btn_lami_over.grid(row = 0, column = 1, stick = 'we')
btn_tixo.grid(row = 0, column = 2, stick = 'we')
btn_gel.grid(row = 0, column = 3, stick = 'we')
btn_calc = tk.Button(win, text = 'Рассчитать', command = Choise_gel)
btn_calc_viscozity = tk.Button(win, text = 'Рассчитать', command = Choise_viscozity)
btn_calc_viscozity_tix = tk.Button(win, text = 'Рассчитать', command = Choise_viscozity_tix)
win.mainloop()