echo "https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04"
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
apt-cache policy docker-ce
sudo apt install docker-ce
sudo systemctl status docker

echo "--------"
echo "sudo usermod -aG docker ${USER}"
echo "su - ${USER}"
echo "sudo usermod -aG docker marrtino"
