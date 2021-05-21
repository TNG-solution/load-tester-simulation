sudo docker run \
  -it \
  --name loads --rm \
  -p 5000:5000 \
  -v /home/djcharles26/Documents/TNG/load-tester-simulation/pycerver-server:/home/py \
  -e RUNTIME=development \
  -e PORT=5000 \
  -e MONGO_URI=mongodb+srv://backdoor:DbVzutpNdcT1t00B@cluster0.boyri.mongodb.net/test \
  -e CERVER_RECEIVE_BUFFER_SIZE=4096 -e CERVER_TH_THREADS=4 \
  -e CERVER_CONNECTION_QUEUE=4 \
  tngsolution/load-test-py:development /bin/bash