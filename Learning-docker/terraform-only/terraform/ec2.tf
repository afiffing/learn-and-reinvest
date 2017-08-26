
# ECS Container Instances

resource "aws_instance" "terraform-01" {
    ami                         = "${lookup(var.amis, var.region)}"
    instance_type               = "${var.instance_type}"
    availability_zone           = "${var.availability_zones}"
    subnet_id                   = "${var.subnet_preconf_id}"
    key_name                    = "${var.key_name}"
    associate_public_ip_address = true
    security_groups             = ["${aws_security_group.tf-sg.id}"]
    tags {
      Name = "terraform-01"
    }
}
