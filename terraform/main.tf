terraform {
  required_providers {
    alicloud = {
      source = "aliyun/alicloud"
      version = "1.115.1"
    }
  }
}

provider "alicloud" {
      profile = "terraform"
      region = "cn-hangzhou"
}

resource "alicloud_vpc" "vpc" {
    name = "tcloud-resouce"
    cidr_block = "172.26.0.0/16"
}

resource "alicloud_vswitch" "wiredcraft_subnet" {
  name = "subnet-tcloud"
  vpc_id = alicloud_vpc.vpc.id
  cidr_block = "172.26.1.0/24"
  availability_zone = "cn-hangzhou-h"
}

resource "alicloud_security_group" "wiredcraft_sg" {
  name        = "wiredcraft-sg"
  description = "default"
  vpc_id = alicloud_vpc.vpc.id
}
