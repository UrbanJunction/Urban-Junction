output "vault_uri" {
  value = azurerm_key_vault.urban_junction_key_vault.vault_uri
}

output "secret_511ny_name" {
  value = azurerm_key_vault_secret.ny511_secret.name
}