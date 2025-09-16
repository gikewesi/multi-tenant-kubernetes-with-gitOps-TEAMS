variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "project_name" {
  type = string
  default = "vero-teams"
}

variable "vpc_cidr" {
  type    = string
  default = "10.0.0.0/16"
}

variable "public_subnets" {
  type    = list(string)
  default = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "private_subnets" {
  type    = list(string)
  default = ["10.0.101.0/24", "10.0.102.0/24"]
}

variable "azs" {
  type    = list(string)
  default = ["us-east-1a", "us-east-1b"]
}

variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
  default    = "vero-teams"
}
variable "alb_chart_version" {
  type    = string
  default = "1.10.0"
}
variable "alb_role_arn" {
  description = "IAM role ARN for the AWS Load Balancer Controller service account"
  type        = string
}