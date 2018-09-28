#!/usr/bin/python
import urllib, sys, time, os, urllib2

os.system('clear')
class warna :
	HIJAU = '\033[92m'
	HT = '\033[32m'
	KUNING = '\033[33m'
	MERAH = '\033[31m'
	TUTUP = '\033[00m'
	
hanyaJudul = """
+===========================================+
|          [ DIRECTORY-BUSTER ]             |
|             [ BRUTEFORCE ]                |
|    AUTHOR  : SECURITY007                  |
|    VERSION : 2.3                          |
|    RELEASE : 13/02/2018                   |
+===========================================+"""
print warna.KUNING+hanyaJudul+warna.TUTUP
print ""
site = raw_input("Host [http://site.com] >>> ")
daftar = "list.txt"
url = site
list = daftar
try:
	buka = open(list,"rb")
	c = buka.readlines()
	p = len(c)
except:
	print warna.MERAH+"[-]List tidak ketemu/directory salah"+warna.TUTUP
	sys.exit()
print "="*60
print "Scanning...",site
print "Proses scanning tergantung pada koneksi internet anda"
print "Total ada",p,"directory pada wordlist"
print "="*60
for file in range(p):
	b = c[file]
	req = urllib.urlopen(url+"/"+b)	
	if (req.code == 200):
		print warna.HIJAU+"/{} Status Code : 200 ok".format(b)+warna.TUTUP
	elif (req.code == 403):
		print warna.HT+"/{} Status Code : 403 forbidden".format(b)+warna.TUTUP
	elif (req.code == 301):
		print warna.KUNING+"/{} Status Code : 301 Moved Permanently".format(b)+warna.TUTUP
	elif (req.code == 302):
		print warna.KUNING+"/{} Status Code : 302 Moved Temporarily".format(b)+warna.TUTUP
	else:
	  print "/{} Status Code : 404 not found".format(b)