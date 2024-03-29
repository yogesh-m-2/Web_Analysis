#----- AWS -------

s3ls(){
aws s3 ls s3://$1
}

s3cp(){
aws s3 cp $2 s3://$1 
}

#---- Content discovery ----
thewadl(){ #this grabs endpoints from a application.wadl and puts them in yahooapi.txt
curl -s $1 | grep path | sed -n "s/.*resource path=\"\(.*\)\".*/\1/p" | tee -a ~/tools/dirsearch/db/yahooapi.txt
}

#----- recon -----
crtndstry(){
./tools/crtndstry/crtndstry $1
}

am(){ #runs amass passively and saves to json
amass enum --passive -d $1 -json $1.json
jq .name $1.json | sed "s/\"//g"| httprobe -c 60 | tee -a $1-domains.txt
}

certprobe(){ #runs httprobe on all the hosts from certspotter
curl -s https://crt.sh/\?q\=\%.$1\&output\=json | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u | httprobe | tee -a ./all.txt
}

mscan(){ #runs masscan
sudo masscan -p4443,2075,2076,6443,3868,3366,8443,8080,9443,9091,3000,8000,5900,8081,6000,10000,8181,3306,5000,4000,8888,5432,15672,9999,161,4044,7077,4040,9000,8089,443,744$
}

certspotter(){ 
curl -s https://certspotter.com/api/v0/certs\?domain\=$1 | jq '.[].dns_names[]' | sed 's/\"//g' | sed 's/\*\.//g' | sort -u | grep $1
} #h/t Michiel Prins

crtsh(){
curl -s https://crt.sh/?Identity=%.$1 | grep ">*.$1" | sed 's/<[/]*[TB][DR]>/\n/g' | grep -vE "<|^[\*]*[\.]*$1" | sort -u | awk 'NF'
}

certnmap(){
curl https://certspotter.com/api/v0/certs\?domain\=$1 | jq '.[].dns_names[]' | sed 's/\"//g' | sed 's/\*\.//g' | sort -u | grep $1  | nmap -T5 -Pn -sS -i - -$
} #h/t Jobert Abma

ipinfo(){
curl http://ipinfo.io/$1
}


#------ Tools ------
dirsearch(){ runs dirsearch and takes host and extension as arguments
python3 ~/tools/dirsearch/dirsearch.py -u $1 -e $2 -t 50 -b 
}

sqlmap(){
python ~/tools/sqlmap*/sqlmap.py -u $1 
}

ncx(){
nc -l -n -vv -p $1 -k
}

crtshdirsearch(){ #gets all domains from crtsh, runs httprobe and then dir bruteforcers
curl -s https://crt.sh/?q\=%.$1\&output\=json | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u | httprobe -c 50 | grep https | xargs -n1 -I{} python3 ~/tools/dirsearch/dirsearch.py -u {} -e $2 -t 50 -b 
}


aquatone(){
/home/kali/tools/aquatone $1 $2
}


proburp(){
sh /home/kali/Downloads/burp/suite/insuite/burp
}

jsparser(){
python3 ~tools/JSParser/handler.py
}

linkfinder(){
python3 ~/tools/LinkFinder/linkfinder.py $1 $2 $3 $4 $5 $6 $7 $8
}
syborg(){
python3 ~/tools/Syborg/syborg.py $1 $2 $3 $4 $5 $6 $7 $8
}

takeover(){
python3 ~/tools/takeover/takeover.py $1 $2 $3 $4 $5
}

hostilesubbruteforcer(){
ruby ~/tools/HostileSubBruteforcer/sub_brute.rb $1 $2 $3
}

gitgraber(){
python3 ~/tools/gitGraber/gitGraber.py $1 $2 $3 $4 $5 $6 $7 $8
}
vhd(){
ruby ~/tools/virtual-host-discovery/scan.rb $1 $2 $3
}
nuclei(){
~/go/bin/nuclei $1 $2 $3
}
paramspider(){
python3 ~/tools/ParamSpider/paramspider.py $1 $2 $3 $4 $5 $6 $7 $8 $9
}

subzy(){
~/go/bin/subzy $1 $2 $3 $4 $5
}

chronos(){
~/go/bin/chronos $1 $2 $3 $4 $5
}

meg(){
~/go/bin/meg $1 $2 $3 $4 $5
}

trufflehog(){
~/go/bin/trufflehog $1 $2 $3 $4 $5
}

waybackurls(){
~/go/bin/waybackurls $1 $2 $3 $4 $5
}
google(){
python3 ~/tools/google.py $1 $2 $3 $4 $5 $6
}
see-surf(){
python3 ~/tools/See-SURF/see-surf.py $1 $2 $3 $4 $5 $6
}
byp4xx(){
python3 ~/tools/byp4xx/byp4xx.py $1 $2 $3 $4 $5 $6
}
fff(){
~/go/bin/fff $1 $2 $3 $4 $5
}
gf(){
~/go/bin/gf $1 $2 $3 $4 $5
}
oralyzer(){
python3 ~/tools/Oralyzer/oralyzer.py $1 $2 $3 $4 $5
}
export PATH=$PATH:/go/bin
