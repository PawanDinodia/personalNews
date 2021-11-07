from flask import Flask,render_template, request,send_file,make_response
import os
import queryData

app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def index():
	return render_template("index.html")

	# /catagories
@app.route('/catagories',methods=['POST'])
def catagories():
	if request.method == 'POST':
		return queryData.getCats()
	else:
		return "invalid request"

	# /getUpdates
@app.route('/getUpdate',methods=['POST'])
def getUpdate():
	if request.method == 'POST':
		return queryData.getUpdate(request.form.get('id'))
	else:
		return "invalid request"

	# /updateSets
@app.route('/starr_change',methods=['POST'])
def starrChange():
	if request.method == 'POST':
		return queryData.starrChange(request.form.get('status'),request.form.get('updateId'))
	else:
		return "invalid request"

	# /updateMark
@app.route('/updateMark',methods=['POST'])
def updateMark():
	if request.method == 'POST':
		return queryData.updateMark(request.form.get('status'),request.form.get('updateId'))
	else:
		return "invalid request"

	# /delFlag
@app.route('/delFlagOn',methods=['POST'])
def delFlagOn():
	if request.method == 'POST':
		return queryData.delFlagOn(request.form.get('updateId'))
	else:
		return "invalid request"

#serve images
@app.route('/starred_img')
def starredImg():
	filename = 'static/imgs/starredImage.png'
	return send_file(filename, mimetype='image/png')
@app.route('/unstarred_img')
def unstarredImg():
	filename = 'static/imgs/unstarredImage.png'
	return send_file(filename, mimetype='image/png')
@app.route('/del_img')
def delImg():
	filename = 'static/imgs/del.png'
	return send_file(filename, mimetype='image/png')

if __name__ == '__main__':
	app.run(debug=True)