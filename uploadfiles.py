import dropbox
import os
class TransferData():
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from)
        f=open(file_from,"rb")
        dbx.file_upload(f.read(),file_to)
        relative_path=os.path.relpath(local_path, file_from)
        dropbox_path=os.path.join(file_to, relative_path)
        with open(local_path, "rb") as f:
            dbx.files_upload(f.read(), dropbox_path. mode=WriteMode("overwrite"))
    def main():
        access_token='sl.BxtpYxAk4JPmmAjwx8ushm4_qRe98wo70flAm-saXrAQ0xRDqhj78VWyKok742mpaeiaMOyZwFTHUrtKrjDjd0jp_xvBckfnbvFaIPR8nz3RGVpqoL01zI1MRTGxq3g3sk12is1hGwHK'
        file_from=input("enter file path")
        file_to=input("enter full path and new file name")
        transferData=TransferData(access_token)
        transferData.upload_file(file_from,file_to)
transferData.main()