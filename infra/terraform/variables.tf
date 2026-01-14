// infra/terraform/variables.tf
variable "aws_region" {
  description = "AWS region to deploy the ECS service"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Name prefix for ECS/ECR resources"
  type        = string
  default     = "toon-prompter-api"
}

variable "container_port" {
  description = "Port where the container listens"
  type        = number
  default     = 8000
}

variable "desired_count" {
  description = "Number of ECS tasks to run"
  type        = number
  default     = 1
}

variable "cpu" {
  description = "Fargate CPU units"
  type        = string
  default     = "256"
}

variable "memory" {
  description = "Fargate memory (MiB)"
  type        = string
  default     = "512"
}
