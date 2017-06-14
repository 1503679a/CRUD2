from flask import Flask,jsonify
import subprocess

def get_ssl():
	ssl = subprocess.check_output(['sudo','ovs-vsctl','get-ssl'])
	return ssl
def set_ssl(key,cert,ca):
	input = subprocess.call(['sudo','ovs-vsctl','--bootstrap','set-ssl',key,cert,ca])

def del_ssl():
	delete = subprocess.check_output(['sudo','ovs-vsctl','del-ssl'])
	ssl = subprocess.check_output(['sudo','ovs-vsctl','get-ssl'])
	return ssl


def get_bridge_controller(bridge):
	get = subprocess.check_output(['sudo','ovs-vsctl','get-controller',bridge])
	return get

def set_bridge_controller(bridge,prot,ip,port):
	input = subprocess.call(['sudo','ovs-vsctl','set-controller',bridge,prot + ':' + ip + ':' + port])
	


def set_bridge_controller2(bridge,insert):
	input = subprocess.call(['sudo','ovs-vsctl','set-controller'
,bridge,insert])


def del_bridge_controller(bridge):
	delete = subprocess.call(['sudo','ovs-vsctl','del-controller',bridge])

def update_bridge_controller(bridge,insert):
	subprocess.call(['sudo','ovs-vsctl','del-controller',bridge])
	subprocess.call(['sudo','ovs-vsctl','set-controller',bridge,insert])	

def get_sflow():
	get = subprocess.check_output(['sudo','ovs-vsctl','list','sflow'])
	return get

def del_sflow(bridge):
	delete =  subprocess.call(['sudo','ovs-vsctl','--','clear','Bridge',bridge,'sflow'])

def set_sflow(agent,target,header,sampling,polling,bridge):

	subprocess.call(['sudo','ovs-vsctl','--','--id=@s','create','sFlow','agent='+agent,'target='+target,'header='+header,'sampling='+sampling,'polling='+polling,'--','set','Bridge',bridge,'sflow=@s'])

def update_sflow(agent,target,header,sampling,polling,bridge):
	subprocess.call(['sudo','ovs-vsctl','--','clear','Bridge',bridge,'sflow'])
	subprocess.call(['sudo','ovs-vsctl','--','--id=@s','create','sFlow','agent='+agent,'target='+target,'header='+header,'sampling='+sampling,'polling='+polling,'--','set','Bridge',bridge,'sflow=@s'])
