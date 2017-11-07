# AWS_Tutorials
## Tutorial to install R Server and Shiny Server on AWS

[Inspired from this great article  great article](https://aws.amazon.com/blogs/big-data/running-r-on-aws/)


The file *Script_User_Data.txt* contains the script needed to install at launch the following
* R
* RServer
* Shiny
* Shiny Server



Once the Server Shiny is set up, a little configuration is needed.
Connect to the instance and launch the following command lines

``
mkdir ~/ShinyApps
sudo /opt/shiny-server/bin/deploy-example user-dirs
cp -R /opt/shiny-server/samples/sample-apps/hello ~/ShinyApps/
``


You can check the output of the user data on the file **/var/log/cloud-init-output.log**