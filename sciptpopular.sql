-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: locadora_carro
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

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

DROP SCHEMA IF EXISTS `locadora`;
CREATE SCHEMA `locadora`;
USE `locadora`; 

--
-- Table structure for table `carro`
--

DROP TABLE IF EXISTS `carro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carro` (
  `placa` varchar(7) NOT NULL,
  `numero_chassi` varchar(17) NOT NULL,
  `cor` varchar(12) DEFAULT NULL,
  `disponibilidade` ENUM("Disponível", "Ocupado") DEFAULT "Disponível",
  `modelo` varchar(30) DEFAULT NULL,
  `patio` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`placa`),
  UNIQUE KEY `numero_chassi` (`numero_chassi`),
  KEY `modelo` (`modelo`),
  KEY `patio` (`patio`),
  CONSTRAINT `carro_ibfk_1` FOREIGN KEY (`modelo`) REFERENCES `modelo` (`id_modelo`),
  CONSTRAINT `carro_ibfk_2` FOREIGN KEY (`patio`) REFERENCES `patio` (`id_patio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carro`
--

LOCK TABLES `carro` WRITE;
/*!40000 ALTER TABLE `carro` DISABLE KEYS */;
/*!40000 ALTER TABLE `carro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `Num_cliente` int NOT NULL AUTO_INCREMENT,
  `complemento` text DEFAULT NULL,
  `cep` varchar(8) DEFAULT NULL,
  `email` text DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  PRIMARY KEY `Num_cliente` (`Num_cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contato_loja`
--

DROP TABLE IF EXISTS `contato_loja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contato_loja` (
  `loja` varchar(8) NOT NULL,
  `contato` float NOT NULL,
  PRIMARY KEY (`loja`,`contato`),
  UNIQUE KEY `loja` (`loja`),
  CONSTRAINT `contato_loja_ibfk_1` FOREIGN KEY (`loja`) REFERENCES `loja` (`id_loja`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contato_loja`
--

LOCK TABLES `contato_loja` WRITE;
/*!40000 ALTER TABLE `contato_loja` DISABLE KEYS */;
/*!40000 ALTER TABLE `contato_loja` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fisica`
--

DROP TABLE IF EXISTS `fisica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fisica` (
  `cpf` varchar(11) NOT NULL,
  `num_cliente` int NOT NULL,
  `nome` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`cpf`),
  UNIQUE KEY `cpf` (`cpf`),
  KEY `num_cliente` (`num_cliente`),
  CONSTRAINT `fisica_ibfk_1` FOREIGN KEY (`num_cliente`) REFERENCES `cliente` (`Num_cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fisica`
--

LOCK TABLES `fisica` WRITE;
/*!40000 ALTER TABLE `fisica` DISABLE KEYS */;
/*!40000 ALTER TABLE `fisica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionario`
--

DROP TABLE IF EXISTS `funcionario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionario` (
  `cpf` varchar(11) NOT NULL,
  `salario` float DEFAULT NULL,
  `nome` varchar(30) DEFAULT NULL,
  `loja` varchar(8) NOT NULL,
  PRIMARY KEY (`cpf`),
  UNIQUE KEY `cpf` (`cpf`),
  UNIQUE KEY `loja` (`loja`),
  CONSTRAINT `funcionario_ibfk_1` FOREIGN KEY (`loja`) REFERENCES `loja` (`id_loja`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionario`
--

LOCK TABLES `funcionario` WRITE;
/*!40000 ALTER TABLE `funcionario` DISABLE KEYS */;
/*!40000 ALTER TABLE `funcionario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `horario_loja`
--

DROP TABLE IF EXISTS `horario_loja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `horario_loja` (
  `loja` varchar(8) NOT NULL,
  `periodo` varchar(100) NOT NULL,
  `dia` ENUM("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo", "Úteis", "Todos") NOT NULL,
  PRIMARY KEY (`loja`,`periodo`,`dia`),
  UNIQUE KEY `loja` (`loja`),
  CONSTRAINT `horario_loja_ibfk_1` FOREIGN KEY (`loja`) REFERENCES `loja` (`id_loja`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `horario_loja`
--

LOCK TABLES `horario_loja` WRITE;
/*!40000 ALTER TABLE `horario_loja` DISABLE KEYS */;
/*!40000 ALTER TABLE `horario_loja` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `juridica`
--

DROP TABLE IF EXISTS `juridica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `juridica` (
  `cnpj` varchar(14) NOT NULL,
  `num_cliente` int NOT NULL,
  `razao_social` varchar(255) NOT NULL,
  PRIMARY KEY (`cnpj`),
  UNIQUE KEY `cnpj` (`cnpj`),
  KEY `num_cliente` (`num_cliente`),
  CONSTRAINT `juridica_ibfk_1` FOREIGN KEY (`num_cliente`) REFERENCES `cliente` (`Num_cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `juridica`
--

LOCK TABLES `juridica` WRITE;
/*!40000 ALTER TABLE `juridica` DISABLE KEYS */;
/*!40000 ALTER TABLE `juridica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loja`
--

DROP TABLE IF EXISTS `loja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loja` (
  `id_loja` varchar(8) NOT NULL,
  `cep` varchar(8) DEFAULT NULL,
  `numero` int DEFAULT NULL,
  PRIMARY KEY (`id_loja`),
  UNIQUE KEY `id_loja` (`id_loja`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loja`
--

LOCK TABLES `loja` WRITE;
/*!40000 ALTER TABLE `loja` DISABLE KEYS */;
/*!40000 ALTER TABLE `loja` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manobrista`
--

DROP TABLE IF EXISTS `manobrista`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manobrista` (
  `cpf` varchar(11) NOT NULL,
  `patio` varchar(8) NOT NULL,
  PRIMARY KEY (`cpf`),
  UNIQUE KEY `cpf` (`cpf`),
  UNIQUE KEY `patio` (`patio`),
  CONSTRAINT `manobrista_ibfk_1` FOREIGN KEY (`cpf`) REFERENCES `funcionario` (`cpf`),
  CONSTRAINT `manobrista_ibfk_2` FOREIGN KEY (`patio`) REFERENCES `patio` (`id_patio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manobrista`
--

LOCK TABLES `manobrista` WRITE;
/*!40000 ALTER TABLE `manobrista` DISABLE KEYS */;
/*!40000 ALTER TABLE `manobrista` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manobrista_horario`
--

DROP TABLE IF EXISTS `manobrista_horario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manobrista_horario` (
  `cpf` varchar(11) NOT NULL,
  `dia` ENUM("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo", "Úteis", "Todos") NOT NULL,
  `turno` ENUM("Manhã", "Tarde", "Noite") NOT NULL,
  PRIMARY KEY (`cpf`,`dia`,`turno`),
  UNIQUE KEY `cpf` (`cpf`),
  UNIQUE KEY `dia` (`dia`),
  CONSTRAINT `manobrista_horario_ibfk_1` FOREIGN KEY (`cpf`) REFERENCES `manobrista` (`cpf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manobrista_horario`
--

LOCK TABLES `manobrista_horario` WRITE;
/*!40000 ALTER TABLE `manobrista_horario` DISABLE KEYS */;
/*!40000 ALTER TABLE `manobrista_horario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `modelo`
--

DROP TABLE IF EXISTS `modelo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `modelo` (
  `id_modelo` varchar(8) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `ano` varchar(10) NOT NULL,
  `marca` varchar(255) NOT NULL,
  `preco_diaria` float DEFAULT NULL,
  `capacidade` int DEFAULT NULL,
  PRIMARY KEY (`id_modelo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modelo`
--

LOCK TABLES `modelo` WRITE;
/*!40000 ALTER TABLE `modelo` DISABLE KEYS */;
/*!40000 ALTER TABLE `modelo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagamento`
--

DROP TABLE IF EXISTS `pagamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagamento` (
  `id_pagamento` varchar(8) NOT NULL,
  `tipo` ENUM("Boleto", "Pix", "Cartão", "Dinheiro") NOT NULL,
  `valor` float unsigned DEFAULT NULL,
  `reserva` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_pagamento`),
  UNIQUE KEY `id_pagamento` (`id_pagamento`),
  UNIQUE KEY `reserva` (`reserva`),
  CONSTRAINT `pagamento_ibfk_1` FOREIGN KEY (`reserva`) REFERENCES `reserva` (`id_reserva`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagamento`
--

LOCK TABLES `pagamento` WRITE;
/*!40000 ALTER TABLE `pagamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `pagamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patio`
--

DROP TABLE IF EXISTS `patio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patio` (
  `id_patio` varchar(8) NOT NULL,
  `vagas_disp` int DEFAULT NULL,
  `vagas_pre` int DEFAULT NULL,
  `loja` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`id_patio`),
  UNIQUE KEY `id_patio` (`id_patio`),
  KEY `loja` (`loja`),
  CONSTRAINT `patio_ibfk_1` FOREIGN KEY (`loja`) REFERENCES `loja` (`id_loja`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patio`
--

LOCK TABLES `patio` WRITE;
/*!40000 ALTER TABLE `patio` DISABLE KEYS */;
/*!40000 ALTER TABLE `patio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reserva`
--

DROP TABLE IF EXISTS `reserva`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reserva` (
  `id_reserva` int NOT NULL AUTO_INCREMENT,
  `num_diarias` int unsigned NOT NULL,
  `data_inicio` date DEFAULT NULL,
  `cliente` int NOT NULL,
  `carro` varchar(7) NOT NULL,
  PRIMARY KEY (`id_reserva`),
  UNIQUE KEY `id_reserva` (`id_reserva`),
  KEY `cliente` (`cliente`),
  KEY `carro` (`carro`),
  CONSTRAINT `reserva_ibfk_1` FOREIGN KEY (`cliente`) REFERENCES `cliente` (`Num_cliente`),
  CONSTRAINT `reserva_ibfk_2` FOREIGN KEY (`carro`) REFERENCES `carro` (`placa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reserva`
--

LOCK TABLES `reserva` WRITE;
/*!40000 ALTER TABLE `reserva` DISABLE KEYS */;
/*!40000 ALTER TABLE `reserva` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-03 22:14:15
