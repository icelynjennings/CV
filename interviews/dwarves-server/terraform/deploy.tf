resource "kubernetes_replication_controller" "dwarves" {
  metadata {
    name = "dwarves"
    labels {
      App = "dwarves"
    }
  }

  spec {
    replicas = 2
    selector {
      App = "dwarves"
    }
    template {
      container {
        image = "devopsice/dwarves:alpine"
        name  = "dwarves"

        port {
          container_port = 8000
        }

        resources {
          limits {
            cpu    = "0.5"
            memory = "512Mi"
          }
          requests {
            cpu    = "250m"
            memory = "50Mi"
          }
        }
      }
    }
  }
}

resource "kubernetes_service" "dwarves" {
  metadata {
    name = "dwarves"
  }
  spec {
    selector {
      App = "${kubernetes_replication_controller.dwarves.metadata.0.labels.App}"
    }
    port {
      port = 80
      target_port = 8000
    }

    type = "LoadBalancer"
  }
}

output "lb_ip" {
  value = "${kubernetes_service.dwarves.load_balancer_ingress.0.ip}"
}

