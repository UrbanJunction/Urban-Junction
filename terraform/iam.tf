#define 511ny secret
resource "aws_secretsmanager_secret" "api_key_511ny" {
    name = var.ny511_secret_name
    recovery_window_in_days = var.secrets_manager_recovery_in_days
}

#define api key with associated secret value 
resource "aws_secretsmanager_secret_version" "api_key_version_511ny" {
  secret_id     = aws_secretsmanager_secret.api_key_511ny.id
  secret_string = var.ny511_key
}