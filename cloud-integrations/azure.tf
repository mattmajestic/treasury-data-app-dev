# Define the Azure provider
provider "azurerm" {
  features {}
}

# Define the resource group
resource "azurerm_resource_group" "example" {
  name     = "my-resource-group"
  location = "eastus"
}

# Define the container registry
resource "azurerm_container_registry" "example" {
  name                = "my-container-registry"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  sku                 = "Basic"
  admin_enabled       = true
}

# Define the container registry credentials
data "azurerm_container_registry" "example" {
  name = azurerm_container_registry.example.name
}

# Define the container instance
resource "azurerm_container_group" "example" {
  name                = "my-container-group"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name

  os_type = "Linux"

  container {
    name   = "my-container"
    image  = "my-docker-image:latest"
    cpu    = 1
    memory = 1

    ports {
      port     = 8000
      protocol = "TCP"
    }

    environment_variables = {
      FOO = "BAR"
    }

    secrets = [
      {
        name  = "my-secret"
        value = data.azurerm_container_registry.example.admin_username
      },
      {
        name  = "my-secret2"
        value = data.azurerm_container_registry.example.admin_password
      }
    ]
  }
}
