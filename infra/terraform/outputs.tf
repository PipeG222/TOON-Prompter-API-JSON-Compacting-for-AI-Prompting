// infra/terraform/outputs.tf
output "alb_dns_name" {
  description = "Public DNS of the Application Load Balancer"
  value       = aws_lb.alb.dns_name
}

output "ecs_cluster_name" {
  description = "ECS Cluster name"
  value       = aws_ecs_cluster.cluster.name
}

output "ecs_service_name" {
  description = "ECS Service name"
  value       = aws_ecs_service.service.name
}

output "ecr_repository_url" {
  description = "ECR repo URL to push your Docker image"
  value       = aws_ecr_repository.repo.repository_url
}
