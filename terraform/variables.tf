variable "ny511_key" {
    description = "dev key for NY511"
    type = string
}

variable "location" {
    description = "azure location"
    type = string 
    default = "East US"
}

variable "resource_group_name" {
    description = "name of resource group to create"
    type = string 
    default = "urban-junction-resource-group"
}

variable "key_vault_name" {
    description = "name for key vault"
    type = string
    default = "urban-junction-vault"
}

variable "ny511_secret_name" {
    description = "name for NY511 API key secret"
    type = string
    default = "ny511-api-secret"
}