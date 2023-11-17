cd ../
unzip jsai_data.zip
mv jsai_data datasets
cp scripts/prepare_train.sh datasets/
cd datasets
mkdir train
mkdir test
cd train
mkdir images
mkdir labels
mv ../*.jpg ./images
mv ../*.txt ./labels
cd ../test
mkdir images
mkdir labels
mv ../train/images/24631-out_ori.jpg ./images
mv ../train/images/24632-out_ori.jpg ./images
mv ../train/images/24633-out_ori.jpg ./images
mv ../train/images/24634-out_ori.jpg ./images
mv ../train/images/24635-out_ori.jpg ./images
mv ../train/labels/24631-out_ori.txt ./labels
mv ../train/labels/24632-out_ori.txt ./labels
mv ../train/labels/24633-out_ori.txt ./labels
mv ../train/labels/24634-out_ori.txt ./labels
mv ../train/labels/24635-out_ori.txt ./labels
cd ../
python3 prepare_train.py

docker run --name Chrome2 -d \
	-p 8081:8080 \
	--env 'CUSTOM_RES_W=1280' \
	--env 'CUSTOM_RES_H=768' \
	--env 'UID=99' \
	--env 'GID=100' \
	--env 'UMASK=000' \
	--env 'DATA_PERM=770' \
	--volume /opt/chrome2:/chrome \
	ich777/chrome
