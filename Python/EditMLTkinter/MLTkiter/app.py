from tkinter import Frame, LabelFrame, StringVar, IntVar, Label, Tk, Entry, Button, TclError, Scrollbar,Toplevel, Canvas, Checkbutton, Radiobutton
from tkinter.constants import *
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, mean_absolute_error,mean_squared_error
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

class MachineLearning:
    def __init__(self):
        self.data = None
        self.selection_x = None
        self.table = None
        self.selection_y = None
        self.X = None     self.y = None
        self.X_test_l = None
        self.X_train_l = None
        self.y_test_l = None
        self.y_train_l = None
        self.X_test = None
        self.X_train = None
        self.y_test = None
        self.y_train = None
        self.le = LabelEncoder()

        self.linreg_model = None
        self.linreg_predictions = None
        self.logreg_model = None
        self.logreg_predictions = None
        self.dtree_model = None
        self.dtree_predictions = None
        self.rforest_model = None
        self.rforest_predictions = None

        self.window = Tk()
        self.color = 'grey95'
        self.window.geometry('620x700')
        self.window.resizable(False, False)
        self.window.configure(background=self.color)
        self.window.title('Machine Learning')
        self.window.iconbitmap('py.ico')

        # Heading
        self.heading = Label(self.window, text='Machine Learning', bg=self.color, pady=20, font=('Helvetica'
, 35, 'bold'))
        self.heading.place(width=620, height=100, bordermode=OUTSIDE, x=0, y=0)


        # File Selection and viewing
        self.frame = LabelFrame(self.window, text='File Selection', bg=self.color)
        self.frame.place(width=580, height=80, bordermode=OUTSIDE, x=20, y=100)

        self.name_label = Label(self.frame, text='File Name : ', bg=self.color, padx=10, pady=10,
font=('Helvetica', 15))
        self.name_label.place(width=120, height=30, bordermode=INSIDE, x=10, y=13)

        self.name = StringVar()
        self.name_entry = Entry(self.frame, exportselection=False, textvariable=self.name, font=('Helvetica', 12))
        self.name_entry.place(width=250, height=30, bordermode=INSIDE, x=130, y=13)

        self.name_select = Button(self.frame, text='Select', command=lambda: self.select())
        self.name_select.place(width=50, height=30, bordermode=INSIDE, x=395, y=13)

        self.df_show = Button(self.frame, text='Show', command=lambda: self.create_table(), state=
DISABLED)

        self.df_show.place(width=50, height=30, bordermode=INSIDE, x=455, y=13)

        self.df_hide = Button(self.frame, text='Hide', command=lambda: self.hide(), state=DISABLED)
        self.df_hide.place(width=50, height=30, bordermode=INSIDE, x=515, y=13)

        # Train Test Split
        self.ttsplit = LabelFrame(self.window, text='Train Test Split', bg=self.color)
        self.ttsplit.place(width=580, height=80, bordermode=OUTSIDE, x=20, y=200)

        self.select_x = Button(self.ttsplit, text='X', command=lambda: self.get_x(), state=DISABLED)
        self.select_x.place(width=80, height=30, bordermode=INSIDE, x=10, y=13)

        self.select_y = Button(self.ttsplit, text='y', command=lambda: self.get_y(), state=DISABLED)
        self.select_y.place(width=80, height=30, bordermode=INSIDE, x=100, y=13)

        self.test_size_label = Label(self.ttsplit, text='Test Size : ', bg=self.color)
        self.test_size_label.place(width=60, height=30, bordermode=INSIDE, x=200, y=13)

        self.test_size = StringVar()
        self.test_size.set('0.25')
        self.test_size_entry = Entry(self.ttsplit, exportselection=False, textvariable=self.test_size, font=('
Helvetica', 10))

        self.test_size_entry.place(width=50, height=30, bordermode=INSIDE, x=260, y=13)

        self.rstate_label = Label(self.ttsplit, text='Random State : ', bg=self.color)
        self.rstate_label.place(width=100, height=30, bordermode=INSIDE, x=330, y=13)

        self.rstate = StringVar()
        self.rstate.set('None')
        self.rstate_entry = Entry(self.ttsplit, exportselection=False, textvariable=self.rstate, font=('Helvetica
', 10))

        self.rstate_entry.place(width=50, height=30, bordermode=INSIDE, x=430, y=13)

        self.split_button = Button(self.ttsplit, text='Split', command=lambda: self.split(), state=DISABLED)
        self.split_button.place(width=80, height=30, bordermode=INSIDE, x=490, y=13)


        # Linear Regression
105 self.linreg = LabelFrame(self.window, text='Linear Regression', bg=self.color)
106 self.linreg.place(width=580, height=80, bordermode=OUTSIDE, x=20, y=300)
107
self.linreg_pred = Button(self.linreg, text='Predict', command=lambda: self.pred_linreg(), state=
DISABLED)
108
109 self.linreg_pred.place(width=125, height=30, bordermode=INSIDE, x=8, y=13)
110
self.coefficients = Button(self.linreg, text='Coefficients', command=lambda: self.coeff(), state=
DISABLED)
111
112 self.coefficients.place(width=125, height=30, bordermode=INSIDE, x=153, y=13)
113
self.scatter_button = Button(self.linreg, text='Scatter Plot', command=lambda: self.scatter(), state=
DISABLED)
114
115 self.scatter_button.place(width=125, height=30, bordermode=INSIDE, x=298, y=13)
116
self.linreg_error = Button(self.linreg, text='Error', command=lambda: self.errors_linreg(), state=
DISABLED)
117
118 self.linreg_error.place(width=125, height=30, bordermode=INSIDE, x=443, y=13)
119
120 # Logistic Regression
121 self.logreg = LabelFrame(self.window, text='Logistic Regression', bg=self.color)
122 self.logreg.place(width=580, height=80, bordermode=OUTSIDE, x=20, y=400)
123
self.logreg_pred = Button(self.logreg, text='Predict', command=lambda: self.pred_logreg(), state=
DISABLED)
124
125 self.logreg_pred.place(width=125, height=30, bordermode=INSIDE, x=8, y=13)
126
self.logreg_cm = Button(self.logreg, text='Confusion Matrix', command=lambda: self.cm_logreg(),
state=DISABLED)
127
128 self.logreg_cm.place(width=125, height=30, bordermode=INSIDE, x=153, y=13)
129
self.logreg_cr = Button(self.logreg, text='Classification Report', command=lambda: self.cr_logreg(),
state=DISABLED)
130
131 self.logreg_cr.place(width=125, height=30, bordermode=INSIDE, x=298, y=13)
132
self.logreg_error = Button(self.logreg, text='Error', command=lambda: self.errors_logreg(), state=
DISABLED)
133
134 self.logreg_error.place(width=125, height=30, bordermode=INSIDE, x=443, y=13)
135
136 # Decision Tree
137 self.dtree = LabelFrame(self.window, text='Decision Tree', bg=self.color)
138 self.dtree.place(width=580, height=80, bordermode=OUTSIDE, x=20, y=500)
139
self.dtree_pred = Button(self.dtree, text='Predict', command=lambda: self.pred_dtree(), state=
DISABLED)
140
141 self.dtree_pred.place(width=125, height=30, bordermode=INSIDE, x=8, y=13)
142
self.dtree_cm = Button(self.dtree, text='Confusion Matrix', command=lambda: self.cm_dtree(),
state=DISABLED)
143
144 self.dtree_cm.place(width=125, height=30, bordermode=INSIDE, x=153, y=13)
145
self.dtree_cr = Button(self.dtree, text='Classification Report', command=lambda: self.cr_dtree(),
state=DISABLED)
146
147 self.dtree_cr.place(width=125, height=30, bordermode=INSIDE, x=298, y=13)

148
self.dtree_error = Button(self.dtree, text='Error', command=lambda: self.errors_dtree(), state=
DISABLED)
149
150 self.dtree_error.place(width=125, height=30, bordermode=INSIDE, x=443, y=13)
151
152 # Random Forest
153 self.rforest = LabelFrame(self.window, text='Random Forest', bg=self.color)
154 self.rforest.place(width=580, height=80, bordermode=OUTSIDE, x=20, y=600)
155
self.rforest_pred = Button(self.rforest, text='Predict', command=lambda: self.pred_rforest(), state=
DISABLED)
156
157 self.rforest_pred.place(width=125, height=30, bordermode=INSIDE, x=8, y=13)
158
self.rforest_cm = Button(self.rforest, text='Confusion Matrix', command=lambda: self.cm_rforest()
, state=DISABLED)
159
160 self.rforest_cm.place(width=125, height=30, bordermode=INSIDE, x=153, y=13)
161
self.rforest_cr = Button(self.rforest, text='Classification Report', command=lambda: self.cr_rforest
(), state=DISABLED)
162
163 self.rforest_cr.place(width=125, height=30, bordermode=INSIDE, x=298, y=13)
164
self.rforest_error = Button(self.rforest, text='Error', command=lambda: self.errors_rforest(), state=
DISABLED)
165
166 self.rforest_error.place(width=125, height=30, bordermode=INSIDE, x=443, y=13)
167
168 self.window.mainloop()
169
170 def select(self):
171 try:
172 self.data = pd.read_csv(self.name.get())
173 self.df_show['state'] = NORMAL
174 self.df_hide['state'] = NORMAL
175 self.name_entry['state'] = DISABLED
176 self.name_select['state'] = DISABLED
177 self.select_x['state'] = NORMAL
178 except FileNotFoundError:
179 self.name.set('Invalid')
180
181 def create_table(self):
182 try:
183 self.table.window.deiconify()
184 except AttributeError:
185 if self.data.shape[0] > 50:
186 self.table = Table(self.data.head(50), self.window, self.name.get())
187 else:
188 self.table = Table(self.data, self.window, self.name.get())
189 except TclError:
190 if self.data.shape[0] > 50:
191 self.table = Table(self.data.head(50), self.window, self.name.get())
192 else:
193 self.table = Table(self.data, self.window, self.name.get())
194
195 def hide(self):
196 try:
197 self.table.window.withdraw()

198 except TclError:
199 return
200 except AttributeError:
201 return
202
203 def get_x(self):
204 self.selection_x = SelectionX(self.window, self.data)
205 self.X = []
206 for i in range(len(self.data.columns)):
207 if self.selection_x.variables[i].get() == 1:
208 self.X.append(self.data.columns[i])
209
210 self.select_x['state'] = DISABLED
211 self.select_y['state'] = NORMAL
212
213 def get_y(self):
214 self.selection_y = SelectionY(self.window, self.data)
215 self.y = self.data.columns[self.selection_y.variable.get()]
216 if self.y not in self.X:
217 self.split_button['state'] = NORMAL
218 self.select_y['state'] = DISABLED
219
220 def split(self):
221 test_size = 0.25
222 try:
223 test_size = float(self.test_size.get())
224 if test_size <= 0 or test_size >= 1:
225 test_size = 0.25
226 except ValueError:
227 test_size = 0.25
228 self.test_size.set('0.25')
229 random_state = None
230 if self.rstate.get() != 'None':
231 try:
232 random_state = int(self.rstate.get())
233 except ValueError:
234 random_state = None
235 self.rstate.set('None')
236
self.X_train_l, self.X_test_l, self.y_train_l, self.y_test_l = train_test_split(self.data[self.X], self.data[
self.y], test_size=test_size, random_state=random_state)
237
self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.data[self.X], self.le.
fit_transform(self.data[self.y]), test_size=test_size, random_state=random_state)
238
239
240 self.linreg_pred['state'] = NORMAL
241 self.coefficients['state'] = DISABLED
242 self.scatter_button['state'] = DISABLED
243 self.linreg_error['state'] = DISABLED
244
245 self.logreg_pred['state'] = NORMAL
246 self.logreg_cr['state'] = DISABLED
247 self.logreg_cm['state'] = DISABLED
248 self.logreg_error['state'] = DISABLED
249
250 self.dtree_pred['state'] = NORMAL

251 self.dtree_cr['state'] = DISABLED
252 self.dtree_cm['state'] = DISABLED
253 self.dtree_error['state'] = DISABLED
254
255 self.rforest_pred['state'] = NORMAL
256 self.rforest_cm['state'] = DISABLED
257 self.rforest_cr['state'] = DISABLED
258 self.rforest_error['state'] = DISABLED
259
260 def pred_linreg(self):
261 self.linreg_model = LinearRegression()
262 self.linreg_model.fit(self.X_train_l, self.y_train_l)
263 self.linreg_predictions = self.linreg_model.predict(self.X_test_l)
264
265 self.linreg_error['state'] = NORMAL
266 self.scatter_button['state'] = NORMAL
267 self.coefficients['state'] = NORMAL
268
269 def scatter(self):
270 Scatter(self.window, self.y_test_l, self.linreg_predictions)
271
272 def coeff(self):
273 Coefficients(self.window, self.linreg_model.intercept_, self.linreg_model.coef_, self.X)
274
275 def errors_linreg(self):
temp = [mean_absolute_error(self.y_test, self.linreg_predictions), mean_squared_error(self.y_test
, self.linreg_predictions), np.sqrt(mean_squared_error(self.y_test, self.linreg_predictions))]
276
277 Errors(self.window, temp, 'Linear Regression')
278
279 def pred_logreg(self):
280 self.logreg_model = LogisticRegression(solver='liblinear')
281 self.logreg_model.fit(self.X_train, self.y_train)
282 self.logreg_predictions = self.logreg_model.predict(self.X_test)
283
284 self.logreg_cr['state'] = NORMAL
285 self.logreg_cm['state'] = NORMAL
286 self.logreg_error['state'] = NORMAL
287
288 def cm_logreg(self):
ConfusionMatrix(self.window, confusion_matrix(self.le.inverse_transform(self.y_test), self.le.
inverse_transform(self.logreg_predictions)), 'Logistic Regression', self.le.classes_)
289
290
291 def cr_logreg(self):
ClassificationReport(self.window, classification_report(self.le.inverse_transform(self.y_test), self.
le.inverse_transform(self.logreg_predictions)), 'Logistic Regression')
292
293
294 def errors_logreg(self):
temp = [mean_absolute_error(self.y_test, self.logreg_predictions), mean_squared_error(self.
y_test, self.logreg_predictions), np.sqrt(mean_squared_error(self.y_test, self.logreg_predictions))]
295
296 Errors(self.window, temp, 'Logistic Regression')
297
298 def pred_dtree(self):
299 self.dtree_model = DecisionTreeClassifier()
300 self.dtree_model.fit(self.X_train, self.y_train)
301 self.dtree_predictions = self.dtree_model.predict(self.X_test)

302
303 self.dtree_cr['state'] = NORMAL
304 self.dtree_cm['state'] = NORMAL
305 self.dtree_error['state'] = NORMAL
306
307 def cm_dtree(self):
ConfusionMatrix(self.window, confusion_matrix(self.le.inverse_transform(self.y_test), self.le.
inverse_transform(self.dtree_predictions)), 'Decision Tree', self.le.classes_)
308
309
310 def cr_dtree(self):
ClassificationReport(self.window, classification_report(self.le.inverse_transform(self.y_test), self.
le.inverse_transform(self.dtree_predictions)), 'Decision Tree')
311
312
313 def errors_dtree(self):
temp = [mean_absolute_error(self.y_test, self.dtree_predictions), mean_squared_error(self.y_test
, self.dtree_predictions), np.sqrt(mean_squared_error(self.y_test, self.dtree_predictions))]
314
315 Errors(self.window, temp, 'Decision Tree')
316
317 def pred_rforest(self):
318 self.rforest_model = RandomForestClassifier(n_estimators=100)
319 self.rforest_model.fit(self.X_train, self.y_train)
320 self.rforest_predictions = self.rforest_model.predict(self.X_test)
321
322 self.rforest_cr['state'] = NORMAL
323 self.rforest_cm['state'] = NORMAL
324 self.rforest_error['state'] = NORMAL
325
326 def cm_rforest(self):
ConfusionMatrix(self.window, confusion_matrix(self.le.inverse_transform(self.y_test), self.le.
inverse_transform(self.rforest_predictions)), 'Random Forest', self.le.classes_)
327
328
329 def cr_rforest(self):
ClassificationReport(self.window, classification_report(self.le.inverse_transform(self.y_test), self.
le.inverse_transform(self.rforest_predictions)), 'Random Forest')
330
331
332 def errors_rforest(self):
temp = [mean_absolute_error(self.y_test, self.rforest_predictions), mean_squared_error(self.
y_test, self.rforest_predictions), np.sqrt(mean_squared_error(self.y_test, self.rforest_predictions))]
333
334 Errors(self.window, temp, 'Random Forest')
335
336
337 class Table:
338 def __init__(self, data, master, name):
339 self.master = master
340 self.window = Toplevel(self.master)
341 self.data = data
342 self.name = name
343 self.window.title(self.name)
344 self.window.geometry('600x600')
345 self.window.minsize(250, 250)
346
347 self.frame = Frame(self.window)
348 self.frame.pack(expand=True, fill=BOTH)
349
350 self.canvas = Canvas(self.frame, background='white')

351
352 self.h_scroll = Scrollbar(self.frame, orient=HORIZONTAL, command=self.canvas.xview)
353 self.h_scroll.pack(side=BOTTOM, fill=X)
354 self.v_scroll = Scrollbar(self.frame, orient=VERTICAL, command=self.canvas.yview)
355 self.v_scroll.pack(side=RIGHT, fill=Y)
356
357 self.canvas['xscrollcommand'] = self.h_scroll.set
358 self.canvas['yscrollcommand'] = self.v_scroll.set
359 self.canvas.pack(expand=True, fill=BOTH)
360
361 self.label_frame = LabelFrame(self.canvas)
362 self.canvas.create_window((0, 0), window=self.label_frame, anchor=N + W)
363
364 self.shape = (data.shape[0], data.shape[1])
365
366 Table.add_label(self, 0, 0, '#', font=('Helvetica', 15, 'bold'))
367 for j in range(self.shape[1]):
368 Table.add_label(self, 0, j + 1, self.data.columns[j], font=('Helvetica', 12, 'bold'))
369 self.height = 20
370 for i in range(self.shape[0]):
371 Table.add_label(self, i + 1, 0, str(i + 1))
372 ar = data.iloc[i].values
373 for j in range(len(ar)):
374 Table.add_label(self, i + 1, j + 1, ar[j])
375 self.window.update()
376 self.canvas.configure(scrollregion=self.label_frame.bbox(ALL))
377
378 def add_label(self, i, j, text, font=('Helvetica', 10)):
379 if j % 2 == 0:
380 color = 'white'
381 else:
382 color = 'antique white'
383 label = Label(self.label_frame, text=text, font=font, bg=color)
384 label.grid(row=i, column=j, sticky=E+N+W+S)
385
386
387 class SelectionX:
388 def __init__(self, master, data):
389 self.master = master
390 self.data = data
391 self.columns = self.data.columns
392 self.variables = [IntVar() for _ in range(len(self.columns))]
393
394 self.window = Toplevel(self.master)
395 self.window.grab_set()
396 self.window.title('Independent Variables')
397 self.window.geometry('400x400')
398 self.window.minsize(250, 250)
399
400 self.frame = Frame(self.window)
401 self.frame.pack(expand=True, fill=BOTH)
402
403 self.canvas = Canvas(self.frame, background='antique white')
404
405 self.v_scroll = Scrollbar(self.frame, orient=VERTICAL, command=self.canvas.yview)

406 self.v_scroll.pack(side=RIGHT, fill=Y)
407
408 self.canvas['yscrollcommand'] = self.v_scroll.set
409 self.canvas.pack(expand=True, fill=BOTH)
410
411 self.frame2 = Frame(self.canvas, bg='antique white')
412 self.canvas.create_window((0, 0), window=self.frame2, anchor=N + W)
413
414 for i in range(len(self.columns)):
Checkbutton(self.frame2, variable=self.variables[i], text=self.columns[i], bg='antique white').
pack(anchor=N+W)
415
416
self.all = Button(self.canvas, text='Select All', height=2, width=10, command=lambda: self.select_all
())
417
418 self.all.pack(anchor=E, padx=20, pady=20)
419
self.none = Button(self.canvas, text='Select None', height=2, width=10, command=lambda: self.
select_none())
420
421 self.none.pack(anchor=E, padx=20, pady=0)
422
self.none = Button(self.canvas, text='Confirm', height=2, width=10, command=lambda: self.
confirm())
423
424 self.none.pack(anchor=E, padx=20, pady=20)
425
426 self.window.update()
427
428 self.canvas.configure(scrollregion=self.canvas.bbox(ALL))
429
430 self.window.mainloop()
431
432 def select_all(self):
433 for i in self.variables:
434 i.set(1)
435
436 def select_none(self):
437 for i in self.variables:
438 i.set(0)
439
440 def confirm(self):
441 self.window.grab_release()
442 self.window.quit()
443 self.window.destroy()
444
445
446 class SelectionY:
447 def __init__(self, master, data):
448 self.master = master
449 self.data = data
450 self.columns = self.data.columns
451 self.variable = IntVar()
452
453 self.window = Toplevel(self.master)
454 self.window.grab_set()
455 self.window.title('Dependent Variables')
456 self.window.geometry('400x400')

457 self.window.minsize(250, 250)
458
459 self.frame = Frame(self.window)
460 self.frame.pack(expand=True, fill=BOTH)
461
462 self.canvas = Canvas(self.frame, background='antique white')
463
464 self.v_scroll = Scrollbar(self.frame, orient=VERTICAL, command=self.canvas.yview)
465 self.v_scroll.pack(side=RIGHT, fill=Y)
466
467 self.canvas['yscrollcommand'] = self.v_scroll.set
468 self.canvas.pack(expand=True, fill=BOTH)
469
470 self.frame2 = Frame(self.canvas, bg='antique white')
471 self.canvas.create_window((0, 0), window=self.frame2, anchor=N + W)
472
473 for i in range(len(self.columns)):
Radiobutton(self.frame2, variable=self.variable, value=i, text=self.columns[i], bg='antique white'
).pack(anchor=N+W)
474
475
self.none = Button(self.canvas, text='Confirm', height=2, width=10, command=lambda: self.
confirm())
476
477 self.none.pack(anchor=E, padx=20, pady=20)
478
479 self.canvas.configure(scrollregion=self.canvas.bbox(ALL))
480
481 self.window.mainloop()
482
483 def confirm(self):
484 self.window.grab_release()
485 self.window.quit()
486 self.window.destroy()
487
488
489 class ConfusionMatrix:
490 def __init__(self, master, data, name, labels):
491 self.data = data
492 self.master = master
493 self.name = name
494 self.labels = sorted(labels)
495
496 self.total = np.sum(self.data)
497
498 self.window = Toplevel(self.master)
499 self.window.title(self.name + ' Confusion Matrix')
500 self.window.resizable(False, False)
501
self.total_label = Label(self.window, text=f'Total = {self.total}', font=('Helvetica', 15, 'bold'), bg='
antique white')
502
503 self.total_label.grid(row=0, column=0, sticky=(N, S, E, W))
504
505 for i in range(len(self.labels)):
506 if i % 2 == 0:
507 color = 'white'
508 else:

509 color = 'antique white'
Label(self.window, text=f'Predicted\n{self.labels[i]}', font=('Helvetica', 15, 'bold'), bg=color).grid
(row=0, column=i+1, sticky=(N, S, E, W))
510
511
512 for i in range(len(self.labels)):
513 if i % 2 == 0:
514 color = 'white'
515 else:
516 color = 'antique white'
Label(self.window, text=f'Actual\n{self.labels[i]}', font=('Helvetica', 15, 'bold'), bg=color).grid(
row=i+1, column=0, sticky=(N, S, E, W))
517
518 for j in range(len(self.labels)):
519 color = ['grey90', 'grey80', 'grey70']
Label(self.window, text=str(self.data[i][j]), font=('Helvetica', 15, 'bold'), bg=color[(i + j) % 3]).
grid(row=i+1, column=j+1, sticky=(N, S, E, W))
520
521
522
523 class Errors:
524 def __init__(self, master, data, name):
525 self.master = master
526 self.data = data
527 self.name = name
528
529 self.window = Toplevel(self.master)
530 self.window.title(self.name + ' Errors')
531 self.window.geometry('500x180')
532 self.window.resizable(False, False)
533
534 self.frame = Frame(self.window)
535 self.frame.place(width=504, height=184, bordermode=OUTSIDE, x=0, y=0)
536
self.text1 = Label(self.frame, text='Mean Absolute Error :', font=('Helvetica', 15, 'bold'), bg='
antique white')
537
538 self.text1.place(width=260, height=60, bordermode=INSIDE, x=0, y=0)
539 self.text2 = Label(self.frame, text='Mean Squared Error :', font=('Helvetica', 15, 'bold'), bg='white')
540 self.text2.place(width=260, height=60, bordermode=INSIDE, x=0, y=60)
self.text3 = Label(self.frame, text='Root Mean Squared Error: ', font=('Helvetica', 15, 'bold'), bg='
antique white')
541
542 self.text3.place(width=260, height=60, bordermode=INSIDE, x=0, y=120)
543
544 self.value1 = Label(self.frame, text=str(data[0]), font=('Helvetica', 15, 'bold'), bg='antique white')
545 self.value1.place(width=240, height=60, bordermode=INSIDE, x=260, y=0)
546 self.value2 = Label(self.frame, text=str(data[1]), font=('Helvetica', 15, 'bold'), bg='white')
547 self.value2.place(width=240, height=60, bordermode=INSIDE, x=260, y=60)
548 self.value3 = Label(self.frame, text=str(data[2]), font=('Helvetica', 15, 'bold'), bg='antique white')
549 self.value3.place(width=240, height=60, bordermode=INSIDE, x=260, y=120)
550
551
552 class ClassificationReport:
553 def __init__(self, master, data, name):
554 self.master = master
555 self.data = data
556 self.name = name
557
558 self.window = Toplevel(self.master)

559 self.window.title(self.name + ' Classification Report')
560 self.window.configure(background='white')
561 self.window.resizable(False, False)
562 y = 0
563
Label(self.window, text='precision', font=('Helvetica', 15, 'bold'), anchor=E, bg='antique white').
place(width=100, height=50, bordermode=INSIDE, x=150, y=y)
564
Label(self.window, text='recall', font=('Helvetica', 15, 'bold'), anchor=E, bg='white').place(width=
100, height=50, bordermode=INSIDE, x=250, y=0)
565
Label(self.window, text='f1‐score', font=('Helvetica', 15, 'bold'), anchor=E, bg='antique white').
place(width=100, height=50, bordermode=INSIDE, x=350, y=y)
566
Label(self.window, text='support', font=('Helvetica', 15, 'bold'), anchor=E, bg='white').place(width
=100, height=50, bordermode=INSIDE, x=450, y=y)
567
568 y = y + 50
569
Label(self.window, bg='antique white').place(width=100, height=10, bordermode=INSIDE, x=150, y
=y)
570
Label(self.window, bg='antique white').place(width=100, height=10, bordermode=INSIDE, x=350, y
=y)
571
572 y = y + 10
573
574 self.ar = self.data.split('\n\n')[1:]
575 self.part1 = self.ar[0].split('\n')
576
577 for i in self.part1:
578 temp = i.split()
Label(self.window, text=temp[0], font=('Helvetica', 12, 'bold'), anchor=E, bg='white').place(width
=150, height=30, bordermode=INSIDE, x=0, y=y)
579
Label(self.window, text=temp[1], font=('Helvetica', 12), anchor=E, bg='antique white').place(
width=100, height=30, bordermode=INSIDE, x=150, y=y)
580
Label(self.window, text=temp[2], font=('Helvetica', 12), anchor=E, bg='white').place(width=100,
height=30, bordermode=INSIDE, x=250, y=y)
581
Label(self.window, text=temp[3], font=('Helvetica', 12), anchor=E, bg='antique white').place(
width=100, height=30, bordermode=INSIDE, x=350, y=y)
582
Label(self.window, text=temp[4], font=('Helvetica', 12), anchor=E, bg='white').place(width=100,
height=30, bordermode=INSIDE, x=450, y=y)
583
584 y = y + 30
585
Label(self.window, bg='antique white').place(width=100, height=20, bordermode=INSIDE, x=150, y
=y)
586
Label(self.window, bg='antique white').place(width=100, height=20, bordermode=INSIDE, x=350, y
=y)
587
588 y = y + 20
589
590 self.part2 = self.ar[1].split('\n')
591
592 for i in self.part2:
593 if i == '':
594 continue
595 temp = i.split()
Label(self.window, text=temp.pop(), font=('Helvetica', 12), anchor=E, bg='white').place(width=
100, height=30, bordermode=INSIDE, x=450, y=y)
596
Label(self.window, text=temp.pop(), font=('Helvetica', 12), anchor=E, bg='antique white').place(
width=100, height=30, bordermode=INSIDE, x=350, y=y)
597
598 if len(temp) != 1:

Label(self.window, text=temp.pop(), font=('Helvetica', 12), anchor=E, bg='white').place(width=
100, height=30, bordermode=INSIDE, x=250, y=y)
599
600 if len(temp) != 1:
Label(self.window, text=temp.pop(), font=('Helvetica', 12), anchor=E, bg='antique white').place
(width=100, height=30, bordermode=INSIDE, x=150, y=y)
601
602 else:
Label(self.window, bg='antique white').place(width=100, height=30, bordermode=INSIDE, x=
150, y=y)
603
Label(self.window, text=' '.join(temp), font=('Helvetica', 12, 'bold'), anchor=E, bg='white').place(
width=150, height=30, bordermode=INSIDE, x=0, y=y)
604
605 y = y + 30
606
607 self.window.geometry('550x'+str(y))
608
609
610 class Scatter:
611 def __init__(self, master, y_test, pred):
612 self.master = master
613 self.y_test = y_test
614 self.pred = pred
615
616 self.window = Toplevel(self.master)
617 self.window.title('Scatter Plot (y_test vs predictions)')
618 self.window.configure(background='white')
619 self.window.resizable(False, False)
620
621 self.figure = Figure(figsize=(5, 5), dpi=100)
622 self.sub = self.figure.add_subplot(111)
623 self.sub.scatter(self.y_test, self.pred, edgecolor='black')
624 self.sub.plot()
625
626 self.canvas = FigureCanvasTkAgg(self.figure, master=self.window)
627 self.canvas.get_tk_widget().pack()
628 self.canvas.draw()
629
630
631 class Coefficients:
632 def __init__(self, master, intercept, coef, columns):
633 self.master = master
634 self.intercept = intercept
635 self.coef = coef
636 self.columns = columns
637
638 self.window = Toplevel(self.master)
639 self.window.title('Intercept and Coefficients')
640 self.window.configure(background='white')
641 self.window.resizable(False, False)
642
self.intercept_label = Label(self.window, text='Intercept :', font=('Helvetica', 15, 'bold'), bg='
antique white')
643
644 self.intercept_label.grid(row=0, column=0, sticky=(N, S, E, W))
645 self.intercept_value = Label(self.window, text=str(self.intercept), font=('Helvetica', 15), bg='white')
646 self.intercept_value.grid(row=0, column=1, sticky=(N, S, E, W))
647
648 self.coefs = Label(self.window, text='Coefficients', font=('Helvetica', 15, 'bold'), bg='white')

649 self.coefs.grid(row=1, column=0, columnspan=2, sticky=(N, S, E, W))
650
651 for i in range(len(self.coef)):
Label(self.window, text=self.columns[i], font=('Helvetica', 12), bg='antique white').grid(row=i+2,
column=0, sticky=(N, S, E, W))
652
Label(self.window, text=str(self.coef[i]), font=('Helvetica', 12), bg='white').grid(row=i+2, column=
1, sticky=(N, S, E, W))
653
654
655
656 if __name__ == '__main__':
657 MachineLearning()