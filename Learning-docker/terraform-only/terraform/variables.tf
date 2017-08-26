
variable "aws_access_key" {
  description = "AWS access key"
}

variable "aws_secret_key" {
  description = "AWS secret key"
}

variable "vpc_preconf_id" {
  description = "VPC network"
}

variable "subnet_preconf_id" {
  description = "VPC network"
}


variable "region" {
  description = "AWS Region"
  default     = "us-west-2"
}

variable "availability_zones" {
  description = "Availability Zones"
  default     = "us-west-2b"
}


variable "amis" {
  description = "Instances AMIs"
  default = {
    us-west-2      = "ami-835b4efa"
  }
}

variable "instance_type" {
  description = "EC2 instance type"
  default = "t2.micro"
}


variable "key_name" {
  description = "SSH key name to access the EC2 instances"
}
