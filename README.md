Hit the player by : https://united-secretly-mongoose.ngrok-free.app/

Reference :
https://www.jenkins.io/doc/book/installing/kubernetes/#create-a-deployment
https://sweetcode.io/how-to-deploy-an-application-to-kubernetes-cluster-using-jenkins-ci-cd-pipeline/


Kubernetes installation : 
##vim /etc/netplan/00-installer-config.yaml
cat /etc/netplan/00-installer-config.yaml > Server_files/00-installer-config.yaml
##ip a
##apt install icmp-tools
##apt-get install traceroute
##apt install iputils-ping
##netplan try
##swapoff -a
##free -m
##cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
cat /etc/modules-load.d/k8s.conf > Server_files/k8s.conf
##sudo modprobe overlay
##sudo modprobe br_netfilter
##cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
cat /etc/sysctl.d/k8s.conf >> Server_files/k8s.conf
##net.bridge.bridge-nf-call-iptables  = 1
##net.bridge.bridge-nf-call-ip6tables = 1
##net.ipv4.ip_forward                 = 1
##EOF
##sudo sysctl --system
##sudo apt-get install -y apt-transport-https ca-certificates curl
##apt-get update
##sudo mkdir /etc/apt/keyrings
##ls /etc/apt/keyrings
##curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-archive-keyring.gpg
##echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
##apt-get update
##sudo apt install -y kubelet=1.26.5-00 kubeadm=1.26.5-00 kubectl=1.26.5-00
##apt install docker.io
##mkdir /etc/containerd
##sh -c "containerd config default > /etc/containerd/config.toml"
##sudo sed -i 's/ SystemdCgroup = false/ SystemdCgroup = true/' /etc/containerd/config.toml
##vim /etc/containerd/config.toml
cat /etc/containerd/config.toml config.toml
##systemctl restart containerd.service
##systemctl restart kubelet.service
##systemctl enable kubelet.service
##kubeadm config images pull
##kubeadm init --pod-network-cidr=10.10.0.0/16
##mkdir -p $HOME/.kube
##sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
cat $HOME/.kube/config > admin.conf
##sudo chown $(id -u):$(id -g) $HOME/.kube/config
##kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/tigera-operator.yaml
##curl https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/custom-resources.yaml -O
##sed -i 's/cidr: 192\.168\.0\.0\/16/cidr: 10.10.0.0\/16/g' custom-resources.yaml
##cat custom-resources.yaml
##kubectl create -f custom-resources.yaml
##kubectl get nodes
##ls -lrth
##apt install python3-venv
##python3 -m venv EGIN_VENV
##source EGIN_VENV/bin/activate
##scp 192.168.1.24:/tmp/id* /tmp/
##scp omsadmin@192.168.1.24:/tmp/id* /tmp/
##cp /tmp/id_ed25519* .ssh/
##vim Dockerfile
cat ~/Dockerfile > Dockerfile
##python --version
##vim Dockerfile
##ls
##git clone git@github.com:kannarajesh/EGIN_MUSIC.git
##pip install -r requirements.txt
##python manage.py runserver 0.0.0.0:8000
##ls -lrth
##cd EGIN_MUSIC/
##vim Dockerfile
##docker build -t python-django-app .
##docker run -it -p 8000:8000 python-django-app
##docker build -t python-django-app .
##docker run -it -p 8000:8000 python-django-app
##docker ps -a
##docker run -it -p 8000:8000 egin_music
##vim eginmusic-deployment.yaml
cat ~/eginmusic-deployment.yaml > eginmusic-deployment.yaml
##docker images get
##docker images
##vim eginmusic-deployment.yaml
##kubectl apply -f eginmusic-deployment.yaml
##kubectl get deploy
##kubectl get deploy eginmusic
##kubectl describe deplo
##kubectl get deploy eginmusic
##kubectl get pod
##kubectl get deploy
##docker images
##docker login
##docker images
##docker tag python-django-app:latest kannarajesh064/eginmusic:tagname
##docker push kannarajesh064/eginmusic:tagname
##vim eginmusic-deployment.yaml
##kubectl apply -f  eginmusic-deployment.yaml
##kubectl get deploy django-app
##kubectl get deploy eginmusic
##kubectl delete deployment --all
##kubectl get pod
cat ~/django-svc.yaml > django-svc.yaml
##vim django-svc.yaml
##kubectl apply -f django-svc.yaml
##kubectl get svc django
##telnet localhost 31785
##curl localhost:31785
##curl localhost:8000
##kubectl get svc django


Jenkins installation:


#sudo wget -O /usr/share/keyrings/jenkins-keyring.asc   https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key

#echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]   https://pkg.jenkins.io/debian-stable binary/ | sudo tee   /etc/apt/sources.list.d/jenkins.list > /dev/null

#sudo apt-get update

#sudo apt update
#sudo apt install fontconfig openjdk-17-jre
#sudo apt-get install jenkins
#sudo systemctl restart jenkins
#systemctl status jenkins



#docker run -it -e NGROK_AUTHTOKEN=XXXXXXXXXXXXXXXXXXXXXX ngrok/ngrok tunnel --label edge=edghts_ http://localhost:80
