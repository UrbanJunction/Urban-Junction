variable "ny511_key" {
    description = "dev key for NY511"
    type = string
}

variable "region" {
    description = "aws service region"
    type = string 
    default = "us-east-2"
}

variable "ny511_secret_name" {
    description = "name for NY511 API key secret"
    type = string
    default = "ny511-api-secret"
}

variable "secrets_manager_recovery_in_days" {
  type        = number
  default     = 0
  description = "Deletion delay for AWS Secrets Manager upon resource destruction"
}