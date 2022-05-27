import pandas
filename = 'attendance.csv'
data = pandas.read_csv(filename, header=0) 
myData = data.values 
print(len(myData)) 
print(myData)



# @app.route('/to_do',methods=['GET','POST'])
# def to_do():
#     if request.method == 'POST':
#         task_content = request.form['content']
#         new_task = Todo(content=task_content)

#         try:
#             db.session.add(new_task)
#             db.session.commit()
#             return redirect(url_for('to_do'))
#         except:
#             return 'There was an issue adding your task'

#     else:
#         tasks = Todo.query.order_by(Todo.date_created).all()
#         return render_template('to_do.html')

# @app.route('/delete/<int:id>')
# def delete(id):
#     task_to_delete = Todo.query.get_or_404(id)

#     try:
#         db.session.delete(task_to_delete)
#         db.session.commit()
#         return redirect(url_for('to_do'))
#     except:
#         return 'There was a problem deleting that task'

# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     task = Todo.query.get_or_404(id)

#     if request.method == 'POST':
#         task.content = request.form['content']

#         try:
#             db.session.commit()
#             return redirect(url_for('to_do'))
#         except:
#             return 'There was an issue updating your task'

#     else:
#         return render_template('update.html', task=task)

