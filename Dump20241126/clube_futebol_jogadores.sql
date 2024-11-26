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
-- Table structure for table `jogadores`
--

DROP TABLE IF EXISTS `jogadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jogadores` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `cpf` bigint(12) DEFAULT NULL,
  `altura` float(3,2) DEFAULT NULL,
  `data_nascimento` date NOT NULL,
  `telefone` bigint(14) DEFAULT NULL,
  `endereco` varchar(50) NOT NULL,
  `cidade` varchar(50) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `nacionalidade` varchar(50) NOT NULL,
  `salario` float(10,2) DEFAULT NULL,
  `numero_camisa` int(5) NOT NULL,
  `dominancia` varchar(50) NOT NULL,
  `posicao` varchar(50) NOT NULL,
  `contrato` date NOT NULL,
  `condicao` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jogadores`
--

LOCK TABLES `jogadores` WRITE;
/*!40000 ALTER TABLE `jogadores` DISABLE KEYS */;
INSERT INTO `jogadores` VALUES (1,'Rui Costa',2147483647,1.93,'2002-12-14',94564534345,'Rua da Cascata','Abilio Cunt','Santa Catarina','Brasileiro',12000.48,32,'Destro','Goleiro','2027-12-31','Ativo'),(2,'Ramon Dias',456456166,1.84,'2002-03-14',94534536154,'Rua Monteiro Lobato','Jundiaí','São Paulo','Brasileiro',14523.98,3,'Destro','Zagueiro','2027-12-31','Ativo'),(3,'Leandro Novaes',4568653156,1.79,'2001-12-11',98744564514,'Rua da Cascata','Maringá','Paraná','Brasileiro',11548.20,4,'Destro','Goleiro','2027-12-31','Ativo'),(4,'Alberto Rios',4464564204,1.68,'1999-07-05',95153540540,'Avenida 7 de Setembro','Concórdia','Santa Catarina','Brasileiro',15764.50,2,'Destro','Lateral Direito','2026-12-31','Ativo'),(5,'Sorato Mendes',7893131055,1.82,'1998-08-07',97875405647,'Rua Tereza Cristina','Porto Alegre','Rio Grande do Sul','Brasileiro',15489.96,6,'Canhoto','Lateral Esquerdo','2028-12-31','Ativo'),(6,'Carlos Benitez',354645634,1.65,'2002-01-21',94564205404,'Calle Maradona','Buenos Aires','','Argentino',17546.69,5,'Canhoto','Volante','2027-12-31','Ativo'),(7,'Ricardo Nunes',5445663100,1.77,'2001-09-08',97899546446,'Rua Felipe Schimit','Florianópolis','Santa Catarina','Brasileiro',15674.68,8,'Destro','Volante','2026-12-31','Ativo'),(8,'Rafael Junior',8978345048,1.74,'2000-03-08',93105788464,'Rua Carlos Drummont','Salvador','Bahia','Brasileiro',14568.50,7,'Destro','Meia','2027-12-31','Ativo'),(9,'Samuel Zanin',4568756459,1.80,'2003-09-07',93124565407,'Rua Santos Dummont','Rio De Janeiro','Rio De Janeiro','Brasileiro',18546.77,10,'Canhoto','Meia','2027-12-31','Ativo'),(10,'Tiago Fragoso',4567845642,1.71,'1999-12-28',97854646546,'Rua Jasmin','Mossoró','Rio Grande Do Norte','Brasileiro',19872.50,11,'Destro','Atacante','2025-12-31','Ativo'),(11,'Ramon Castillo',8978978464,1.90,'1998-11-10',98745645113,'Calle Bolívar','Calle Bolívar','Bolívar','Equatoriano',20211.10,9,'Destro','Atacante','2028-12-31','Ativo'),(14,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(15,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(16,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(17,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(18,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(19,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(20,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(21,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(22,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(23,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(24,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(25,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(26,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(27,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(28,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(29,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(30,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(31,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(32,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(33,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(34,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(35,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(36,'',0,0.00,'0000-00-00',0,'','','','',0.00,0,'','','0000-00-00',''),(38,'Rodrigo Rodrigues Robaina',568765764,1.83,'1990-05-19',98465431456,'Pedro Candioto','Cocal Do Sul','Santa Catarina','Brasileiro',100000.00,12,'canhoto','goleiro','2028-12-31','Ativo');
/*!40000 ALTER TABLE `jogadores` ENABLE KEYS */;
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
