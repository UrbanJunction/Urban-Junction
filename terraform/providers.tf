terraform {
    required_providers {
      azurerm = {
        source = "hashicorp/azurerm"
      }
    }
}

provider "azurerm" {
  skip_provider_registration = true 
  features {}
}

data "azurerm_client_config" "current" {
}
