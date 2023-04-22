# Define the AWS provider
provider "aws" {
  region = "us-east-1"
}

# Define the ECS task definition
resource "aws_ecs_task_definition" "app_task" {
  family                   = "my-app"
  container_definitions    = jsonencode([{
    name                    = "my-app"
    image                   = "my-app-image:latest"
    portMappings            = [{
      containerPort         = 8000
      protocol              = "tcp"
    }]
  }])
}

# Define the ECS service
resource "aws_ecs_service" "app_service" {
  name        = "my-app-service"
  cluster     = "default"
  task_definition = aws_ecs_task_definition.app_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    security_groups = ["sg-12345678"]
    subnets         = ["subnet-12345678", "subnet-23456789"]
  }
}
