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
-- Table structure for table `jogador_campeonato`
--

DROP TABLE IF EXISTS `jogador_campeonato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jogador_campeonato` (
  `id_jogador` int(5) NOT NULL,
  `id_campeonato` int(5) NOT NULL,
  `gols` int(11) DEFAULT '0',
  `cartoes_amarelos` int(11) DEFAULT '0',
  `cartoes_vermelhos` int(11) DEFAULT '0',
  PRIMARY KEY (`id_jogador`,`id_campeonato`),
  KEY `id_campeonato` (`id_campeonato`),
  CONSTRAINT `jogador_campeonato_ibfk_1` FOREIGN KEY (`id_jogador`) REFERENCES `jogadores` (`id`),
  CONSTRAINT `jogador_campeonato_ibfk_2` FOREIGN KEY (`id_campeonato`) REFERENCES `campeonatos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jogador_campeonato`
--

LOCK TABLES `jogador_campeonato` WRITE;
/*!40000 ALTER TABLE `jogador_campeonato` DISABLE KEYS */;
INSERT INTO `jogador_campeonato` VALUES (1,1,0,2,0),(1,2,0,0,0),(2,1,0,5,1),(2,2,0,0,0),(3,1,2,3,1),(3,2,0,0,0),(4,1,2,2,0),(4,2,0,0,0),(5,1,1,3,1),(5,2,0,0,0),(6,1,4,2,0),(6,2,0,0,0),(7,1,0,0,0),(7,2,0,0,0),(8,1,0,0,0),(9,1,0,0,0),(9,2,5,1,0),(10,1,0,0,0),(10,2,0,0,0),(11,1,0,0,0),(11,2,0,0,0),(38,1,0,0,0),(38,2,0,0,0);
/*!40000 ALTER TABLE `jogador_campeonato` ENABLE KEYS */;
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
