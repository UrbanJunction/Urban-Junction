terraform {
    required_providers {
      azurerm = {
        source = "hashicorp/azurerm"
      }
    }
}

data "azurerm_client_config" "current" {
}

resource "azurerm_resource_group" "urban_junction_rg" {
    name = var.resource_group_name
    location = var.location 
}

resource "azurerm_key_vault" "urban_junction_key_vault" {
    name = var.key_vault_name
    resource_group_name = azurerm_resource_group.urban_junction_rg.name
    location = var.location
    soft_delete_retention_days = 7
    purge_protection_enabled = false 
    sku_name = "standard"
    tenant_id = azurerm_client_config.current.tenant_id
}

resource "azurerm_key_vault_secret" "ny511_secret" {
    name = var.ny511_secret_name
    value = var.ny511_key
    key_vault_id = azurerm_key_vault.urban_junction_key_vault.id
}