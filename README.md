## Example ansible plugin to retrieve EC2 metadata (IPs, i-$instance_id demoed)

A lot of folks in IRC (including myself) have had trouble getting the ec2.py plugin to play nice with tag names, so this is a mostly functioning demo of an alternative pattern of use, and the general model is meant to be pretty easily extended.

You will need to be authenticated against Amazon for this to work. (duh)

Change {{ your_key }} to your AWS key. Everything else ought to actually work.


1. ansible-playbook -vvv ec2-instances.yml -i /etc/ansible/local --tags infra

This starts up 2 EC2 instances and an ELB. Don't forget to tear them down. :)

2. ansible-playbook -vvv ec2-instances.yml -i /etc/ansible/local --tags output_ips

This will show you how stdout looks, and you can then run other tasks with these as items.

3. ansible-playbook -vvv ec2-instances.yml -i /etc/ansible/local --tags instance_to_elbs


You will see something like this:

msg: The instance i-c0f8fbef could not be put in service on LoadBalancer:SampleApp. Reason: Instance has not passed the configured HealthyThreshold number of health checks consecutively.


BUT, that's better than not being able to join instances by tag name at all. :)

