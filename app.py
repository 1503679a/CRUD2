#!flask/bin/python
from flask import Flask, jsonify, request
import Process
call = Flask(__name__)



@call.route('/todo-apin/getssl',methods=['GET'])

def get_ssl():
	return Process.get_ssl()
@call.route('/todo-apin/setssl',methods=['POST'])
def set_ssl():
	key = request.json['key']
	cert = request.json['cert']
	ca = request.json['ca']
	Process.set_ssl(key,cert,ca)
	return jsonify({'Private key' : key,
			'Certificate' : cert,
			'Certificate Authority' : ca
						}), 201

@call.route('/todo-apin/delssl',methods=['GET'])
def del_ssl():
	return Process.del_ssl()

@call.route('/todo-apin/getbridge/<string:input>',methods=['GET'])
def get_bridge_controller(input):
	config = Process.get_bridge_controller(input)
	return jsonify({'Config' : config })
@call.route('/todo-apin/setbridge',methods=['POST'])
def set_bridge_controller():
	bridge = request.json['bridge']
	prot = request.json['prot']
	ip = request.json['ip']
	port = request.json['port']
	result = Process.set_bridge_controller(bridge,prot,ip,port)
	return jsonify({'Bridge' : bridge,
			'Type' : prot,
			'IP' : ip,
			'Port' : port
					}), 201


@call.route('/todo-apin/setbridge2',methods=['POST'])
def set_bridge_controller2():

#	json_dict = request.get_json(force=True)
	bridge = request.json['bridge']
	insert = request.json['insert']

	result = Process.set_bridge_controller2(bridge,insert)
	return jsonify({'Bridge' : bridge,
                         'Insert' : insert
                                         }), 201

@call.route('/todo-apin/delbridge/<bridge>',methods=['DELETE'])
def del_bridge_controller(bridge):
	Process.del_bridge_controller(bridge)
	return jsonify({'Result': True
					}), 
@call.route('/todo-apin/updatebridge/<bridge>/<insert>',methods=['PUT'])
def update_bridge_controller(bridge,insert):
	Process.update_bridge_controller(bridge,insert)
	return jsonify({'Bridge' : bridge,
			'Config' : insert
					})

@call.route('/todo-apin/getsflow',methods=['GET'])
def get_sflow():
	return Process.get_sflow()

@call.route('/todo-apin/delsflow/<bridge>',methods=['DELETE'])
def del_sflow(bridge):
	Process.del_sflow(bridge)
	status = "sFlow table cleared"
	return jsonify({'Bridge' : bridge,
			'Status' : status
					})
@call.route('/todo-apin/setsflow/<agent>/<target>/<header>/<sampling>/<polling>/<bridge>',methods=['POST'])

def set_sflow(agent,target,header,sampling,polling,bridge):
	Process.set_sflow(agent,target,header,sampling,polling,bridge)
	status = "sFlow table created"
	return jsonify({'Agent' : agent,
			'Target' : target,
			'Header' : header,
			'Sampling' : sampling,
			'Polling' : polling,
			'Bridge' : bridge,
			'Status' : status,}),201
@call.route('/todo-apin/updatesflow/<agent>/<target>/<header>/<sampling>/<polling>/<bridge>',methods=['PUT'])


def update_sflow(agent,target,header,sampling,polling,bridge):
	Process.update_sflow(agent,target,header,sampling,polling,bridge)
	status = "sFlow table updated for bridge "+bridge
        return jsonify({'Agent' : agent,
                        'Target' : target,
                        'Header' : header,
                        'Sampling' : sampling,
                        'Polling' : polling,
                        'Bridge' : bridge,
                        'Status' : status,}),

if __name__=='__main__':
	call.run(debug=True)


