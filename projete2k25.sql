-- MySQL dump 10.13  Distrib 8.0.43, for Linux (x86_64)
--
-- Host: localhost    Database: projete2k25
-- ------------------------------------------------------
-- Server version	8.0.43-0ubuntu0.24.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NOT NULL,
  `nome` varchar(50) DEFAULT NULL,
  `nome_animal` varchar(50) DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `endereco` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `clientes_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,10,'Gustavo','Rex','11999999999','gustavo@email.com','Rua Exemplo, 123'),(2,10,'sa','sa','+21 (31) 31313-1231','sa','sa'),(3,10,'reergerg','egegeg','+54 (64) 65465-4654','egreg','grege');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exames`
--

DROP TABLE IF EXISTS `exames`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exames` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cliente_id` int NOT NULL,
  `alimentos` json DEFAULT NULL,
  `peso` int DEFAULT NULL,
  `sexo` varchar(10) DEFAULT NULL,
  `data` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `cliente_id` (`cliente_id`),
  CONSTRAINT `exames_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exames`
--

LOCK TABLES `exames` WRITE;
/*!40000 ALTER TABLE `exames` DISABLE KEYS */;
INSERT INTO `exames` VALUES (1,1,'{\"soja\": \"negativo\", \"milho\": \"negativo\", \"peixe\": \"negativo\", \"trigo\": \"positivo\", \"banana\": \"negativo\", \"batata\": \"negativo\", \"maçã\": \"positivo\", \"abobora\": \"negativo\", \"cenoura\": \"positivo\", \"ervilha\": \"negativo\", \"camarão\": \"positivo\", \"leite_vaca\": \"negativo\", \"carne_porco\": \"negativo\", \"ovo_galinha\": \"positivo\", \"carne_bovina\": \"positivo\", \"carne_frango\": \"negativo\"}',72,'M','2025-09-12 09:19:29');
/*!40000 ALTER TABLE `exames` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `senha` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES (10,'Gustavo','teste2@email.com','929608f050eae7a40fc1d3614446a69ecb710ae955dee393fbf39c2276c270ea'),(18,'Gabriel','gabrielvasconcelos@gmail.com','e6955a2c59dc90833986fe0894cf6718dddaa7816bb51bc955cdd3eb4470e554'),(19,'Biel','gabrielvasconcelos073965@gmail.com','e6955a2c59dc90833986fe0894cf6718dddaa7816bb51bc955cdd3eb4470e554'),(20,'Gabriel','gabrielvasconcel@gmail.com','e6955a2c59dc90833986fe0894cf6718dddaa7816bb51bc955cdd3eb4470e554');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-09-21 18:25:57
