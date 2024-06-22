USE `locadora`; 

-- Populando a tabela `modelo`
INSERT INTO `modelo` (`id_modelo`, `nome`, `ano`, `marca`, `preco_diaria`, `capacidade`)
VALUES
('MDL001', 'Civic', 2020, 'Honda', 150.00, 5),
('MDL002', 'Corolla', 2021, 'Toyota', 160.00, 5)
ON DUPLICATE KEY UPDATE `id_modelo` = `id_modelo`;

INSERT INTO `loja` (`id_loja`, `cep`, `numero`)
VALUES
('LJ001', 12345678, 100),
('LJ002', 87654321, 200)
ON DUPLICATE KEY UPDATE `id_loja` = `id_loja`;

INSERT INTO `patio` (`id_patio`, `vagas_disp`, `vagas_pre`, `loja`)
VALUES
('PTY001', 10, 5, 'LJ001'),
('PTY002', 8, 4, 'LJ002')
ON DUPLICATE KEY UPDATE `id_patio` = `id_patio`;

INSERT INTO `carro` (`placa`, `numero_chassi`, `cor`, `disponibilidade`, `modelo`, `patio`)
VALUES
('HIJ1817', '7HGBH41JXMN109152', 'Amarelo', "Disponível", 'MDL001', 'PTY001'),
('PQR1119', '8HGBH41JXMN109143', 'Roxo', "Ocupado", 'MDL002', 'PTY002')
ON DUPLICATE KEY UPDATE `placa` = `placa`;

INSERT INTO `cliente` (`complemento`, `cep`, `email`, `telefone`)
VALUES
('Apto 303', 12345001, 'cliente3@example.com', 777777777),
('Apto 404', 54321001, 'cliente4@example.com', 666666666),
('Apto 505', 13579000, 'cliente5@example.com', 555555555),
('Apto 606', 98765432, 'cliente6@example.com', 444444444);


INSERT INTO `fisica` (`cpf`, `num_cliente`, `nome`)
VALUES
(00000001111, 1, 'Vinicius Morais'),
(11116223211, 2, 'Ana Clara')
ON DUPLICATE KEY UPDATE `cpf` = `cpf`;

INSERT INTO `juridica` (`cnpj`, `num_cliente`, `razao_social`)
VALUES
(12345678901234, 3, 'Empresa A'),
(98765432109876, 4, 'Empresa B')
ON DUPLICATE KEY UPDATE `cnpj` = `cnpj`;

-- Populando a tabela `reserva`
INSERT INTO `reserva` (`num_diarias`, `data_inicio`, `cliente`, `carro`) VALUES
(5, '2024-06-01', 1, 'HIJ1817'),
(3, '2024-06-02', 3, 'PQR1119');

INSERT INTO `pagamento` (`id_pagamento`, `tipo`, `valor`, `reserva`)
VALUES
('PGT001', 'Dinheiro', 100.00, 1),
('PGT002', 'Cartão', 150.00, 2)
ON DUPLICATE KEY UPDATE `id_pagamento` = `id_pagamento`;

INSERT INTO `contato_loja` (`loja`, `contato`)
VALUES
('LJ001', 123456789),
('LJ002', 987654321)
ON DUPLICATE KEY UPDATE `loja` = `loja`;

INSERT INTO `funcionario` (`cpf`, `salario`, `nome`, `loja`)
VALUES
(12345678901, 2000.00, 'João', 'LJ001'),
(98765432100, 2500.00, 'Maria', 'LJ002')
ON DUPLICATE KEY UPDATE `cpf` = `cpf`;

INSERT INTO `horario_loja` (`loja`, `periodo`, `dia`)
VALUES
('LJ001', '08:00 - 22:00', 'Segunda'),
('LJ001', '08:00 - 22:00', 'Terça'),
('LJ001', '08:00 - 22:00', 'Quarta'),
('LJ001', '08:00 - 22:00', 'Quinta'),
('LJ001', '08:00 - 22:00', 'Sexta'),
('LJ001', '08:00 - 22:00', 'Sábado'),
('LJ002', '08:00 - 22:00', 'Segunda'),
('LJ002', '08:00 - 22:00', 'Terça'),
('LJ002', '08:00 - 22:00', 'Quarta'),
('LJ002', '08:00 - 22:00', 'Quinta'),
('LJ002', '08:00 - 22:00', 'Sexta'),
('LJ002', '08:00 - 22:00', 'Sábado'),
('LJ002', '08:00 - 16:00', 'Domingo')
ON DUPLICATE KEY UPDATE `loja` = `loja`;

INSERT INTO `manobrista` (`cpf`, `patio`)
VALUES
(12345678901, 'PTY001'),
(98765432100, 'PTY002')
ON DUPLICATE KEY UPDATE `cpf` = `cpf`;

INSERT INTO `manobrista_horario` (`cpf`, `dia`, `turno`)
VALUES
(12345678901, 'Segunda', 'Manhã'),
(12345678901, 'Segunda', 'Tarde'),
(12345678901, 'Quarta', 'Manhã'),
(12345678901, 'Sexta', 'Manhã'),
(12345678901, 'Sexta', 'Tarde'),
(12345678901, 'Sábado', 'Manhã'),
(98765432100, 'Todos', 'Tarde')
ON DUPLICATE KEY UPDATE `cpf` = `cpf`;