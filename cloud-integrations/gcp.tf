# Define the Google Cloud provider
provider "google" {
  project = "my-project-id"
  region  = "us-central1"
}

# Define the container cluster
resource "google_container_cluster" "example" {
  name               = "my-container-cluster"
  location           = var.region
  initial_node_count = 1
}

# Define the container registry
resource "google_container_registry" "example" {
  name = "my-container-registry"
}

# Define the container instance
resource "google_container_node_pool" "example" {
  name       = "my-container-pool"
  location   = var.region
  cluster    = google_container_cluster.example.name
  node_count = 1

  node_config {
    preemptible  = true
    machine_type = "n1-standard-1"
  }

  management {
    auto_repair  = true
    auto_upgrade = true
  }
}

# Define the container instance
resource "google_container_node_pool" "example" {
  name       = "my-container-pool"
  location   = var.region
  cluster    = google_container_cluster.example.name
  node_count = 1

  node_config {
    preemptible  = true
    machine_type = "n1-standard-1"
  }

  management {
    auto_repair  = true
    auto_upgrade = true
  }
}

# Define the container instance
resource "google_container_node_pool" "example" {
  name       = "my-container-pool"
  location   = var.region
  cluster    = google_container_cluster.example.name
  node_count = 1

  node_config {
    preemptible  = true
    machine_type = "n1-standard-1"
  }

  management {
    auto_repair  = true
    auto_upgrade = true
  }
}

# Define the container instance
resource "google_container_node_pool" "example" {
  name       = "my-container-pool"
  location   = var.region
  cluster    = google_container_cluster.example.name
  node_count = 1

  node_config {
    preemptible  = true
    machine_type = "n1-standard-1"
  }

  management {
    auto_repair  = true
    auto_upgrade = true
  }
}

# Define the container instance
resource "google_container_node_pool" "example" {
  name       = "my-container-pool"
  location   = var.region
  cluster    = google_container_cluster.example.name
  node_count = 1

  node_config {
    preemptible  = true
    machine_type = "n1-standard-1"
  }

  management {
    auto_repair  = true
    auto_upgrade = true
  }
}

# Define the container instance
resource "google_container_node_pool" "example" {
  name       = "my-container-pool"
  location   = var.region
  cluster    = google_container_cluster.example.name
  node_count = 1

  node_config {
    preemptible  = true
    machine_type = "n1-standard-1"
  }

  management {
    auto_repair  = true
    auto_upgrade = true
  }
}