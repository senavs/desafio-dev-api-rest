CREATE SCHEMA IF NOT EXISTS `DOCK` ;
USE `DOCK` ;

CREATE TABLE IF NOT EXISTS `DOCK`.`PESSOA` (
  `ID_PESSOA` INT NOT NULL AUTO_INCREMENT,
  `NOME` VARCHAR(128) NOT NULL,
  `CPF` CHAR(11) NOT NULL,
  `DATA_NASCIMENTO` DATETIME NOT NULL,
  PRIMARY KEY (`ID_PESSOA`),
  UNIQUE INDEX `ID_PESSOA_UNIQUE` (`ID_PESSOA` ASC),
  UNIQUE INDEX `CPF_UNIQUE` (`CPF` ASC)
);

CREATE TABLE IF NOT EXISTS `DOCK`.`TIPO_CONTA` (
  `ID_TIPO_CONTA` INT NOT NULL AUTO_INCREMENT,
  `NOME` VARCHAR(32) NOT NULL,
  `DESCRICAO` VARCHAR(32) NULL,
  PRIMARY KEY (`ID_TIPO_CONTA`),
  UNIQUE INDEX `ID_TIPO_CONTA_UNIQUE` (`ID_TIPO_CONTA` ASC),
  UNIQUE INDEX `NOME_UNIQUE` (`NOME` ASC)
);

CREATE TABLE IF NOT EXISTS `DOCK`.`CONTA` (
  `ID_CONTA` INT NOT NULL AUTO_INCREMENT,
  `ID_PESSOA` INT NOT NULL,
  `SALDO` DECIMAL(10, 2) NOT NULL DEFAULT 0,
  `LIMITE_SAQUE_DIARIO` DECIMAL(10, 2) NOT NULL DEFAULT 0,
  `ATIVO` TINYINT NOT NULL DEFAULT 1,
  `ID_TIPO_CONTA` INT NOT NULL,
  `DATA_CRIACAO` DATETIME NOT NULL,
  PRIMARY KEY (`ID_CONTA`),
  UNIQUE INDEX `ID_CONTA_UNIQUE` (`ID_CONTA` ASC),
  INDEX `fk_CONTA_PESSOA_idx` (`ID_PESSOA` ASC),
  INDEX `fk_CONTA_TIPO_CONTA1_idx` (`ID_TIPO_CONTA` ASC),
  CONSTRAINT `fk_CONTA_PESSOA`
    FOREIGN KEY (`ID_PESSOA`)
    REFERENCES `DOCK`.`PESSOA` (`ID_PESSOA`),
  CONSTRAINT `fk_CONTA_TIPO_CONTA1`
    FOREIGN KEY (`ID_TIPO_CONTA`)
    REFERENCES `DOCK`.`TIPO_CONTA` (`ID_TIPO_CONTA`)
);

CREATE TABLE IF NOT EXISTS `DOCK`.`TRANSACAO` (
  `ID_TRANSACAO` INT NOT NULL AUTO_INCREMENT,
  `ID_CONTA` INT NOT NULL,
  `VALOR` DECIMAL(10, 2) NOT NULL DEFAULT 0,
  `DATA_CRIACAO` DATETIME NOT NULL,
  PRIMARY KEY (`ID_TRANSACAO`),
  UNIQUE INDEX `ID_TRANSACAO_UNIQUE` (`ID_TRANSACAO` ASC),
  INDEX `fk_TRANSACAO_CONTA1_idx` (`ID_CONTA` ASC),
  CONSTRAINT `fk_TRANSACAO_CONTA1`
    FOREIGN KEY (`ID_CONTA`)
    REFERENCES `DOCK`.`CONTA` (`ID_CONTA`)
);
