output "secret_name_511ny" {
  value = aws_secretsmanager_secret.api_key_511ny.name
}

output "region" {
  value = var.region
}