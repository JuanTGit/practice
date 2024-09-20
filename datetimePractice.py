from datetime import datetime, timedelta


file =  ["FILE_UPLOAD_AT", "2021-07-01T12:00:00", "CodeSignal.txt", "150kb", 3600]
server = {}


timestamp = file[1]
fileName = file[2]
fileSize = file[3]
ttl = file[4]

upload_time = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")

expiration = upload_time + timedelta(seconds=ttl)

server[fileName] = {'size': fileSize, 'uploadTime': upload_time, 'expiration': expiration}


print(server)