#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

net = Mininet()

##########################################
############        HOSTS      ###########
##########################################

#Sala de Desenvolvimentoa
host_dev_1 = net.addHost( 'host_dev_1' )
host_dev_2 = net.addHost( 'host_dev_2' )
host_dev_3 = net.addHost( 'host_dev_3' )
host_dev_4 = net.addHost( 'host_dev_4' )
host_dev_5 = net.addHost( 'host_dev_5' )
host_dev_6 = net.addHost( 'host_dev_6' )
host_dev_7 = net.addHost( 'host_dev_7' )
host_dev_8 = net.addHost( 'host_dev_8' )
host_dev_9 = net.addHost( 'host_dev_9' )
host_dev10 = net.addHost( 'host_dev10' )

#Sala de Testes
host_teste_1 = net.addHost( 'host_dev_1' )
host_teste_2 = net.addHost( 'host_dev_2' )
host_teste_3 = net.addHost( 'host_dev_3' )
host_teste_4 = net.addHost( 'host_dev_4' )
host_teste_5 = net.addHost( 'host_dev_5' )

#Sala de Reuniao
host_reuniao_1 = net.addHost( 'host_dev_1' ) 
host_reuniao_1 = net.addHost( 'host_dev_2' )

#Sala de TI
serv_dns = net.addHost( 'serv_dns' ) 
serv_arq = net.addHost( 'serv_arq' )
serv_web1 = net.addHost( 'serv_web1' )
serv_web2 = net.addHost( 'serv_web2' )

##########################################
############      SWITCH       ###########
##########################################

#Adiciona os Links (SW) Sala Desenvolvimento
s1= net.addSwitch( 's1' )

net.addLink( host_dev_1, s1 )                                                                                                                         
net.addLink( host_dev_2, s1 )      
net.addLink( host_dev_3, s1 )  
net.addLink( host_dev_4, s1 )                                                                                                                         
net.addLink( host_dev_5, s1 )      
net.addLink( host_dev_6, s1 )  
net.addLink( host_dev_7, s1 )                                                                                                                         
net.addLink( host_dev_8, s1 )      
net.addLink( host_dev_9, s1 )
net.addLink( host_dev10, s1 )
    

#Adiciona os Links (SW) Sala Testes
s2 = net.addSwitch( 's2' )

net.addLink( host_teste_1, s2 )                                                                                                                                  
net.addLink( host_teste_2, s2 )      
net.addLink( host_teste_3, s2 )  
net.addLink( host_teste_4, s2 )                                                                                                                         
net.addLink( host_teste_5, s2 )    

#Adiciona os Links (SW) Sala Reuniao
s3 = net.addSwitch( 's3' )

net.addLink( host_reuniao_1, s3 )                                                                                                                                   
net.addLink( host_reuniao_1, s3 )

#Adiciona os Links (SW) Sala TI
s4 = net.addSwitch( 's4' )

net.addLink( serv_dns, s4 )                                                                                                                                   
net.addLink( serv_arq, s4 )  
net.addLink( serv_web1, s4 )                                                                                                                                   
net.addLink( serv_web2, s4 )                                                                                                                                   

##########################################
############      ROTEADOR     ###########
##########################################

router1 = net.addHost( 'router1' )
router2 = net.addHost( 'router2' )
router3 = net.addHost( 'router3' )

CLI( net )
