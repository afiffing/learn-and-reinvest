
output "terraform-01" {
    value = "${aws_instance.terraform-01.public_ip}"
}
