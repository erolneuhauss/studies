resource "kubernetes_service" "tf-k8s-service" {
  metadata {
    name = "tf-k8s-service"
    labels = {
      name = "tf-k8s-deployment"
    }
  }

  spec {
    selector = {
        name = "tf-k8s-deployment"
      }

    port {
      node_port   = 30801
      port        = 80
      target_port = 80
    }
    type = "NodePort"
  }
}

