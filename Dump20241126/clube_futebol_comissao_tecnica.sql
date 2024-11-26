-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: clube_futebol
-- ------------------------------------------------------
-- Server version	5.5.20-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comissao_tecnica`
--

DROP TABLE IF EXISTS `comissao_tecnica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comissao_tecnica` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `cpf` int(12) NOT NULL,
  `data_nascimento` date NOT NULL,
  `telefone` int(12) NOT NULL,
  `endereco` varchar(50) NOT NULL,
  `cidade` varchar(50) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `nacionalidade` varchar(50) NOT NULL,
  `ocupacao` varchar(50) NOT NULL,
  `contrato` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comissao_tecnica`
--

LOCK TABLES `comissao_tecnica` WRITE;
/*!40000 ALTER TABLE `comissao_tecnica` DISABLE KEYS */;
INSERT INTO `comissao_tecnica` VALUES (1,'João Marciel',2147483647,'1968-10-12',2147483647,'Rua do Apelo','Cascavel','Paraná','Brasileiro','Técnico','2026-12-31'),(2,'José Sirley',2147483647,'1988-06-22',2147483647,'Rua Castelo Branco','Porto Alegre','Rio Grande do Sul','Brasileiro','Auxiliar Técnico','2026-12-31'),(3,'Francisco Bento',2147483647,'1988-02-28',2147483647,'Rua Solimões','Cuiabá','Mato Grosso','Brasileiro','Auxiliar Técnico','2026-12-31'),(5,'Roger Cinclair',2147483647,'1990-12-23',2147483647,'Rua Sartor','Criciúma','Santa Catarina','Brasileiro','Preparador de Goleiro','2027-12-31'),(6,'Biribinha',2147483647,'1985-12-31',354343735,'Rua dos carai','Laguna','Santa Catarina','Brasileiro','Massagista','2025-12-31');
/*!40000 ALTER TABLE `comissao_tecnica` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-26 13:25:40
