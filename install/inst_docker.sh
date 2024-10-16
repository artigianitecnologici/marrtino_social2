echo "install DOcker"
sudo apt install docker-io docker-compose
sudo systemctl status docker

echo "--------"
echo "sudo usermod -aG docker ${USER}"
echo "su - ${USER}"
echo "sudo usermod -aG docker marrtino"
