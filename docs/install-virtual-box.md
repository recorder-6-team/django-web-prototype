# Installing VirtualBox

One option for installation of the Recorder 6 web prototype is to use VirtualBox to create a
self-contained "virtual machine" which runs the operating system and web components required for
the server setup. This keeps the software components completely separate from the rest of the
machine it is running on and also gives us the option of importing a ready-configured virtual
machine to simplify the installation process.

Install VirtualBox from https://www.virtualbox.org/wiki/Downloads using the Windows hosts link in
the VirtualBox platform packages section. When asked to configure the custom setup, click the drop
down arrow next to VirtualBox USB Support and choose the "Entire feature will be unavailable"
option. Repeat for VirtualBox Python Support as we will install our own Python later.

![VirtualBox Custom Setup installation page](screenshots/virtualbox-custom-setup.png?raw=true "VirtualBox Custom Setup")

If you get a security alert from Windows Defender, make sure you check the option to allow private
network access then click “Allow access” as below:

![VirtualBox Windows Defender alert](screenshots/virtualbox-defender-alert.png?raw=true "VirtualBox Windows Defender alert")

If you get a warning about compatibility, choose "This program installed correctly":

![VirtualBox Windows compatibility warning](screenshots/virtualbox-windows-compatibility.png?raw=true "VirtualBox Windows compatibility warning")

In order to use VirtualBox reliably, I found that I had to uninstall the built-in Windows features
for virtual machine support. To do this:

1. Press the Windows Key then type "Feature" and select "Turn Windows features on or off".
2. Uncheck Virtual Machine Platform and Windows Hypervisor Platform.
3. Click OK.
4. Restart your machine.